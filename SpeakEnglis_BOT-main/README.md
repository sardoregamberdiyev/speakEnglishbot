# SpeakEnglis_BOT 🚀    Muallif: [Anvar Narzullayev](https://github.com/anvarnarz)
Bu telegram bot hisoblanadi

[![platform](https://img.shields.io/github/followers/5?style=social)](https://t.me/nurbekdev)
[![GitHub license](https://img.shields.io/badge/License-Apache2.0-blue.svg)](LICENSE)
  # Botni Herokuga yuklash qadamlari
 ## * 0. Tayyorgarlik

heroku.com sahifaisga kirib ro’yxatdan o’tasiz

Git CLI yuklab oling va o’rnating: https://git-scm.com/downloads

Heroku CLI yuklab oling va o’rnating: https://devcenter.heroku.com/articles/heroku-cli#download-and-install

## * 1. Fayllarni tayyorlaymiz
 
Botingizni va kerakli fayllarni bitta papkaga saqlang

Asosy bot faylini `bot.py` yoki main.py deb nomlang

Papkada `__init__.py` faylini yarating (ichiga hech narsa yozish shart emas)

Papkada Procfile faylini yarating va ichiga quyidagi kodni yozing: worker: python `bot.py` (bot.py o’rniga asosiy faylingiz nomini yozing)

Agar pipenv muhitidan foydalanmagan bo’lsangiz, requirements.txt faylini yarating va ichiga barcha kerakli paketlar nomini yozing

aiogram==2.14.3

wikipedia

requirements==2.26.3

## * 2. Git

Quyidagi buyruqlarni Windows Powershell (terminal) dasturida oldinma-ketin bajaring:

      git init

      git add -A

      git commit -m 'initial commit'

## * 3. Heroku CLI

 Quyidagi buyruqlarni Windows Powershell (terminal) dasturida oldinma-ketin bajaring:

      heroku login

      heroku create

 Agar botni avval yaratilgan app ichiga yuklamoqchi bo’lsangiz:

      heroku git:remote -a app_nomi

      git push heroku master

      heroku ps:scale worker=1

Tabriklaymiz, botingiz ishga tushdi 🙌


Agar botingiz ishlamasa, `heroku logs --tail` buyrug’i yordamida serverdagi loglarni ko’rish mumkin.




