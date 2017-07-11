# solutions.py
"""Volume IB: Testing.
<Name>
<Date>
"""
import math
from numpy import random as rd
import numpy as np
import os.path

# Problem 1 Write unit tests for addition().
# Be sure to install pytest-cov in order to see your code coverage change.


def addition(a, b):
    return a + b


def smallest_factor(n):
    """Finds the smallest prime factor of a number.
    Assume n is a positive integer.
    """
    if n == 1:
        return 1
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return i
    return n


# Problem 2 Write unit tests for operator().
def operator(a, b, oper):
    if type(oper) != str:
        raise ValueError("Oper should be a string")
    if len(oper) != 1:
        raise ValueError("Oper should be one character")
    if oper == "+":
        return a + b
    if oper == "/":
        if b == 0:
            raise ValueError("You can't divide by zero!")
        return a/float(b)
    if oper == "-":
        return a-b
    if oper == "*":
        return a*b
    else:
        raise ValueError("Oper can only be: '+', '/', '-', or '*'")

# Problem 3 Write unit test for this class.
class ComplexNumber(object):
    def __init__(self, real=0, imag=0):
        self.real = real
        self.imag = imag

    def conjugate(self):
        return ComplexNumber(self.real, -self.imag)

    def norm(self):
        return math.sqrt(self.real**2 + self.imag**2)

    def __add__(self, other):
        real = self.real + other.real
        imag = self.imag + other.imag
        return ComplexNumber(real, imag)

    def __sub__(self, other):
        real = self.real - other.real
        imag = self.imag - other.imag
        return ComplexNumber(real, imag)

    def __mul__(self, other):
        real = self.real*other.real - self.imag*other.imag
        imag = self.imag*other.real + other.imag*self.real
        return ComplexNumber(real, imag)

    def __truediv__(self, other):
        if other.real == 0 and other.imag == 0:
            raise ValueError("Cannot divide by zero")
        bottom = (other.conjugate()*other*1.).real
        top = self*other.conjugate()
        return ComplexNumber(top.real / bottom, top.imag / bottom)

    def __eq__(self, other):
        return self.imag == other.imag and self.real == other.real

    def __str__(self):
        return "{}{}{}i".format(self.real, '+' if self.imag >= 0 else '-',
                                                                abs(self.imag))

# Problem 5: Write code for the Set game here
"""
class Setgenerator(object):
    def __init__(self,m,h):
        self.g_set = self.cardgen(m)
        self.h_set = self.handgen(self.g_set,h)
        self.m = m
        self.h = h

    def cardgen(self,m):
        poss_list = range(0,m)
        g_set = []
        for i in poss_list:
            for j in poss_list:
                for k in poss_list:
                    for l in poss_list:
                        g_set.append([i,j,k,l])
        return g_set

    def handgen(self,g_set,h):
        i_set = [i for i in range(0,len(g_set))]
        hand_index = rd.choice(i_set,h)
        h_set = [g_set[i] for i in hand_index]
        return h_set

    def setexport(self,e_file):
        prep_set = self.h_set
        i_set = 'B'
        for i in range(len(prep_set)):
            for j in range(len(prep_set[i])):
                i_set = i_set + str(prep_set[i][j])
        print(i_set)
        text_file = open(e_file, "w")
        text_file.write(str(i_set))
        text_file.close()
        return "Hand Exported"
"""
import itertools

class Checker(object):
    def setimport(self,h,i_file):
        g_input = i_file[3:-1]
        f_output = []
        for i in range(0,h*4,4):
            k = [int(g_input[i]),int(g_input[i+1]),int(g_input[i+2]),int(g_input[i+3])]
            f_output.append(k)
        return f_output

    def matchpicker(self,h,input_file):
        if os.path.isfile(input_file) != True:
            raise NameError("Not a valid file")
        input_file = np.loadtxt(input_file, dtype=str)
        input_file = str(input_file)
        if len(input_file) != 52:
            raise ValueError("Not a valid card sorting")
        init_input = self.setimport(h,input_file)
        rg = range(0, len(init_input))
        for i in rg:
            for j in rg:
                if init_input[i] == init_input[j] and i !=j:
                    raise ValueError("Error: Duplicate Card Present")
        match_set = []
        index_set = list(set(itertools.combinations(rg, 3)))
        for i in range(len(index_set)):
            part_set = [init_input[x] for x in index_set[i]]
            s_case = np.sum(part_set,axis=0)
            if s_case[0] % 3 == 0 or s_case[1] % 3 == 0 or s_case[2] % 3 == 0 or s_case[3] % 3 == 0:
                match_set.append(s_case)
        if match_set == []:
            raise ValueError("There are no matches")
        return len(match_set)




Setg = Checker()
print(Setg.matchpicker(12,"set.txt"))
