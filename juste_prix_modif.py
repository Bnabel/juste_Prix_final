import random  # Module

print("|================================================================================================================================|")
input("|                         Bienvenue aux jeux du juste prix appuyé sûr <ENTER> pour commencer                                     |")
print("|================================================================================================================================|")

# Le joueur choisit son niveau.
choix_niveau = int(input("Vous avez trois niveaux de difficulté\nNiveau 1: mode facile, vous devez deviner un nombre de 1 à 100 sans limite de temps\nNiveau 2: mode normal, vous devez deviner un nombre de 1 à 100 mais vous n'avez que dix essais\nNiveau 3: mode personnalisé, vous pouvez choisir un prix au hasard qui sera supérieur à 1 et au nombre d'essais qui vous plaira.\nQuel sera votre choix ? "))

# Mode de difficulté
mode_facile = 1
mode_normal = 2
mode_personnalise = 3

# =========|
# Niveau 1 |
# =========|

try:
    if choix_niveau == mode_facile:
        prix_propose = int(input(
            "Entrez un prix entre 1 et 100: pour abandonner la partie appuyée sur 0: "))
        # Nombre générer par la fonction randint entre 1 et 100
        juste_prix = random.randint(1, 100)

        while prix_propose != juste_prix:
            if prix_propose == 0:
                exit('Vous avez perdue la partie, abandon !!! ')
            elif juste_prix < prix_propose:
                print("C’est moins")
                prix_propose = int(input("Entrer un prix entre 1 et 100 : "))
            elif juste_prix > prix_propose:
                print("C’est plus")
                prix_propose = int(input("Entrer un prix  entre 1 et 100: "))
        else:
            print(
                f"Félicitations :-) le juste prix est le numéro ({juste_prix})")

# =========|
# Niveau 2 |
# =========|
    if choix_niveau == mode_normal:
        # Nombre générer par la fonction randint entre 1 et 100.
        juste_prix = random.randint(1, 100)
        prix_propose = 0
        nombre_essai_max = 10
        nombre_essai_min = 1

        print(
            f"Entrer un prix entre 1 et 100 : Vous avez {nombre_essai_max } essais! bonne chance")
        while prix_propose != juste_prix and nombre_essai_min <= nombre_essai_max:
            print("Essai numéro", nombre_essai_min)

            prix_propose = int(input("Votre prix_propose :"))
            if prix_propose == 0:
                exit('Vous avez perdue la partie, abandon !!! ')
            elif prix_propose < juste_prix:
                print("c'est plus")
            elif prix_propose > juste_prix:
                print("c'est moins")
        else:
            print(
                f"Félicitations :-) le juste prix est le ({juste_prix}), vous avez réussi avec {nombre_essai_min} essais")

            nombre_essai_min += 1  # Compteur

        if nombre_essai_min > nombre_essai_max and prix_propose != juste_prix:
            print(
                f"La partie est terminée :-( le nombre à trouver était le {juste_prix}")

# =========|
# Niveau 3 |
# =========|
    if choix_niveau == mode_personnalise:
        prix_min = 1
        prix_max = 0
        nombre_essai_max = 0
        nombre_essai_min = 1
        prix_propose = ''
        print('Veuillez choisir un prix ?')
        prix_max = int(input())
        print("Veuillez choisir un nombre d'essais ?")
        nombre_essai_max = int(input())

    # Le nombre généré sera minimum 1 par défaut et le maximum, sera le nombre que l'utilisateur aura entré.
        juste_prix = random.randint(prix_min, prix_max)

        if nombre_essai_max == 0:
            print(
                f"Le juste prix sera de 1 à {prix_max} votre nombre d'essais est illimité.")
            nombre_essai_min -= 1  # Compteur
        else:
            print(
                f"Le juste prix sera de 1 à {prix_max} et vous aurez {nombre_essai_max} essais ")

        while prix_propose != juste_prix and nombre_essai_min <= nombre_essai_max:
            prix_propose = int(input("Votre prix_propose :"))

            if nombre_essai_max != 0:
                print("Essai numéro", nombre_essai_min)
                
            if prix_propose == 0:
                exit('Vous avez perdue la partie, abandon !!! ')

            elif prix_propose < juste_prix:
                print("c'est plus")
            elif prix_propose > juste_prix:
                print("c'est moins")
            else:
                print(
                    f"Félicitations :-) le juste prix est le numéro ({juste_prix})")

            if nombre_essai_max != 0:
                nombre_essai_min += 1  # Compteur

    if nombre_essai_max <= nombre_essai_min and prix_propose != juste_prix:
        print(
            f"La partie est terminée :-( le nombre à trouver était le numéro {juste_prix}")

except ValueError:
    print('Les caractères sont interdits ! veuillez relancer la partie svp.')
