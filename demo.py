from openai import OpenAI
from main import client

response = client.images.generate(
    model="dall-e-3",
    prompt="Cat laying with dog",
    n=1,
    size="1792x1024"
)

print(response.data[0].url)

"""openai.images.generate()"""
"""image_url = response.data[0].url"""