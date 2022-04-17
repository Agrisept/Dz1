#1
MyName = "Ксюха"
print(MyName)

#2
MyAge = int(16)
print("В свои", MyAge, "мне ещё жить и жить.")

#3
Concatenation = (MyName + " " + MyName + " " + MyName + " " + MyName + " " + MyName)
Iteration = (MyName + " ") * 5
print(Concatenation)
print(Iteration)

#4
UserName = str(input("Здравствуй! Напиши, пожалуйста, своё имя. "))
UserAge = int(input("Будь хорошим человеком, напиши свой возраст :). "))
print("Приятно познакомиться,", UserName, "!")
print("Ого! Тебе", UserAge, "лет. Поздравляшки! Ты ведь не хочешь останавливаться? ^^'")

#5
UserAge = int(input("Немедленно пиши свой возраст! "))
print("Отлично... Так... Подожди-ка... Ооох... Охохохо... Ну и дела... По моим скромным данным ты - ")
if UserAge <= 0 or UserAge > 150:
    print("Врун-пердун. Давай по-серьёзному, от этого зависит моя репутация >:с !!")
elif UserAge > 0 and UserAge <= 13:
    print("Шкет. Где твои родители??? Чт... Ты ещё и с грязными руками? ОХРАНААА!!!")
elif UserAge > 13 and UserAge <= 17:
    print("Человек. Поздравляю, ты в том возрасте, когда тебя уже можно причислить к людям.")
elif UserAge > 17 and UserAge <= 60:
    print("Пардон. Вы* -\nЯвляетесь основной рабочей силой. Ничего особенного. Спасибо что трудитесь на благо нашей цивилизации.\n")
elif UserAge > 60 and UserAge <= 150:
    print("Пардон. Вы* -\nСтарче. Почтенный возраст, не забудьте вытряхнуть песок из клавиатуры.\n")
else:
    print("КАкАя-т0 0Ши6кА")

#6
print(MyName[::-1], MyName[1:], MyName[-3:], MyName[:5]) # 1 - с конца, 2 - со второго, 3 - три последних, 4 - первых пять

#7
NameLength = len(UserName)
print(NameLength, "- длина вашего имени.")
AgeLength = len(str(UserAge))
# Я тут не догнала. Потом спрошу у кого-нидь

#8
