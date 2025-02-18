import random

drum_sections = int(input("Введите количество секций в барабане  (4/6/8):\n"))
if drum_sections == 4:
    drum4 = (random.choice([1,2,3,4]))
    kill = int(input("Введите номер боевого патрона: "))
    if drum4 == kill:
        print("Патрон боевой!\nИгра окончена!")
    else:
        print(f"Боевым патроном оказался {drum4}!\nИгра продолжается!")
        while not drum4 == kill:
            kill = int(input("Введите номер боевого патрона:"))
            drum4 = (random.choice([1,2,3,4]))
            if drum4 == kill:
                print("Патрон боевой!\nИгра окончена!")
            else:
                print(f"Боевым патроном оказался {drum4}!\nИгра продолжается!")

elif drum_sections == 6:
    drum6 = (random.choice([1, 2, 3, 4, 5, 6]))
    kill = int(input("Введите номер боевого патрона: "))
    if drum6 == kill:
        print("Патрон боевой!\nИгра окончена!")
    else:
        print(f"Боевым патроном оказался {drum6}!\nИгра продолжается!")
        while not drum6 == kill:
            kill = int(input("Введите номер боевого патрона:"))
            drum6 = (random.choice([1, 2, 3, 4, 5, 6]))
            if drum6 == kill:
                print("Патрон боевой!\nИгра окончена!")
            else:
                print(f"Боевым патроном оказался {drum6}!\nИгра продолжается!")

elif drum_sections == 8:
    drum8 = (random.choice([1, 2, 3, 4, 5, 6, 7, 8]))
    kill = int(input("Введите номер боевого патрона: "))
    if drum8 == kill:
        print("Патрон боевой!\nИгра окончена!")
    else:
        print(f"Боевым патроном оказался {drum8}!\nИгра продолжается!")
        while not drum8 == kill:
            kill = int(input("Введите номер боевого патрона:"))
            drum8 = (random.choice([1, 2, 3, 4, 5, 6, 7, 8]))
            if drum8 == kill:
                print("Патрон боевой!\nИгра окончена!")
            else:
                print(f"Боевым патроном оказался {drum8}!\nИгра продолжается!")




