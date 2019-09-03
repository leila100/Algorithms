#!/usr/bin/python

import math


def recipe_batches(recipe, ingredients):
    keys = list(recipe)
    if not keys[0] in list(ingredients):
        return 0
    # Initialize the maximum number of batches to the maximum number of batches for the first ingredient
    max_batches = ingredients[keys[0]] // recipe[keys[0]]

    for key in keys[1:]:
        if not key in list(ingredients):
            return 0
        # get smallest division
        batches = ingredients[key] // recipe[key]
        if batches < max_batches:
            max_batches = batches
    return max_batches


if __name__ == '__main__':
    # Change the entries of these dictionaries to test
    # your implementation with different inputs
    recipe = {'milk': 100, 'butter': 50, 'flour': 5}
    ingredients = {'milk': 232, 'butter': 255, 'flour': 251}
    print("{batches} batches can be made from the available ingredients: {ingredients}.".format(
        batches=recipe_batches(recipe, ingredients), ingredients=ingredients))
