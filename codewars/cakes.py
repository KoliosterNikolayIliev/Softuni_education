# def cakes(recipe, available):
#     try:
#         quantity = []
#         for key in recipe.keys():
#             quantity.append(available[key] // recipe[key])
#         return min(quantity)
#     except:
#         return 0


def cakes(recipe, available):
    return min(available.get(k, 0)/recipe[k] for k in recipe)


# must return 2
print(cakes({"flour": 500, "sugar": 200, "eggs": 1}, {"flour": 1200, "sugar": 1200, "eggs": 5, "milk": 200}))
# must return 0
print(cakes({"apples": 3, "flour": 300, "sugar": 150, "milk": 100, "oil": 100},
            {"sugar": 500, "flour": 2000, "milk": 2000}))
