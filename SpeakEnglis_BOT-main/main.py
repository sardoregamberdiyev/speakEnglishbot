
import logging

from aiogram import Bot, Dispatcher, executor, types

from oxfort import getDefinitions
from googletrans import Translator
translator = Translator()

API_TOKEN = 'Bu yerda sizning TOKENINGIZ'

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    """
    This handler will be called when user sends `/start` or `/help` command
    """
    await message.reply(f"Salom!\nMen  SpeakEnglishBot!\nPowered by @nurbekdev.")

@dp.message_handler(commands=[ 'help'])
async def send_welcome(message: types.Message):
    """
    This handler will be called when user sends `/start` or `/help` command
    """
    await message.reply("Bu bot yuborgan so'zingiz 2ta so'zdan kam bo'lsa, engliz tilida ma'nosni va talaffuzini audio shaklda qaytaradi.\nAks holda eng-uz yoki uz-eng da tarjima qilib beradi")



@dp.message_handler()
async def tarjimon(message: types.Message):
    print(message)
    lang = translator.detect(message.text).lang
    if len(message.text.split()) > 2:
        dest = 'uz' if lang == 'en' else 'en'
        await message.reply(translator.translate(message.text, dest).text)
    else:
        if lang=='en':
            word_id = message.text
        else:
            word_id = translator.translate(message.text, dest='en').text

        lookup = getDefinitions(word_id)
        if lookup:
            await message.reply(f"Word: {word_id} \nDefinitions:\n{lookup['definitions']}")
            if lookup.get('audio'):
                await message.reply_voice(lookup['audio'])
        else:
            await message.reply("Bunday so'z topilmadi")


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
