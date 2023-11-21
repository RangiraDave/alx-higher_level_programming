#!/usr/bin/python3

def list_division(my_list1, my_list2, list_length):
    new_list = [0] * list_length
    try:
        for i in range(list_length):
            if (isinstance(my_list1[i], (int, float)) and
                    isinstance(my_list2[i], (int, float))):
                if my_list2[i] == 0:
                    print("division by 0")
                else:
                    new_list[i] = my_list1[i] / my_list2[i]
            else:
                print("wrong type")
    except IndexError:
        print("out of range")
    finally:
        return new_list
