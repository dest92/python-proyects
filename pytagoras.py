from cmath import exp
import math
from multiprocessing.sharedctypes import Value
from tokenize import Name

try:
    input = raw_input
except NameError:
    pass


def get_numbers(number):
    
    
    while True:
        values = input(number)
        if not values:
            return None
        try:
            values = int(values)
        except ValueError:
            print("Solo valores numéricos")
        else:
            break
        
    return values
    
def triangle(a = None, b = None, h= None):
    print("Introduzca los valores, dejando en blanco los desconocidos")
    
    a= get_numbers("a: ")
    b= get_numbers("b: ")
    
    


    