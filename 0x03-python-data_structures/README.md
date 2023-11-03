This folder contains answers for the following python tasks:

0. Write a function that prints all integers of a list.

    Prototype: def print_list_integer(my_list=[]):
    Format: one integer per line. See example
    You are not allowed to import any module
    You can assume that the list only contains integers
    You are not allowed to cast integers into strings
    You have to use str.format() to print integers



1. Write a function that retrieves an element from a list like in C.

    Prototype: def element_at(my_list, idx):
    If idx is negative, the function should return None
    If idx is out of range (> of number of element in my_list), the function should return None
    You are not allowed to import any module
    You are not allowed to use try/except



2. Write a function that replaces an element of a list at a specific position (like in C).

    Prototype: def replace_in_list(my_list, idx, element):
    If idx is negative, the function should not modify anything, and returns the original list
    If idx is out of range (> of number of element in my_list), the function should not modify anything, and returns the original list
    You are not allowed to import any module
    You are not allowed to use try/except


3. Write a function that prints all integers of a list, in reverse order.

    Prototype: def print_reversed_list_integer(my_list=[]):
    Format: one integer per line. See example
    You are not allowed to import any module
    You can assume that the list only contains integers
    You are not allowed to cast integers into strings
    You have to use str.format() to print integers



4. Write a function that replaces an element in a list at a specific position without modifying the original list (like in C).

    Prototype: def new_in_list(my_list, idx, element):
    If idx is negative, the function should return a copy of the original list
    If idx is out of range (> of number of element in my_list), the function should return a copy of the original list
    You are not allowed to import any module
    You are not allowed to use try/except



5. Write a function that removes all characters c and C from a string.

    Prototype: def no_c(my_string):
    The function should return the new string
    You are not allowed to import any module
    You are not allowed to use str.replace()



6. Write a function that prints a matrix of integers.

    Prototype: def print_matrix_integer(matrix=[[]]):
    Format: see example
    You are not allowed to import any module
    You can assume that the list only contains integers
    You are not allowed to cast integers into strings
    You have to use str.format() to print integers



7. Write a function that adds 2 tuples.

    Prototype: def add_tuple(tuple_a=(), tuple_b=()):
    Returns a tuple with 2 integers:
        The first element should be the addition of the first element of each argument
        The second element should be the addition of the second element of each argument
    You are not allowed to import any module
    You can assume that the two tuples will only contain integers
    If a tuple is smaller than 2, use the value 0 for each missing integer
    If a tuple is bigger than 2, use only the first 2 integers



8. Write a function that returns a tuple with the length of a string and its first character.

    Prototype: def multiple_returns(sentence):
    If the sentence is empty, the first character should be equal to None
    You are not allowed to import any module



9. Write a function that finds the biggest integer of a list.

    Prototype: def max_integer(my_list=[]):
    If the list is empty, return None
    You can assume that the list only contains integers
    You are not allowed to import any module
    You are not allowed to use the builtin max()



10. Write a function that finds all multiples of 2 in a list.

    Prototype: def divisible_by_2(my_list=[]):
    Return a new list with True or False, depending on whether the integer at the same position in the original list is a multiple of 2
    The new list should have the same size as the original list
    You are not allowed to import any module



11. Write a function that deletes the item at a specific position in a list.

    Prototype: def delete_at(my_list=[], idx=0):
    If idx is negative or out of range, nothing change (returns the same list)
    You are not allowed to use pop()
    You are not allowed to import any module



12. Complete the source code in order to switch value of a and b

    You can find the source code here
    Your code should be inserted where the comment is (line 4)
    Your program should be exactly 5 lines long



13. Technical interview preparation:

    You are not allowed to google anything
    Whiteboard first

Write a function in C that checks if a singly linked list is a palindrome.

    Prototype: int is_palindrome(listint_t **head);
    Return: 0 if it is not a palindrome, 1 if it is a palindrome
    An empty list is considered a palindrome



100. 
Create a C function that prints some basic info about Python lists.

    Prototype: void print_python_list_info(PyObject *p);
    Format: see example
    Python version: 3.4
    Your shared library will be compiled with this command line: gcc -Wall -Werror -Wextra -pedantic -std=c99 -shared -Wl,-soname,PyList -o libPyList.so -fPIC -I/usr/include/python3.4 100-print_python_list_info.c
    OS: Ubuntu 14.04 LTS
    Start by reading:
        listobject.h
        object.h
        Common Object Structures
        List Objects

julien@ubuntu:~/CPython$ gcc -Wall -Werror -Wextra -pedantic -std=c99 -shared -Wl,-soname,PyList -o libPyList.so -fPIC -I/usr/include/python3.4 100-print_python_list_info.c
julien@ubuntu:~/CPython$ cat 100-test_lists.py 
import ctypes

lib = ctypes.CDLL('./libPyList.so')
lib.print_python_list_info.argtypes = [ctypes.py_object]
l = ['hello', 'World']
lib.print_python_list_info(l)
del l[1]
lib.print_python_list_info(l)
l = l + [4, 5, 6.0, (9, 8), [9, 8, 1024], "My string"]
lib.print_python_list_info(l)
l = []
lib.print_python_list_info(l)
l.append(0)
lib.print_python_list_info(l)
l.append(1)
l.append(2)
l.append(3)
l.append(4)
lib.print_python_list_info(l)
l.pop()
lib.print_python_list_info(l)
julien@ubuntu:~/CPython$ python3 100-test_lists.py 
[*] Size of the Python List = 2
[*] Allocated = 2
Element 0: str
Element 1: str
[*] Size of the Python List = 1
[*] Allocated = 2
Element 0: str
[*] Size of the Python List = 7
[*] Allocated = 7
Element 0: str
Element 1: int
Element 2: int
Element 3: float
Element 4: tuple
Element 5: list
Element 6: str
[*] Size of the Python List = 0
[*] Allocated = 0
[*] Size of the Python List = 1
[*] Allocated = 4
Element 0: int
[*] Size of the Python List = 5
[*] Allocated = 8
Element 0: int
Element 1: int
Element 2: int
Element 3: int
Element 4: int
[*] Size of the Python List = 4
[*] Allocated = 8
Element 0: int
Element 1: int
Element 2: int
Element 3: int
julien@CPython:~/CPython$

#Happy coding#