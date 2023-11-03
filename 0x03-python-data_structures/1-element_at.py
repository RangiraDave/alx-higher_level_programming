#!/usr/bin/python3

#if __name__ == '__main__':
def element_at(my_list, idx):
    if idx > len(my_list) - 1:
        return 'None'
    if idx < 0:
        return 'None'
    return my_list[idx]
