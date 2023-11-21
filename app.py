#http://127.0.0.1:5000
from flask import Flask, render_template, request
import mysql.connector

mydb = mysql.connector.connect(
        host='localhost',
        user='root',
        port=3306,
        password='n0m3l0',
        database='Bayheart'
    )

myCursor = mydb.cursor()

app = Flask(__name__, static_folder='templates', static_url_path='/')


@app.route('/')
def inicio():    
    return render_template('sitio/index.html')

@app.route('/registro')
def registro():
    return render_template('sitio/registro.html') 
   
@app.route('/paginaprincipal', methods=["POST"])
def paginaprincipal():
    return render_template('sitio/paginaprincipal.html') 


@app.route('/sigup', methods=["POST"])
def sigup():
    if request.method == "POST":
        name = request.form['nombre']
        contra = request.form['contra']
        passi = request.form['confirmm']        

        query = f"INSERT INTO Usuario(nombre,contrasenia,confirm) VALUES ('{name}','{contra}','{passi}')"        
        myCursor.execute(query)    
        mydb.commit() #Confirma los cambios
        return render_template('sitio/paginaprincipal.html') 
    else:
        return 'OH NO'


if __name__ == '__main__' :
    app.run(debug=True)

