import pandas as pd
# planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']
# card = ['1']
# planet_to_initial = {planet: planet[0] for planet in planets}
# print(planet_to_initial.values)
# aa = '         '.join(sorted(planet_to_initial.values()))
# print(planet_to_initial.values())
# print(type(card))
# for a in card:
#     print(type(a)
data = pd.read_csv('archive/melb_data.csv',index_col = 0)

dir(pd.DataFrame.columns)