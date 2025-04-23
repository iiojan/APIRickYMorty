import ramapi

pejota = ramapi.Character.filter(name="Rick")

for personaje in pejota["results"]:
    print(personaje['name'], personaje['id'])