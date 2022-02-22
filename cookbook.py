import json
import os
import sys
import _toolkit as ctk # My personal toolkit - This contains a few helper functions that I reuse regularly


class recipe:

    def __init__(self, name) -> None:
        self.name = name
        self.ingredients = []
        self.cookingTools = []
        self.steps = []
        self.cookingTime = 0
        self.price = 0

    def addIngredient(self):
        pass

    def calculatePriceOfIngredients(self):
        self.price = sum([ingredient['price'] for ingredient in self.ingredients])

    def addCookingTool(self):
        pass

    def addStep(self):
        pass

if __name__ == '__main__':
    ctk.clearConsole()
    ctk.pageBreak()
    ctk.declareScriptEnd()
    ctk.pageBreak()
