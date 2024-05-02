from thefuzz import process # Will implement later
import re
import json
import os
import sys
from time import sleep
import pprint
# - I SHOULD SEE IF I CAN FIND A KITCHEN MEASUREMENTS CONVERSION TABLE

# --- CLASSES BLOCK

#class KitchenCupboard: # - I NEED TO ADD INGREDIENTS AND TOOLS HERE FOR EASY ACCESS LATER # - CURRENTLY IRRELEVANT, TO BE WORKED IN LATER
#
#    def __init__(self) -> None:
#        pass

prettyPrintDict = pprint.PrettyPrinter(indent=4)

class RecipeBook:

    class __RecipeEncoder(json.JSONEncoder):
        def default(self, recipeObject):
            return recipeObject.__dict__

    def __init__(self):
        self.recipes = {}

    def addRecipe(self):

        nameOfNewRecipe = input('What is the name of this recipe?:\n')
        newRecipe = Recipe(nameOfNewRecipe)
        newRecipe.addCookingTools()
        newRecipe.addIngredients()
        newRecipe.addSteps()

        self.recipes[newRecipe.name] = self.__RecipeEncoder().encode(newRecipe)

        with open(os.path.join(os.path.dirname(os.path.realpath(__file__)), F'/recipes/{newRecipe.name}.json'), 'a') as recipeFile:
            recipeFile.seek(0)
            json.dump(self.__RecipeEncoder().encode(newRecipe), recipeFile)
            recipeFile.truncate()
        
        # - I NEED TO STORE THE RECIPE AS A JSON FILE TO BE ACCESSED LATER

class Ingredient:

    def __init__(self, nameOfIngredient, amountNeeded, measuredIn) -> None:
        self.nameOfIngredient = nameOfIngredient
        self.amountNeeded = amountNeeded
        self.measuredIn = measuredIn

class Recipe:

    def __init__(self, name) -> None:
        self.name = name
        self.cookingTools = []
        self.ingredients = []
        self.steps = {}
        self.numOfSteps = 0
        #self.cookingTime = 0 # - CURRENTLY IRRELEVANT, TO BE WORKED IN LATER
        #self.tags = [] # - CURRENTLY IRRELEVANT, TO BE WORKED IN LATER
        #self.price = 0 # - CURRENTLY IRRELEVANT, TO BE WORKED IN LATER

    def __questionLoop(self, nameOfQuestionLoop):

        sleep(0.5)

        pageBreak()

        questionLoopResponse = str(input(F'\n\nWould you like to add any more {nameOfQuestionLoop}s to this recipe? (y/n) ')).lower().strip()
        if questionLoopResponse == 'y':
            return questionLoopResponse
        elif questionLoopResponse != 'n':
            print('I\'m, sorry, I didn\'t understand your input...')
            self.__questionLoop(nameOfQuestionLoop)

    def addCookingTools(self):

        sleep(0.5)

        clearConsole()
        pageBreak()

        print('Currently editing recipe: ' + self.name + '\n\nCurrently added cooking tools:\n' + str(self.cookingTools))

        pageBreak()

        nameOfCookingToolToAdd = input('Name of the cooking tool to add:\n')
        self.cookingTools.append(nameOfCookingToolToAdd)

        clearConsole()
        pageBreak()

        print('Currently editing recipe: ' + self.name + '\n\nCurrently added cooking tools:\n' + str(self.cookingTools))

        moreCookingToolsResponse = self.__questionLoop('cooking tool')
        if moreCookingToolsResponse == 'y':
            self.addCookingTools()

    def addIngredients(self):

        sleep(0.5)

        clearConsole()
        pageBreak()

        print('Currently editing recipe: ' + self.name + '\n\nCurrently added ingredients:\n' + str([ingredientListed.nameOfIngredient for ingredientListed in self.ingredients]))

        pageBreak()

        nameOfIngredientToAdd = input('Name of the ingredient to add:\n')
        ingredientMeasuredIn = input('\nWhat will we use to measure this ingredient? (Tbsp, tsp, kg, g, cups, etc.):\n')
        isIngredientAmountANumber = False
        while isIngredientAmountANumber == False:
            try:
                amountOfIngredientNeeded = input('\nAmount needed (Numbers only):\n') # - I NEED TO VERIFY
                verifiedAmountOfIngredientNeeded = float(amountOfIngredientNeeded)
                isIngredientAmountANumber = True
            except:
                print('\nError - please input a number.')
                sleep(3)
                clearConsole()
                pageBreak()
                print('Currently editing recipe: ' + self.name + '\n\nCurrently added ingredients:\n' + str([ingredientListed.nameOfIngredient for ingredientListed in self.ingredients]))
                pageBreak()
                print(F'Name of the ingredient to add:\n{nameOfIngredientToAdd}')
                print(F'\nWhat will we use to measure this ingredient? (Tbsp, tsp, kg, g, cups, etc.):\n{ingredientMeasuredIn}')

        ingredientToAdd = Ingredient(str(nameOfIngredientToAdd), float(verifiedAmountOfIngredientNeeded), str(ingredientMeasuredIn))
        self.ingredients.append(ingredientToAdd)

        clearConsole()
        pageBreak()

        print('Currently editing recipe: ' + self.name + '\n\nCurrently added ingredients:\n' + str([ingredientListed.nameOfIngredient for ingredientListed in self.ingredients]))

        moreIngredientsResponse = self.__questionLoop('ingredient')
        if moreIngredientsResponse == 'y':
            self.addIngredients()

    def addSteps(self):

        sleep(0.5)

        clearConsole()
        pageBreak()

        print('Currently editing recipe: ' + self.name + '\n\nCurrently added steps:\n' + str(self.numOfSteps))

        pageBreak()

        descriptionOfStepToAdd = input('Please describe the current step:\n')
        self.steps[str(self.numOfSteps + 1)] = descriptionOfStepToAdd
        self.numOfSteps = len(list(self.steps.keys()))

        clearConsole()
        pageBreak()

        print('Currently editing recipe: ' + self.name + '\n\nCurrently added steps:\n' + str(self.numOfSteps))

        moreStepsResponse = self.__questionLoop('step')
        if moreStepsResponse == 'y':
            self.addSteps()


# ---

# --- FUNCTION BLOCK

def pageBreak():
    print('\n---\n')

def clearConsole():
    os.system('cls' if os.name=='nt' else 'clear')

# ---

def main():

    # - I NEED TO CHECK FOR PREVIOUSLY STASHED RECIPE FILES
    # - I NEED TO SPIN UP A NEW COOKBOOK USING ANY EXISTING FILES AS A BASE
    # - I NEED TO ASK USER INPUT FOR WHAT THEY WOULD LIKE TO DO

    #print(os.path.join(os.path.dirname(os.path.realpath(__file__)), '/recipes/'))
    if not os.path.exists(os.path.join(os.path.dirname(os.path.realpath(__file__)), '/recipes/')): # - I NEED TO FIX THIS PATH LATER
        os.mkdir((os.path.join(os.path.dirname(os.path.realpath(__file__)), '/recipes/')))

    clearConsole()
    pageBreak()

    recipeBookForCurrentRun = RecipeBook()
    recipeBookForCurrentRun.addRecipe()

    encodedRecipe = recipeBookForCurrentRun.recipes[list(recipeBookForCurrentRun.recipes.keys())[0]]

    clearConsole()
    pageBreak()

    prettyPrintDict.pprint(encodedRecipe)

    pageBreak()

# --- RUN BLOCK

if __name__ == '__main__':
    
    main()
