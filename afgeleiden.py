"""
lmao
"""
# imports
import math


# what nibbas see on the screen
def screen():
    print("\n")
    print("Dit programma berekent de vergelijking van ")
    print("de raaklijn van de grafiek met de vorm: y = ax^n + bx.")
    print("\n")

# Module for formule


def display():
    txt = "De vergelijking is: f(x) = {} x^{} + {}x"
    print(txt.format(a, n, b, ))
    print("\n")


# Module derivative
def afgeleide():
    global A, N, c
    A = (a * n)
    N = (n - 1)
    c = pow(x, N)
    c *= A
    c += b


# Module raaklijn
def raaklijn():
    d = y - c1
    if d < 0:
        d *= -1
        txt4 = "De vergelijking van de raaklijn is y = {}x - {} "
        print(txt4.format(c, d))
        print("\n")
    else:
        txt5 = "De vergelijking van de raaklijn is y = {}x + {} "
        print(txt5.format(c, d))
        print("\n")



def msg():
    global y, c1
    y = pow(x, n)
    y *= a
    y += (b * x)
    c1 = c
    c1 *= x
    txt3 = "Het raakpunt is ({}, {})"
    print(txt3.format(x, y))
    print("\n")


def helling():
    txt3 = "De helling op x = {} is {}"
    print(txt3.format(x, c))
    print("\n")

while True:
    # main code
    screen()
    a = int(input("Voer in a: "))
    print("Getal voor a: ", a)
    n = int(input("Voer in n: "))
    print("Getal voor n: ", n)
    b = int(input("Voer in b: "))
    print("Getal voor b: ", b)
    x = int(input("Voer in x: "))
    print("Getal voor x: ", x)
    print("\n")
# rest of modules
    display()
    afgeleide()
    msg()
    helling()
    raaklijn()
    