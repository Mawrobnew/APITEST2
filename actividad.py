from flask import Flask, request
from flask import jsonify
import pdb
# Instrucciones
# 1. Ruta inicial: Mostrar que la API está en línea
# 2. Ruta que reciba POST (Tomar la data del JSON y usarla dentro de la función. Pueden enviar de vuelta un mensaje con algún dato que haya sido enviado en el JSON)
# 3. Ruta que envíe un objeto de Python (Diccionario, Lista o Tupla)

app=Flask(__name__)

#1. Ruta inicial
@app.route('/')
def index():
    return "Ola"
#2. Ruta que reciba POST
@app.route('/enviar',methods=['POST'])
def enviar_objeto():
    dato=request.json
    mensaje = f"El mensaje escrito {dato}"
    return mensaje

#3. Ruta que envie un objeto  
una_lista=[{
    'id':'1'
},{
    'id':'2'
}]

@app.route('/identificadores')
def obtener_id():
    return jsonify(una_lista)


#Punto de inicio
if __name__ =='__main__':
    app.run(debug=True)   