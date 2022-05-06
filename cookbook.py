from thefuzz import process # Will implement later
import re
import json
import os
import sys
import _toolkit as ctk # My personal toolkit - This contains a few helper functions that I reuse regularly

# --- CLASSES BLOCK

# -- Cupboard Classes

class cupboard:

    def __init__(self) -> None:
        self.cupboardItems = {}

    def __repr__(self) -> str:
        return 'Available Cupboard Items:\n' + str(list(self.cupboardItems.keys()))

class cupboardItem:

    def __init__(self, name, measuredIn, amountInCupboard) -> None:
        self.name = name
        self.measuredIn = measuredIn
        self.amountInCupboard = amountInCupboard

# -- Recipe Classes

class recipeBook:

    def __init__(self) -> None:
        self.recipes = {}

    def __repr__(self) -> str:
        return 'Available Recipes:\n' + str(list(self.recipes.keys()))

class recipe:

    class ingredient:

        def __init__(self, nameOfIngredient, amountNeeded) -> None:
            self.nameOfIngredient = nameOfIngredient
            self.amountNeeded = amountNeeded

            # When using recipe for shopping order:
            # CHECK TO SEE IF INGREDIENT IS IN THE CUPBOARD HERE (WITH FUZZY MATCHING)
            # REMOVE THE AMOUNT NEEDED FROM THE CUPBOARD IF PRESENT
            # ADD IT TO THE SHOPPING LIST IF NOT, OR IF LESS EXISTS THAN IS REQUIRED

    def __init__(self, name) -> None:
        self.name = name
        self.ingredients = []
        self.cookingTools = []
        self.steps = []
        self.cookingTime = 0
        self.price = 0

    def addIngredients(self):

        def addIngredientsQuestionLoop(self):

            ctk.pageBreak()

            moreIngredientsResponse = str(input('\n\nWould you like to add any more ingredients to this recipe? (y/n)')).lower().strip()
            if moreIngredientsResponse == 'y':
                return moreIngredientsResponse
            elif moreIngredientsResponse != 'n':
                print('I\'m, sorry, I didn\'t understand your input...')
                addIngredientsQuestionLoop()

        ctk.clearConsole()
        ctk.pagebreak()

        nameOfIngredientToAdd = input('Name of the ingredient to add: ') # WILL NEED TO VERIFY THAT THIS EXISTS IN THE CUPBOARD & ADD IT IF NOT
        amountOfIngredientNeeded = input('Amount needed: ') # WILL NEED TO VERIFY THAT THIS IS A NUMBER
        ingredientToAdd = self.ingredient(str(nameOfIngredientToAdd), int(amountOfIngredientNeeded))
        self.ingredients.append(ingredientToAdd)

        ctk.clearConsole()
        ctk.pageBreak()

        print('Currently editing recipe: ' + self.name + 'Currently added ingredients:\n' + str([ingredientListed.nameOfIngredient for ingredientListed in self.ingredients]))

        moreIngredientsResponse = addIngredientsQuestionLoop()
        if moreIngredientsResponse == 'y':
            self.addIngredients()

    # Will have to flesh this bit out later & likely change where it lives in the code
    # def calculatePriceOfIngredients(self):
    #     self.price = sum([ingredient['price'] for ingredient in self.ingredients])

    def addCookingTools(self):
        pass

    def addStep(self):
        pass

# --- RUN BLOCK

if __name__ == '__main__':

    ctk.clearConsole()
    ctk.pageBreak()
    ctk.declareScriptEnd()
    ctk.pageBreak()
