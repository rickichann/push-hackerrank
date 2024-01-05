
import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input().strip())
    
    def check_constraint(n):
        if n >= 1 and n <= 100:
            return True
        else:
            return False
    
    if check_constraint(n) == True:
        if n % 2 == 0 and n in [x for x in range(2,6)]:
            print('Not Weird')
        elif n % 2 == 0 and n in [x for x in range(6,21)]:
            print('Weird')
        elif n % 2 == 0 and n > 20 :
            print('Not Weird')
        else:
            print('Weird')
        
