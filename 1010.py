import random
print('1~100中猜一個數字,猜到對''')

answer=random.randint(1,100)



while True:
     
    guess1 = input('玩家一猜猜看:')
    guess1 = int(guess1)
     
    guess2 = input('玩家二猜猜看:')
    guess2 = int(guess2)
     
     
    if guess1 != answer:
        if guess2 !=answer:
             print('都猜錯')
        else:
            print('玩家二猜對')
    elif guess1 == answer:
          if guess2 != answer:
            print('玩家一猜對')
          else:
             print('恭喜都答對!!!!!!!')
    else:
        print('恭喜都答對!!!!!!!!!!!')
        break
