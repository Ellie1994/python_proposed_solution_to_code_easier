names = ["Bruce", "Clark", "Peter"]
heros = ["Batman", "Superman", "Spiderman"]

for name, hero in zip(names, heros):
    print(name, hero)



# output in Py3: 
# Bruce Batman
# Clark Superman
# Peter Spiderman

# output in later versions:
# ('Bruce', 'Batman')
# ('Clark', 'Superman')
# ('Peter', 'Spiderman')

