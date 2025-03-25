import random
import string
import bisect
import pprint

# Génération des nombres
random_num_array = random.sample(range(100000),5000)
print(random_num_array)

# Génération des strings
random_string_array = [''.join(random.choices(string.ascii_letters, k=6)) for _ in range(1000)]
print(random_string_array)

generation_dictionaire = {num: random.sample(random_string_array, k=random.randint(1, 3)) for num in random_num_array}

organiser_dictionnaire = sorted(generation_dictionaire.keys())

def recherche_dichotomique(debut,fin,cle_organiser,dictionnaire):
    premiere_part = bisect.bisect_left(cle_organiser, debut)
    seconde_part = bisect.bisect_right(cle_organiser, fin)
    return {cle_organiser[i]: dictionnaire[cle_organiser[i]] for i in range(premiere_part, seconde_part) }

resultat_recherche = recherche_dichotomique(25000, 26000, organiser_dictionnaire, generation_dictionaire)

print(10**4)

print("\nRésultats pour la plage [25000, 26000] :")
pprint.pprint(resultat_recherche)
