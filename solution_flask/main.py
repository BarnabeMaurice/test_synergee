from flask import Flask, render_template, request
import random
import string
import bisect

app = Flask(__name__)

# Limites pour éviter les erreurs
MAX_NUMBER = 10**6
MAX_NUMBER_RANGE = 10**5
MAX_ENTRIES = 10**5
MAX_STRINGS_ENTRIES = 10**5


@app.route("/", methods=["GET", "POST"])
def index():
    results = None
    errors = [] 
    form_data = {}

    if request.method == "POST":
        try:
            # Récupérer les valeurs et les stocker dans form_data
            form_data["num_count"] = int(request.form["num_count"])
            form_data["num_range"] = int(request.form["num_range"])
            form_data["str_count"] = int(request.form["str_count"])
            form_data["search_start"] = int(request.form["search_start"])
            form_data["search_end"] = int(request.form["search_end"])

            # recherche d'erreurs
            if form_data["num_count"] <= 0 or form_data["num_count"] > MAX_ENTRIES:
                errors.append(f"Le nombre d'entrées numériques doit être entre 1 et {MAX_ENTRIES}.")
            if form_data["num_range"] <= 0 or form_data["num_range"] > MAX_NUMBER_RANGE:
                errors.append(f"La plage de nombres doit être entre 1 et {MAX_NUMBER_RANGE}.")
            if form_data["str_count"] <= 0 or form_data["str_count"] > MAX_STRINGS_ENTRIES:
                errors.append(f"Le nombre de chaînes doit être entre 1 et {MAX_STRINGS_ENTRIES}.")
            if form_data["search_start"] < 0 or form_data["search_start"] > MAX_NUMBER:
                errors.append(f"Le début de la recherche doit être entre 0 et {MAX_NUMBER}.")
            if form_data["search_end"] < form_data["search_start"] or form_data["search_end"] > MAX_NUMBER:
                errors.append(f"La fin de la recherche doit être supérieure au début et dans les limites.")

            # en cas d'erreurs on saute directement à l'affichage des erreurs
            if errors:
                raise ValueError()

            # Génération de nombre aléatoire (sans doublons)
            random_num_array = random.sample(range(form_data["num_range"]), form_data["num_count"])

            # Génération de chaîne de caractère aléatoires (sans doublons)
            random_string_array = set()
            while len(random_string_array) < form_data["str_count"]:
                random_string_array.add(''.join(random.choices(string.ascii_letters, k=6)))
            random_string_array = list(random_string_array)

            # Associer les nombres et chaines
            generation_dictionaire = {num: random.sample(random_string_array, k=random.randint(1, min(6, len(random_string_array)))) for num in random_num_array}

            # Trier les clés pour accelerer la recherche
            organiser_dictionnaire = sorted(generation_dictionaire.keys())

            # Recherche dichotomique avec bisect
            premiere_part = bisect.bisect_left(organiser_dictionnaire, form_data["search_start"])
            seconde_part = bisect.bisect_right(organiser_dictionnaire, form_data["search_end"])
            results = {organiser_dictionnaire[i]: generation_dictionaire[organiser_dictionnaire[i]] for i in range(premiere_part, seconde_part)}

        except ValueError:
            errors.append("Erreur : Vérifiez les valeurs saisies et essayez à nouveau.")

    return render_template("index.html", results=results, errors=errors, form_data=form_data)


if __name__ == "__main__":
    app.run(debug=True)
