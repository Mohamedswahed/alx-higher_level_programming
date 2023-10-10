#!/usr/bin/python3
def no_c(my_string):

    j = ""

    new_string = my_string[:]

    for i in range(len(my_string)):
        if (my_string[i] != 'c' and my_string[i] != 'C'):
            j += my_string[i]

    return (j)
