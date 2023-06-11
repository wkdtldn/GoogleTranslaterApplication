import googletrans  

translator = googletrans.Translator()

print("{번역기}")
while True:
    trans = input("한국어 검색(1)\n영어 검색(2)\n")
    if trans == "1":
        str1 = input("한국어 => 영어\n입력: ")
        result1 = translator.translate(str1,dest='en')
        print(f"%s => {result1.text}"%str1)
        print('-'*50)

    elif trans == "2":
        str2 = input("영어 => 한국어\n입력:")
        result2 = translator.translate(str2,dest='ko')
        print(f"%s => {result2.text}"%str2)
        print('-'*50)
    
    else:
        break








# from flask import Flask, render_template
# import googletrans  

# app = Flask(__name__)

# translator = googletrans.Translator()

# @app.route('/')
# def index(methods=['GET', 'POST']):
#     return "hello"