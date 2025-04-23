import ramapi
from flask import Flask, render_template 


app = Flask(__name__)

@app.route("/")
def personajes():

    personajesPrincipales = ["Rick Sanchez", "Morty Smith", "Jerry Smith", "Summer Smith", "Beth Smith"]
    personajesAMostrar = []

    for pj in personajesPrincipales:
        pejota = ramapi.Character.filter(name=pj)
        personajes = pejota["results"]  # Lista de dicts
        personajesAMostrar.extend(personajes)
        
    return render_template("index.html", personajes=personajesAMostrar)


if __name__ == "__main__":
    app.run(debug=True)