import random

soras = {
    'الفاتحة' : 7,
    'الاعراف' : 206,
    'الانفال' : 75,
    'يونس' : 109,
    'هود' : 123,
    'يوسف' : 111,
    'الرعد' : 43,
    'ابراهيم' : 52,
    'الحجر' : 99,
    'النحل' : 128,
    'الاسراء' : 111
}



keys = list(soras.keys())
while True:
    sora = random.choice(keys)
    question = soras[sora]
    print(sora)
    answer = input('')

    if int(answer) == question:
        print("correct")
    else:
        print(f"Wrong the answer is {question}.")
        
    


