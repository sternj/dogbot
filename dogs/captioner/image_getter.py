
import requests
from PIL import Image
from io import BytesIO

def get_random_image_url() -> str:
    return requests.get('https://dog.ceo/api/breeds/image/random').json()['message']

def get_image_bytes() -> BytesIO:
    return BytesIO(requests.get(get_random_image_url()).content)

def get_random_image():
    return Image.open(get_image_bytes())