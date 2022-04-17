#Является ли слово палиндромом

def is_palindrome(string):
    return string == ''.join(reversed(string))
print(is_palindrome('алала'))

#Тест на Мамонта

answer = 0
play = True
while play:
    if input("Пройти тест на Мамонта?\n").lower() == "да":
        if input("Ты волосатый(ая)?\n").lower() == "да":
            answer = 1
        else:
            answer = 0
        if answer == 1:
            print("Ты мамонт")
        else:
            print("Ты не мамонт")
    play = False