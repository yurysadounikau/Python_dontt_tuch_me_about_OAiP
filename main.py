list_length = int(input("Введите длину списка: "))
i = 0
number_list = []
print("Введите данные в список: ")
while i < list_length:
    number_list.append(int(input()))
    i+=1



print("Ваш список: ", number_list)
work = True
while work:
    print("1) Вставить число в список: ", end="\n")
    print("2) Удалить число из списка: ", end="\n")
    print("3) Отсортировать список: ", end="\n")
    choice = int(input("Ваш выбор: "))
    print("Ваш список: ", number_list)

    if choice == 1:
       number_1 = int(input("Введите число для вставки в список: "))
       number_position_1 = int(input("Введите порядок элемента для вставки: "))
       number_list.insert(number_position_1, number_1)
       print("Ваш список теперь: ", number_list)
       print("Хотите выйти из программы?")
       print("1) Да. ")
       print("2) Нет.")
       exit_choice_1 = int(input())
       if exit_choice_1 == 1:
           print("Вы вышли из программы. ")
           work = False

    if choice == 2:
       index_delete_2 = int(input("Введите число для удаления из списка: "))
       number_list.remove(index_delete_2)
       print("Ваш список теперь: ", number_list)
       print("Хотите выйти из программы?")
       print("1) Да. ")
       print("2) Нет.")
       exit_choice_1 = int(input())
       if exit_choice_1 == 1:
           print("Вы вышли из программы. ")
           work = False


    if choice == 3:
        number_list.sort()
        print("Ваш список теперь", number_list)
        print("Хотите выйти из программы?")
        print("1) Да. ")
        print("2) Нет.")
        exit_choice_1 = int(input())
        if exit_choice_1 == 1:
            print("Вы вышли из программы. ")
            work = False
