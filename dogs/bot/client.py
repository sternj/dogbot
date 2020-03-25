import discord
import io
from dogs.captioner import caption



class DogClient(discord.Client):
    async def on_message(self, message):
        if message.author == self.user:
            return
        if message.content.startswith('-dog'):
            has_bottom = True
            splitmsg = message.content.split()
            if len(splitmsg) > 1 and 'nobottom' in splitmsg[1]:
                has_bottom = False
            img = caption.put_text(has_bottom)
            img_recv = io.BytesIO()
            img.save(img_recv, "JPEG")
            img_recv.seek(0)
            await message.channel.send(file=discord.File(img_recv, 'dog.jpg'))

