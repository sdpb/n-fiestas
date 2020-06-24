class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        text = "Persona: ("
        text = text + self.name + ":"
        text = text + str(self.age) + ") "
        return text


def seeList(data):
    i = 1
    text = "LIST: \n"
    for personX in data:
        line = "[{}]: {}\n".format(i, personX)
        i += 1
        text += line
    text += "......................Fin de la x_list.\n"
    return text


class List:
    def __init__(self):
        self.list = []

    def add(self, obj):
        self.list.append(obj)

    def __str__(self):
        return seeList(self.list)

    def __len__(self):
        return len(self.list)

    def changeList(self, aList):
        self.list = aList
