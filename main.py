import random as random

print('Здравствуй дорогой друг , спасибо что решил пройти этот квест, приятной игры!')
name = input('Введи свое имя --- ')
print('-')
print('-')
print("""Глава-1. Вы попали в темный жуткий лес 
---------Где  кроме своего дыхания 
---------ты ничего не слышишь
---------кроме своих ног
---------ничего не видишь.Страшно.....
--------------------------------------
Что ты думаешь первым тебе стоит сделать ?
- - - - - - -  - - - - - - - - - -  - - - """)
hod1 = input('''1.[Поискать ,что можно поджечь]
2.[Лечь спать на траве]

--- ''')

if hod1 ==  '1':
    print('Ты  нашел большую сухую палку ')
    hod2 = input('''Что ты будешь с  ней делать?
1.[подожгу]
2.[выброшу]
    ---''')
    if hod2 == '1':
        print("аххахаахах, а чем ты будешь поджигать.....")
        hod3 = input('''Хорошо , ты решил заглянуть себе в карман 
и нашел зажигалку.......будь внимательнее
-----------------------------------------
Светом от "факела" ты осветил себе путь
и вдруг увидел мужика , идущего на тебя

Что ты будешь делать в данной ситуации?

1.[пойду на встречу]
2.[побегу в другую сторону]
3.[останусь на месте]

--- ''')
        if hod3 == '1':
            print('Этим мужиком оказался обычний лесничий и он пригласил тебя к себе в хибару')
            hod4 = input('''Лесничий предложил тебе выпить 
1.[пить]
2.[отказаться]

--- ''')
            if hod4 == '1':
                print('Лесничий рассказывает душещипательную историю как давным давно потерял своего сына')
                hod5 = input('''1.[пойти на поиски]
2.[пить дальше]

--- ''')
                if hod5 == '1':
                    print('Первым делом ты решил опросить людей в близь лежащей деревене')
                    print('что они об этом знают')
                    hod6 = input('''ы подошел к старой, сморщенной , противной старухе 
Она остановила тебя и сказала, что где-то уже видела тебя

1.[поговорить с ней]
2.[пройти мимо]

--- ''')
                    if hod6 == '1':
                        print('Поговорив с этой старухой , вы узнали, что она')
                        print('узнает людей по походке, и у неё появилось такое ощущение')
                        print('что она уже знала челоека с такой походкой')
                        hod7 = input('''Старуха спросила сколько тебе лет

1.[15]
2.[17]
3.[19]
4.[21]

---- ''')
                        if hod7 == '4':
                            print('О боже, а тебя случайно зовут не',name+'?')
                            print('''Старуха рассказывает вам , что вспомнила ,что видела такую походку
У сына Лесника и его как раз звали''',name,'''и он пропал 12 лет назад

-------------------------

Вы в шоке идете к Леснику и вы рассказываете ему что вы узнали. С заплаканными глазами он вас обнимает и говорит, что он знал что вы его сын , но он не мог вспомнить его имя и ему было очень стыдно.....

КОНЕЦ, спасибо что прошли квест , вы вышли на лучшую концовку!''')
                        elif hod7 == '1'  or hod7 == '2' or hod7 == '3':
                            print("Старуха говорит, что обозналась")
                            print('Вы решили пойти дальше, но вдруг наткунились на шпану')
                            print('Она предложила вам сыграть в игру "кто ближе" ')
                            print('Три человека называют 2 рандомных числа')
                            print('какое из них ближе к выпавшему в стакане, тот победил')
                            print('Если вы выигрваете ,то можете уйти от сюда живым')
                            hod8 = random.randint(0, 100)
                            per1 = random.randint(0, 100)
                            me = int(input('Введи число от 0 до 100 - '))
                            win1 = hod8 - me
                            win2 = hod8 - per1
                            if win1 < win2  :
                                print('---------------------------')
                                print('Ты выиграл , поздравляю!')
                                print('Вы пошли дальше ,сломали ногу  и в итоге она сгинла, и вам ее отрезали')
                                print('теперь вы инвалид ')
                                print('---------------------------')
                                print('Конец квеста - вы вышли на не очень хорошую концовку')
                            elif win1 > win2  :
                                print('---------------------------')
                                print('Ты проиграл.....')
                                print('Вас убили и бросили в ближайшую канаву')
                                print('---------------------------')
                                print('Конец квеста - вы вышли на не очень хорошую концовку')
                    elif hod6 == '2':
                        print('Вы решили пойти дальше, но вдруг наткунились на шпану')
                        print('Она предложила вам сыграть в игру "кто ближе" ')
                        print('Три человека называют 2 рандомных числа')
                        print('какое из них ближе к выпавшему в стакане, тот победил')
                        print('Если вы выигрваете ,то можете уйти от сюда живым')
                        hod8 = random.randint(0, 100)
                        per1 = random.randint(0, 100)
                        print('---------------------------')
                        me = int(input('Введи число от 0 до 100 - '))
                        win1 = hod8 - me
                        win2 = hod8 - per1
                        if win1 < win2:
                            print('---------------------------')
                            print('Ты выиграл , поздравляю!')
                            print('Вы пошли дальше ,сломали ногу  и в итоге она сгинла, и вам ее отрезали')
                            print('теперь вы инвалид ')
                            print('---------------------------')
                            print('Конец квеста - вы вышли на не очень хорошую концовку')
                        elif win1 > win2:
                            print('---------------------------')
                            print('Ты проиграл.....')
                            print('Вас убили и бросили в ближайшую канаву')
                            print('---------------------------')
                            print('Конец квеста - вы вышли на не очень хорошую концовку')
                elif hod5 == '2':
                    print('Вы очень много пили и решили пойти на улицу, и уснули там')
                    pogoda = int(input("""Сколько градусов по цельсию было сегодня ночью?

Введи сколько было градусов от 0 до 100

или пусть решит рандомайзер

1.[использовать рандомайзер]

--- """))
                    if 1<pogoda<5:



