"""
    Randomly draw all persons from a list
"""
# coding: utf-8

# imports
import random


# functions
def main():
    """
        Randomly draw all persons from a list
    """

    peoples = [
        "Timothée",
        "Gael",
        "David",
        "Quentin",
        "Théo",
        "Nicolas",
        "Jojo",
        "Jordan",
        "Adrien",
        "Cécilia"]

    peoplesEnd = [
        ["         "],
        ["         "],
        ["         "],
        ["         "],
        ["         "],
        ["         "],
        ["         "],
        ["         "],
        ["         "],
        ["         "]]
    # number = 1

    # while len(peoples) != 0:




    new_list_ppl = list(peoples)

    for name in new_list_ppl:
        
        number = new_list_ppl.index(name) + 1
        index_random_people = random.randint(0, len(peoples)-1)
        poped_person = peoples.pop(index_random_people)
        start_string = f"{number}ème"
        end_string = f"il reste {len(peoples)} personnes"

        if number == 1:
            start_string = f"{number}er"

        if len(peoples) == 0:
            end_string = "il ne reste plus personne"

        print(f"{start_string} {poped_person} {end_string}")







        # {peoplesEnd[i]
        # print(f"{start_string} {poped_person}", end ="")

        # peoplesLen = len(peoples[i])
        # test = 0  

        # longName = len(start_string) + len(poped_person)
        # space = "x"*longName

        # print(space, end ="")
        # print(peoplesEnd[i])
        


# code starts here
if __name__ == "__main__":
    main()

