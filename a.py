import googletrans

translator = googletrans.Translator()

print("번역기(스킵: skip it12/스탑: stop12)")
print()
while True:
    str1 = input("한국어 => 영어\n입력: ")
    if str1 == "skip it12":
        pass
    elif str1 == "stop12":
        break
    else:
        result1 = translator.translate(str1,dest='en')
        print(f"%s => {result1.text}"%str1)
    print('-'*50)

    str2 = input("영어 => 한국어\n입력:")
    if str2 == "skip it12":
        pass
    elif str2 == "stop12":
        break
    else:
        result2 = translator.translate(str1,dest='ko')
        print(f"%s => {result2.text}"%str2)
    print('-'*50)