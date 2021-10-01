# # EXERCIE 1
# print("Tout droit tu grimperas,")
# print("La clé tu trouveras,")
# print("Habile tu seras,")
# print("Quand tu les porteras,")
# print("Et avec le chef tu reviendras !")


# # DANS LE FOURRE
# from robot import *
# for i in range(30):
#    print("a_",end="")
# print("")
# for i in range(30):
#    print("b_",end="")
# print("")
# for i in range(30):
#    print("c_",end="")

# for loop in range(39):
#     for loop in range(10):
#         print("O", end = "")
#         print("X", end = "")
#     print()
#     for loop in range(10):
#         print("X", end = "")
#         print("O", end = "")
#     print()

# long = (5*17) + (2*7) + 5 + (2*2)
# print(long)
# print(long*2)
# print(long*4)

# candy = 0
# for i in range(50):
#     if(i == 0):
#         candy += 1
#     else:
#         candy = candy + i + 1
#     print(candy)

# cube = 17
# calc = 0
# for i in range(8):
#     calc += cube * cube * cube
#     cube-=2
# calc+=1
# print(calc)

# for i in range(20):
#     num = i + 1
#     for e in range(20):
#         one = e + 1
#         print(num * one," ", end="")
        
#     print("\n")
    # print(f"{num}  {num*2}")


# longueur = int(input(""))
# def champs(long):
#     carre = long * long
#     print(23*carre)  
# champs(longueur)

# km = int(input())
# print(km * (16*3600))

# num = int(input())
# add = 66
# for i in range(num):
#     if(i == 0):
#        print(1*add) 
#     else:
#         iTotal = i
#         total = (iTotal)* add
#         add = add + total
#         print(add)


# positionDepart = 10
# largeurEmplacement = 5
# nbVendeurs = 3
# for i in range(nbVendeurs+1):
#     print(positionDepart + (largeurEmplacement*i))


# valMax = 7
# valMin = 3
# result = 0
# for i in range((valMax - valMin)+1):
#    if(valMin <= valMax): 
#       result = result + (valMin * valMin)
#       valMin += 1
#    else:
#       break
# print(result)


# nbKarvas = 2
# for i in range(nbKarvas):
#     poids = 100
#     age = 5
#     corn = 25
#     garrot = 90
#     print(corn*garrot + poids)

# heureArriv = 12
# prixMax = 53
# prix = 10

# if(heureArriv  == 0):
#    print(prix)
# else:
#    if(prix == 53):
#       prix = 53
#    elif(prix <= 53):
#      for i in range(heureArriv):
#         prix += 5
#         if(prix > 53):
#             prix = prixMax    
#    print(prix)

# heure = 12
# prix = 10 + 5 * heure
# if prix > 53:
#    prix = 53
# print(prix)

# champAri = 10
# champEva = 20
# nomAri = "Arignon"
# nomEva = "Evaran"

# if(champAri < champEva):
#     result = champEva - champAri
#     if(result > 10):
#         nom = "La famille "+nomEva+" a un champ trop grand "
#         # print(" La famille",nom,"a un champ trop grand ")
# elif(champAri > champEva):
#     result = champAri - champEva
#     if(result > 10):
#         nom = "La famille "+nomAri+" a un champ trop grand "
#         # print(" La famille",nom,"a un champ trop grand ")
# else:
#     nom = ""
# print(nom)


# age = int(input())
# if(age < 21):
#     print("Tarif réduit")
# else:
#     print("Tarif plein")


# intNo1 = int(input())
# intNo2 = int(input())
# somme = intNo1 + intNo2
# if(somme >= 10):
#     taxe = 36
#     print("Taxe spéciale !")
#     print(taxe)
# else:
#     taxe = somme * 2
#     print("Taxe régulière")
#     print(taxe)
    

# nbMembres = int(input())
# totalEquipes = nbMembres * 2
# pds1 = 0
# pds2 = 0
# for i in range(totalEquipes):
#     poids = int(input())
#     if(i%1 == 0):
#         pds1 += poids
#     else:
#         pds2 += poids
# if(pds1 > pds2):
#     print("L'équipe 1 a un avantage")
# else:
#     print("L'équipe 2 a un avantage")
# print("Poids total pour l'équipe 1 :",pds1)
# print("Poids total pour l'équipe 2 :",pds2)


# recupMdp = int(input())
# if(recupMdp == 64741):
#     print("Bon festin !")
# else:
#     print("Allez-vous en !")

# recupVille = int(input())
# totalHab = 0
# for i in range(recupVille):
#     numberHab = int(input())
#     if(numberHab > 10000):
#         totalHab += 1
# print(totalHab)

# positionStart = int(input())
# village = int(input())
# nbVillage = 0
# for i in range(village):
#     nextVillage = int(input())
#     if((positionStart + 50) < nextVillage + positionStart or (positionStart + 50) > nextVillage - positionStart and positionStart - nextVillage <= 50):
#         nbVillage += 1
    
# print(nbVillage)

# if(nextVillage > 0):
#     if(positionStart > nextVillage):
#         if((positionStart + 50) < nextVillage + positionStart):
#             nbVillage += 1
#     elif(positionStart < nextVillage):
#         if((positionStart + 50) > nextVillage - positionStart):
#             nbVillage += 1


# positionStart = int(input())
# village = int(input())
# nbVillage = 0
# for i in range(village):
#     positionStartPlus = positionStart + 50
#     positionStartMoins = positionStart - 50
#     nextVillage = int(input())
#     if(nextVillage < positionStartMoins):
#         nbVillage += 0
#     elif(nextVillage > positionStartPlus):
#         nbVillage +=0
#     else:
#         nbVillage +=1
# print(nbVillage)