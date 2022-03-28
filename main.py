import sys


def run_function():
    str_list = []

    x = str(input('Введите строку: '))
    str_list.append(x)
    print(str_list)

    print('---------------------------------------')

    my_list = []
    for num in range(1):
        user_input = str(input('Введите число и индекс with comma: '))
        input_arr = user_input.split(',')
        number_str = input_arr[0]
        index_str = input_arr[1]

        print(number_str)
        print(index_str)

        mylist = [11, 34, 15, 78, 56, 90]
        item = 78
        index = mylist.index(item)
        mylist.remove(34)

        print("The index of", item, "in the list is:", index)
        print(mylist)

        counter = 0
        str(input('Введите число: '))
        if counter == [11, 34, 15, 78, 56, 90]:
            print(True)
        else:
            print('Error')


#################### don't touch #############
run_function()
