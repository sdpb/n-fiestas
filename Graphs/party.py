from colorama import init, Fore
from BaseClasses.simulate import *

acquaintance = {}
personList = []
partyList = []


def makePerson(n):
    for _ in range(n):
        person = genName(genGender())
        while person in personList:
            person = genName(genGender())
        personList.append(person)
        acquaintance[person] = []


def knownPeople():
    for person in personList:
        for _ in range(random.randint(int(len(personList) * 0.0), int(len(personList) * 0.25))):
            friend = random.choice(personList)
            if person != friend and not (friend in acquaintance[person]):
                acquaintance[person].append(friend)
                acquaintance[friend].append(person)


def party():
    partyList.clear()
    known = True
    for _ in personList:
        if len(acquaintance[_]) == len(personList) - 1:
            continue
        else:
            if not partyList:
                partyList.append(_)
            elif not (_ in partyList):
                for guest in partyList:
                    if _ in acquaintance[guest]:
                        known = True
                        break
                    else:
                        known = False
                if not known:
                    partyList.append(_)
                    known = True


def meetPeople():
    for _ in partyList:
        a = partyList[:]
        a.remove(_)
        print("{:<30} : {:<20}".format(_, str(acquaintance[_])))
        acquaintance[_] = acquaintance[_] + a
        print("{:<30} : {:<20}".format(_, str(acquaintance[_])))


def debPrint(state):
    if state == "i":
        print(Fore.RED + "Initial state" + Fore.RESET)
    elif state == "f":
        print(Fore.RED + "Final state" + Fore.RESET)
    for _ in acquaintance:
        print("{:<30} ==> {:<20}".format(_, str(acquaintance[_])))
    print()


def genGraph(n):
    init()
    makePerson(n)
    knownPeople()

    debPrint("i")

    parties = totalPeopleInParties = 0
    while True:
        print()
        party()
        if not partyList:
            break
        parties += 1
        peopleInParty = len(partyList)
        totalPeopleInParties += len(partyList)
        print(Fore.YELLOW + "Number of party:", parties, "- People in party:",
              peopleInParty, Fore.RESET)

        print(Fore.BLUE + "Guests ", partyList, Fore.RESET)
        meetPeople()

    debPrint("f")
    print(Fore.GREEN + "Total People in parties:", totalPeopleInParties)
    print("Total parties:", parties, "\n" + Fore.RESET)
