from openai import OpenAI
from dotenv import load_dotenv
import os
import requests

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

response = client.images.generate(
    model="dall-e-3",
    prompt="Generate an image of gray tabby cat hugging an otter with an orange scarf",
    n=1,
    size="1024x1024"
)

# obter o URL da imagem gerada
image_url = response.data[0].url

# baixar a imagem e salvá-la localmente
img_data = requests.get(image_url).content

# salvar a imagem em um arquivo
with open("./dados/cat_and_otter.png", "wb") as handler:
    handler.write(img_data)