import ramapi
from flask import Flask, render_template 
import time
import requests


app = Flask(__name__)



try:
    urlAPI = "https://rickandmortyapi.com/api"

    respuesta = requests.get(urlAPI)
    respuesta.raise_for_status()
    tiempo = respuesta.elapsed.total_seconds()
    mensaje = f"[{respuesta.status_code}] ¡Éxito en la solicitud!. Tiempo de ejecución: {tiempo} segundos."
    print(mensaje)

except requests.exceptions.HTTPError as error:
    print(f"\033[1;91mERROR EN LA SOLICITUD HTTP: \033[93m {error}\033[0m")
except requests.exceptions.RequestException as err:
    print(f"\033[1;91mERROR EN LA COENXIÓN: \033[93m {err}\033[0m")

    
@app.route("/")
def personajes():

    personajesPrincipales = ["Rick Sanchez", "Morty Smith", "Jerry Smith", "Summer Smith", "Beth Smith"]
    personajesAMostrar = []

    for pj in personajesPrincipales:
        pejota = ramapi.Character.filter(name=pj)
        personajes = pejota["results"]
        personajesAMostrar.extend(personajes)

    return render_template("index.html", personajes=personajesAMostrar)


if __name__ == "__main__":
    app.run(debug=True)