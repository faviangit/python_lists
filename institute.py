institute = ['house_apollo', 'house_ceres', 'house_diana', 'house_juno', 'house_jupiter', 'house_mars', 'house_minerva', 'unknown_house']

print(institute[3])

for home in institute:
    print('darrow will join', home)
    if home == 'house_mars':
        print('he will be primus')

institute[5] = 300
print(institute)

h = len(institute)
print(h)

w = 'beware the howlers'
for home in institute:
    if home == 'house_diana':
        print(w)

institute[5] = 'house_mars'
for home in institute:
    print('welcome to', home)