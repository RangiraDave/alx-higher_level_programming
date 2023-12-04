#!/usr/bin/python3
"""Definition of MyList class that inherits list"""


class MyList(list):
    """MyList's constructor"""
    def __init__(self):
        list.__init__(self)

    def print_sorted(self):
        """Function to print sorted list"""

        print("{}".format(sorted(self)))
