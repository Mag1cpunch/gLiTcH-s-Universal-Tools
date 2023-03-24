import sys
import random
import string
##Основное
def main():
    print("--------------------------------")
    print("--------Core Initialized--------")
    print("--------------------------------")
main()
##Калькулятор
def calculator():
    a = input("Enter First Num:")
    b = input("Enter Second Num:")
    x = int(a) * int(b)
    print(a, "*", b, "=", x)
##Перезагрузка
def reload():
    main()
    switch()
##Выход
def exit_program():
    print("Exiting program...")
    sys.exit()
##Случайное Число
def randomnum():
    random_number = random.randint(1, 100)
    t = input("Do You Want To Randomize Numbers Between 1 And 100? y/n:")
    if t == ("y"):
        print(random_number)
        switch()

    if t == ("n"):
        switch()
##Получение Случайного Пароля
def randompass(length):
        password_characters = string.ascii_letters + string.digits
        password = ''.join(random.choice(password_characters) for i in range(length))
        return password
##Вывод Случайного Пароль В Консоль
def randompass2():
    password = randompass(16)
    j = input("Do You Want To Generate Password(Range is 16)? y/n: ")
    if j == ("y"):
        print(password)
        switch()

    if j == ("n"):
        print("Password Generation Cancelled")
        switch()
    switch()
##Комманды
def switch():
    s = "List Of Available Commands:\ncalculator\nrandomnum\nrandompass\nreload\nexit"
    e = input("Enter Command(Write help To See All Available Commands):")
    if e == "help":
        print(s)
        switch()
    
    if e == "calculator":
        calculator()

    if e == "randomnum":
        randomnum()

    if e == "genpass":
        randompass2()

    if e == "reload":
        reload()

    if e == "exit":
        exit_program()

switch()
