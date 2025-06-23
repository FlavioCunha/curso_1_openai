from openai import OpenAI
from dotenv import load_dotenv
import os
import requests

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

tools = [{
    "type": "function",
    "function": {
        "name": "get_weather",
        "description": "Get current temperature for a given location.",
        "parameters": {
            "type": "object",
            "properties": {
                "location": {
                    "type": "string",
                    "description": "City and country e.g. Niterói, RJ, Brazil"
                }
            },
            "required": ["location"],
            "additionalProperties": False
        }
    }
}]

def get_lat_lon_from_city(city_name):
    url = "https://nominatim.openstreetmap.org/search"
    params = {
        "q": city_name,
        "format": "json",
        "limit": 1
    }
    resp = requests.get(url, params=params, headers={"User-Agent": "Mozilla/5.0"})
    if resp.status_code == 200 and resp.json():
        data = resp.json()[0]
        return float(data["lat"]), float(data["lon"])
    else:
        return None, None

def get_weather_real(location):
    latitude, longitude = get_lat_lon_from_city(location)
    if latitude is None or longitude is None:
        return {"temperature": "N/A", "description": "Cidade não encontrada"}
    url = (
        f"https://api.open-meteo.com/v1/forecast"
        f"?latitude={latitude}&longitude={longitude}&current_weather=true"
    )
    resp = requests.get(url)
    if resp.status_code == 200:
        data = resp.json()
        temp = data["current_weather"]["temperature"]
        weather_code = data["current_weather"]["weathercode"]
        description = {
            0: "Ensolarado",
            1: "Principalmente ensolarado",
            2: "Parcialmente nublado",
            3: "Nublado"
        }.get(weather_code, "Tempo desconhecido")
        return {"temperature": f"{temp}°C", "description": description}
    else:
        return {"temperature": "N/A", "description": "Não foi possível obter o tempo"}

# Solicita a cidade ao usuário
cidade = input("Digite a cidade (ex: Niterói): ")

# 1. Primeira chamada: modelo pede execução da função
messages = [{"role": "user", "content": f"What is the weather like in {cidade} today?"}]
response = client.chat.completions.create(
    model="gpt-4o",
    messages=messages,
    tools=tools
)

tool_calls = response.choices[0].message.tool_calls
if tool_calls:
    import json
    arguments = json.loads(tool_calls[0].function.arguments)
    location = arguments["location"]

    weather_result = get_weather_real(location)

    function_response = {
        "role": "tool",
        "tool_call_id": tool_calls[0].id,
        "name": "get_weather",
        "content": json.dumps(weather_result, ensure_ascii=False)
    }
    messages.append({
        "role": "assistant",
        "tool_calls": [tool_calls[0].to_dict()]
    })
    messages.append(function_response)

    final_response = client.chat.completions.create(
        model="gpt-4o",
        messages=messages
    )
    print("\nResposta final do modelo:")
    print(final_response.choices[0].message.content)
else:
    print(response.choices[0].message.content)