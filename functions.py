import random
import os

def _get_random_string(min_lenght: int, max_lenght: int):
    string = ""
    if min_lenght > max_lenght:
        print("MAX_LENGHT_IS_LOWER_THAN_THE_MIN_LENGHT")
        return 0
    cycles = random.randint(min_lenght, max_lenght)
    i = 0
    while i < cycles:
        p = ""
        t = random.randint(1, 26)
        match t:
            case 1:
                p = "a"
            case 2:
                p = "b"
            case 3:
                p = "c"
            case 4:
                p = "d"
            case 5:
                p = "e"
            case 6:
                p = "f"
            case 7:
                p = "g"
            case 8:
                p = "h"
            case 9:
                p = "i"
            case 10:
                p = "j"
            case 11:
                p = "k"
            case 12:
                p = "l"
            case 13:
                p = "m"
            case 14:
                p = "n"
            case 15:
                p = "o"
            case 16:
                p = "p"
            case 17:
                p = "q"
            case 18:
                p = "r"
            case 19:
                p = "s"
            case 20:
                p = "t"
            case 21:
                p = "u"
            case 22:
                p = "v"
            case 23:
                p = "w"
            case 24:
                p = "x"
            case 25:
                p = "y"
            case 26:
                p = "z"
        i += 1
        if random.randint(0, 1) == 1:
            p = p.upper()
        string += p
    return string