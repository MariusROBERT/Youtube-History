import json


with open('watch-history.json', 'r') as f:
    historique = json.load(f)

afficher_top = 10

compteur_indispo = 0

chaines = {}
videos = {}
videos_uniques = {}

# print(type(historique))

for i in historique:
    try:
        chaine = i["subtitles"][0]["name"]
        if chaine in chaines.keys():  # (chaine):
            chaines[chaine] += 1
        else:
            chaines[chaine] = 1

        if i["title"] in videos.keys():  # (i.title):
            videos[i["title"]] += 1
        else:
            videos[i["title"]] = 1

            try:
                videos_uniques[chaine] += 1
            except KeyError:
                videos_uniques[chaine] = 1

    except:
        # print("blabla")
        # print(i)

        #print("Vidéo supprimée/non répertoriée")
        compteur_indispo += 1


# print(historique[0])

#dict(sorted(x.items(), key=lambda item: item[1]))

compteur = 0

for keys, value in reversed(dict(sorted(chaines.items(), key=lambda item: item[1])).items()):
    if compteur < afficher_top:
        print("Chaine : {}     Vidéos vues : {}".format(keys, value))
        compteur += 1
    else:
        break


print()


compteur = 0

for keys, value in reversed(dict(sorted(videos.items(), key=lambda item: item[1])).items()):
    if compteur < afficher_top:
        print("Video  : {}     Nombre de vues : {}".format(keys[18:], value))
        compteur += 1
    else:
        break

print()

compteur = 0

for keys, value in reversed(dict(sorted(videos_uniques.items(), key=lambda item: item[1])).items()):
    if compteur < afficher_top:
        print("Chaine : {}     Vidéos Uniques vues : {}".format(keys, value))
        compteur += 1
    else:
        break


# print(chaines)
print()
# print(videos)


print("Vidéos désormais plus disponibles : {}".format(compteur_indispo))

# print(test)
"""
{'header': 'YouTube',
'title': 'Vous avez regardé Best Of Coro #214 - SHINZOU WO SASAGEYO',
'titleUrl': 'https://www.youtube.com/watch?v=QsxvCDEjrY8',
'subtitles': [{'name': 'Best Of Corobizar',
                'url': 'https://www.youtube.com/channel/UCp0h67F7SePS_QxoX6S2lPQ'}],
'time': '2021-03-11T13:09:04.709Z',
'products': ['YouTube']}
"""
