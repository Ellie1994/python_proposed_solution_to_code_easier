names = ["Bruce", "Clark", "Peter"]
heros = ["Batman", "Superman", "Spiderman"]


my_dict = {}
for name, hero in zip(names, heros):
    my_dict[name] = hero
print(my_dict)

# output:
# {'Bruce': 'Batman', 'Clark': 'Superman', 'Peter': 'Spiderman'}

