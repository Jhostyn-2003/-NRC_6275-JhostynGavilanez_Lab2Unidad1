# Nombre: Jhostyn Javier Gavilanez Suarez

# importar la libreria flask
# En este apartado se añade la libreria de flask, entre otras para hacer el llamado y otras funcionalidades de la pagina TO Do.
from flask import Flask, render_template, redirect, request, url_for
#---------------------------------------------------------------------------
# Este es el nombre para llamar a los templates de python, ya que se inicializa y se llama a traves del templates donde tenemos nuestra carpeta.
app = Flask(__name__, template_folder='templates')
#---------------------------------------------------------------------------
# Este es el arreglo para almacenar las tareas en forma de lista.
ListasApp = [] # arreglo de la lista
#---------------------------------------------------------------------------
#Password para tener acceso a dicha aplicacion mediante el uso del secret key
app.secret_key = 'jhostyn2022'    
#---------------------------------------------------------------------------
# Este es el primer paso ver las listas de las tareas pendientes
# Esta es la ruta raiz donde esta nuestro html controlador  raiz
@app.route('/')
# llamar a index.html en la ruta principal
def panelPrincipal():
    return render_template('/index.html', ListasApp=ListasApp)



# ejecutar del main principal de la pagina To DO local host 
if __name__ == '__main__':

    app.run(debug=True)
