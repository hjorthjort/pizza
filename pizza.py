from operator import itemgetter
from pizzalist import pizzas
import os
import random


correctPoints = 10
needsPoints = -2
extraIngPoints = -8

class Pizza:
    def __init__(self, name):
        self.name = name

    def set_ingredients(self, ingredients):
        self.ingredients = ingredients

    def get_ingredients(self):
        if hasattr(self,"ingredients"):
            return self.ingredients
        else:
            return None

    def set_closest(self, closest):
        self.closest = closest

    def get_closest(self):
        return self.closest

class PizzaModifier(Pizza):
    def set_added(self, added):
        self.added = added

    def get_added(self):
        if hasattr(self,"added"):
            return self.added
        else:
            return None

    def set_removed(self, removed):
        self.removed = removed

    def get_removed(self):
        if hasattr(self,"removed"):
            return self.removed
        else:
            return None


# Picks an element at random from 'possibilities' and add it to 'picked'. Keep 
# trying to pick until an item that isn't already in picked appears, thereby
# eliminating duplicates
def pickFrom(possibilities, picked):
    select = random.randint(0, len(possibilities) -1)
    while possibilities[select] in picked:
        select = random.randint(0, len(possibilities) -1)
    picked.append(possibilities[select])

# Returns a list of items by opening the given file (filename given relative to 
# directory of script) and reading items, splitting by lines
def readFile(filename):
    dirname = os.path.dirname(os.path.realpath(__file__))
    filename = dirname + filename
    with open(filename, encoding="utf-8") as f:
        ret = f.read().splitlines()
    return ret

# Randomize an awesome name
def random_name():
    names = readFile("/cities")
    return names[random.randint(0, len(names)-1)]

# Create a random pizza with specified number of ingredients, and optional arguments
def random_pizza(args=[], min_ingred=2, max_ingred=6):
    ret = Pizza(random_name())

    # Load all basic ingredients
    ingredients = readFile("/vegetarian")

    # If specified on arguments, load meat as well
    if "meat" in args :
        ingredients = ingredients + readFile("/meat")

    # The list to return
    roulette_result = []

    # The number of ingredients we will add
    roulette_tries = random.randint(min_ingred,max_ingred)

    # The number of sauces to put on the pizza
    sauces_nbr = random.randint(0,2)

    # Add as many ingredients as roulette_tries specified
    for i in range(0, roulette_tries):
        pickFrom(ingredients, roulette_result)

    # Add as many sauces as sauces_nbr specified
    sauces = readFile("/sauce")
    for i in range(0, sauces_nbr):
        pickFrom(sauces, roulette_result)

    ret.set_ingredients(roulette_result)

    ret.set_closest(findClosestPizza(ret))

    return ret

def findClosestPizza(inPizza):
    listPizza = inPizza.get_ingredients()
    pizzaIngredients = set(listPizza)
    lenPizza = len(pizzaIngredients)
    resultQuad = []
    correctIngr = {}
    extraIngr = {}
    stillMissing = {}
    for k in pizzas:
        ingr = set(pizzas.get(k))
        correctIngr = pizzaIngredients.intersection(ingr)
        stillMissing = pizzaIngredients.difference(ingr)
        extraIngr = ingr.difference(pizzaIngredients)
        resultQuad.append((len(correctIngr)*correctPoints+len(extraIngr)*extraIngPoints+len(stillMissing)*needsPoints, k, ingr, extraIngr, stillMissing))
    resultQuad.sort(reverse=True)
    if resultQuad[0][0] > 0 :
        # ret = {'pizza_name':resultQuad[0][1]}
        ret = PizzaModifier(resultQuad[0][1])
        if len(resultQuad[0][2]) != 0 :
            ret.set_ingredients(list(resultQuad[0][2]))
        if len(resultQuad[0][3]) != 0 :
            ret.set_removed(list(resultQuad[0][3]))
        if len(resultQuad[0][4]) != 0 :
            ret.set_added(list(resultQuad[0][4]))
    else :
        #ret = {'Margharita':str(pizzaIngredients)}
        ret = PizzaModifier("Margharita")
        ret.set_added(listPizza)
    return ret
