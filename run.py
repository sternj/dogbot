import nltk
import os
from dogs.bot.client import DogClient

nltk.download('punkt')

client = DogClient()

client.run(os.environ["DISCORD_KEY"])