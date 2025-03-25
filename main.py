import random
import string
import pprint

random_num_array = random.sample(range(200),20)
print(random_num_array)

random_string_array = [''.join(random.choices(string.ascii_letters, k=6)) for _ in range(10)]
print(random_string_array)

dictionnaire_generation = {num: random.sample(random_string_array, k=random.randint(1, 3)) for num in random_num_array}

def recherche(debut,fin,dictionnaire):
    return {num: strings for num, strings in dictionnaire.items() if debut <= num <= fin }

resultat_recherche = recherche(50, 100, dictionnaire_generation)

print("\nRésultats pour la plage [50, 100] :")
pprint.pprint(resultat_recherche)
