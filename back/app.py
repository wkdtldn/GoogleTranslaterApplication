from flask import Flask, render_template
import googletrans  

# import googletrans  

# translator = googletrans.Translator()

# print("{번역기}")
# while True:
#     trans = input("한국어 검색(1)\n영어 검색(2)\n")
#     if trans == "1":
#         str1 = input("한국어 => 영어\n입력: ")
#         result1 = translator.translate(str1,dest='en')
#         print(f"%s => {result1.text}"%str1)
#         print('-'*50)

#     elif trans == "2":
#         str2 = input("영어 => 한국어\n입력:")
#         result2 = translator.translate(str2,dest='ko')
#         print(f"%s => {result2.text}"%str2)
#         print('-'*50)
    
#     else:
#         break

app = Flask(__name__)

translator = googletrans.Translator()

@app.route('/')
def index(methods=['GET', 'POST']):
    return "hello"

@app.route('/main')
def main(methods=['GET', 'POST']):
    return "main"

@app.route('/trans_ko')
def trans__ko():
    word1 = "안녕하세요"
    result_ko = translator.translate(word1,dest='en')
    return f"%s => {result_ko.text}"%word1

@app.route('/trans_en')
def trans__en():
    word2 = "hello"
    result_en = translator.translate(word2,dest='ko')
    return f"%s => {result_en.text}"%word2


    
if __name__ == '__main__':
    app.run(debug=True)