"""
Dit programma berekent de vergelijking voor de raaklijn van de grafiek met de vorm: y=ax^n + bx
Gemaakt door Nathan Tromp
"""
# imports
import math


# Module voor formule
def display():
    txt = "De vergelijking is: f(x) = {} x^{} + {}x"
    print(txt.format(a, n, b, ))
    print("\n")


# Module voor de afgeleide
def afgeleide():
    A = (a * n)
    N = (n - 1)
    txt1 = "De vergelijking is: f'(x) = {} x^{} + {} "
    print(txt1.format(A, N, b))
    print("\n")


# Module voor de raaklijn
def raaklijn():
    c =
    print("Formule van de raaklijn is y = cx + d ")
    print("\n")


# start screen
print("Hallo, bedankt voor het openen van dit programma :)")
print("\n")
print("Dit programma berekent de vergelijking voor ")
print("de raaklijn van de grafiek met de vorm: y = ax^n + bx.")


# Inputs
a = int(input("Voer een getal voor a in:"))
print("Getal voor a: ", a)
n = int(input("Voer een getal voor n in:"))
print("Getal voor n: ", n)
b = int(input("Voer een getal voor b in:"))
print("Getal voor b: ", b)
x = int(input("Voer een getal in voor x:"))
print("Getal voor x: ", x)


# initialiseer modules
display()
afgeleide()
