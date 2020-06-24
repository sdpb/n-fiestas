import random

men = ['ANTONIO', 'JOSE', 'FRANCISCO', 'JUAN', 'MANUEL', 'PEDRO', 'JESUS', 'ANGEL', 'MIGUEL', 'JAVIER',
       'JOSE ANTONIO', 'DAVID',
       'CARLOS', 'JOSE LUIS', 'ALEJANDRO', 'MIGUEL ANGEL', 'FRANCISCO JAVIER', 'RAFAEL', 'DANIEL',
       'JUAN JOSE', 'LUIS', 'PABLO', 'JUAN ANTONIO', 'JOAQUIN', 'SERGIO', 'FERNANDO',
       'JUAN CARLOS', 'ANDRES', 'JOSE MANUEL', 'JOSE MARIA', 'RAMON', 'RAUL', 'ALBERTO', 'ENRIQUE', 'ALVARO',
       'VICENTE',
       'EMILIO', 'FRANCISCO JOSE', 'DIEGO', 'JULIAN', 'JORGE', 'ALFONSO', 'ADRIAN',
       'RUBEN', 'SANTIAGO', 'IVAN', 'JUAN MANUEL', 'PASCUAL', 'JOSE MIGUEL', 'MARIO']

women = ['MARIA', 'MARIA CARMEN', 'JOSEFA', 'ISABEL', 'MARIA DOLORES', 'CARMEN',
         'FRANCISCA', 'MARIA PILAR', 'DOLORES', 'MARIA JOSE', 'ANTONIA', 'ANA', 'MARIA ISABEL',
         'MARIA ANGELES', 'PILAR', 'ANA MARIA', 'LUCIA', 'CRISTINA', 'LAURA', 'ENCARNACION', 'JUANA', 'MARIA TERESA',
         'ROSARIO', 'ELENA', 'MARTA',
         'MANUELA', 'ROSA MARIA', 'MARIA LLANOS', 'MARIA JOSEFA', 'RAQUEL', 'ANGELES', 'CONCEPCION', 'MERCEDES',
         'IRENE', 'TERESA', 'BEATRIZ',
         'PAULA', 'ANGELA', 'JULIA', 'ANA BELEN', 'ROCIO', 'AMPARO', 'ALICIA', 'CONSUELO', 'ROSA', 'ASCENSION',
         'ANDREA',
         'MARIA ROSARIO', 'MARIA JESUS', 'MARIA LUISA']

surname = ['MARTINEZ', 'LOPEZ', 'SANCHEZ', 'GONZALEZ', 'GOMEZ',
           'FERNANDEZ', 'MORENO', 'JIMENEZ', 'PEREZ', 'RODRIGUEZ',
           'NAVARRO', 'RUIZ', 'DIAZ', 'SERRANO', 'HERNANDEZ', 'MUÑOZ', 'SAEZ', 'ROMERO',
           'RUBIO', 'ALFARO', 'MOLINA', 'LOZANO', 'CASTILLO', 'PICAZO', 'ORTEGA', 'MORCILLO',
           'CANO', 'MARIN', 'CUENCA', 'GARRIDO', 'TORRES', 'CORCOLES', 'GIL',
           'ORTIZ', 'CALERO', 'VALERO', 'CEBRIAN', 'RODENAS', 'ALARCON', 'BLAZQUEZ', 'NUÑEZ',
           'PARDO', 'MOYA', 'TEBAR', 'REQUENA', 'ARENAS', 'BALLESTEROS', 'COLLADO', 'RAMIREZ',
           'VALENCIA']


def genName(gender):
    if gender == 'F':
        name = random.choice(women)
    else:
        name = random.choice(men)
    surname1 = random.choice(surname)
    surname2 = random.choice(surname)
    name = name + " " + surname1 + " " + surname2
    return name


def genAge():
    return random.randint(18, 85)


def genGender():
    return random.choice(['F', 'M'])
