# Sujet

# Mettre les animaux suivi-dessous dans une liste de dictionnaires
# Grâce à une boucle, afficher tous les animaux sous la forme:
#     “Le Lièvre marron court à 60km/h”
# Si l’animal en question est le plus rapide, ajouter “et c’est lui le plus rapide”
# Si l’animal en question est le plus lent, ajouter “et c’est lui le plus lent”

# Animaux
# Lièvre, marron, 60
# Hérisson, gris, 10
# Lapin, blanc, 30
# Guépard, orange, 90
# Faucon, noir, 120
# Girafe, jaune, 70
# Perroquet, bleu, 50


# Pour aller plus loin 

# Simuler une course avec les animaux au départ (demander la longueur de la course)
# Faire passer une heure à chaque tour et avancer les animaux en conséquence (afficher la distance parcourue pour chacun)
# Quand un animal franchi la ligne d’arrivée, lui attribuer un numéro d’arrivée et ne plus le faire avancer
# Quand tous les animaux sont arrivés, terminer la course en annonçant le gagnant (“Faucon noir à gagné en … heures”)

animals = [
    {
        "Name" : "Lièvre",
        "Color" : "marron",
        "Speed" : "60"
    },
    {
        "Name" : "Hérisson",
        "Color" : "gris",
        "Speed" : "10"
    },
    {
        "Name" : "Lapin",
        "Color" : "blanc",
        "Speed" : "30"
    },
    {
        "Name" : "Guépard",
        "Color" : "orange",
        "Speed" : "90"
    },
    {
        "Name" : "Faucon",
        "Color" : "noir",
        "Speed" : "120"
    },
    {
        "Name" : "Girafe",
        "Color" : "jaune",
        "Speed" : "70"
    },
    {
        "Name" : "Perroquet",
        "Color" : "bleu",
        "Speed" : "50"
    },
]


slower = "et c’est lui le plus lent"

speed = 0
slowSpeed = 12
for elem in animals:
    if(int(elem['Speed']) > speed):
        speed = int(elem['Speed'])
        faster = "et c’est lui le plus rapide" 
        fasterAnimal = f"Le {elem['Name']} {elem['Color']} court à {elem['Speed']}km/h {faster}"
    if(int(elem['Speed']) < slowSpeed):
        slowSpeed = int(elem['Speed'])
        slower = "et c’est lui le plus lent"
        slowerAnimal = f"Le {elem['Name']} {elem['Color']} court à {elem['Speed']}km/h {slower}"

    if(120 == speed):
        print(f"SPEED == {speed}")
        print(fasterAnimal)
        print(f"Le {elem['Name']} {elem['Color']} court à {elem['Speed']}km/h {faster}")
    elif(elem['Speed'] == slowSpeed):
        print(slowerAnimal)
    else:
        print(f"Le {elem['Name']} {elem['Color']} court à {elem['Speed']}km/h")




       
    # print(f"Le {elem['Name']} {elem['Color']} court à {elem['Speed']}km/h")