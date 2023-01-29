import openai
import requests
from PIL import Image
import matplotlib.pyplot as plt
from CONFIG import OPENAI_API_KEY

openai.api_key = OPENAI_API_KEY


def begin():
    userInput = input(
        "Enter a prompt and we will generate your image! The more specific the better :)")
    createImage(userInput)


def createImage(userInput):
    response = openai.Image.create(
        prompt=userInput,
        n=1,
        size="1024x1024"
    )
    image_url = response['data'][0]['url']

    r = requests.get(image_url, stream=True)
    img = Image.open(r.raw)
    img.show()


# def editImage():
#     response = openai.Image.create_edit(
#         image=open("sunlit_lounge.png", "rb"),
#         mask=open("mask.png", "rb"),
#         prompt="A sunlit indoor lounge area with a pool containing a flamingo",
#         n=1,
#         size="1024x1024"
#     )
#     image_url = response['data'][0]['url']


begin()
