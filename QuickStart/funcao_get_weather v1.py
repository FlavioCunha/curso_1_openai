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

def get_weather_real(location):
    # Exemplo usando Open-Meteo (https://open-meteo.com/)
    # Você pode adaptar para outro serviço, como WeatherAPI, Weather.com, etc.
    # Aqui, vamos usar latitude/longitude de Niterói como exemplo
    if "Niterói" in location:
        latitude = -22.8832
        longitude = -43.1034
    else:
        # Para outros locais, você pode usar uma API de geocoding para buscar latitude/longitude
        latitude = -22.8832
        longitude = -43.1034

    url = (
        f"https://api.open-meteo.com/v1/forecast"
        f"?latitude={latitude}&longitude={longitude}&current_weather=true"
    )
    resp = requests.get(url)
    if resp.status_code == 200:
        data = resp.json()
        temp = data["current_weather"]["temperature"]
        weather_code = data["current_weather"]["weathercode"]
        # Simples descrição baseada no código do tempo
        description = {
            0: "Ensolarado",
            1: "Principalmente ensolarado",
            2: "Parcialmente nublado",
            3: "Nublado"
        }.get(weather_code, "Tempo desconhecido")
        return {"temperature": f"{temp}°C", "description": description}
    else:
        return {"temperature": "N/A", "description": "Não foi possível obter o tempo"}



# 1. Primeira chamada: modelo pede execução da função
messages = [{"role": "user", "content": "What is the weather like in Niterói today?"}]
response = client.chat.completions.create(
    model="gpt-4o",
    messages=messages,
    tools=tools
)

tool_calls = response.choices[0].message.tool_calls
if tool_calls:
    print("O modelo solicitou a execução da função:")
    print(tool_calls)

    # Extrai o argumento location da chamada da função
    import json
    arguments = json.loads(tool_calls[0].function.arguments)
    location = arguments["location"]

    # Chama a função real de clima
    weather_result = get_weather_real(location)

    # 2. Envia o resultado real para o modelo
    function_response = {
        "role": "tool",
        "tool_call_id": tool_calls[0].id,
        "name": "get_weather",
        "content": json.dumps(weather_result, ensure_ascii=False)
    }
    messages.append({
        "role": "assistant",
        "tool_calls": [tool_calls[0].to_dict()] # Adiciona a chamada da função ao histórico
    })
    messages.append(function_response)

    # 3. Segunda chamada: modelo responde ao usuário usando o resultado da função
    final_response = client.chat.completions.create(
        model="gpt-4o",
        messages=messages
    )
    print("\nResposta final do modelo:")
    print(final_response.choices[0].message.content)
else:
    print(response.choices[0].message.content)