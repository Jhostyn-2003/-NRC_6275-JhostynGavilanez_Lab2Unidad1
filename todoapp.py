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
def panelPrincipal():   # es la ruta principal del primer controlador raiz
    return render_template('/index.html', ListasApp=ListasApp)

#---------------------------------------------------------------------------
# Este es el segundo paso para enviar datos a nuestra lista mediante el formulario dado.
# Controlador de envio.
@app.route('/enviar', methods=['POST'])
# metodo de guardar los datos
def enviar():  #Aqui realiza el envio de datos para ser guardados en la lista. 
    if request.method == 'POST':
# el mensaje de añadir un registro de un nuevo dato se muestra por codigo javascript en el html 
        lista_Name = request.form['lista_Name']
        lista_Email = request.form['lista_Email']
        lista_Prioridad = request.form['lista_Prioridad']

        if lista_Name == '' or lista_Email == '' or lista_Prioridad=='': #El mensaje esta por codigo javascript dentro del HTML
                return redirect(url_for('panelPrincipal'))
        else:
                ListasApp.append(
                    {'lista_Name': lista_Name,
                     'lista_Email': lista_Email, 
                     'lista_Prioridad': lista_Prioridad})

                return redirect(url_for('panelPrincipal'))




#---------------------------------------------------------------------------
#Controlador de la ruta para borrar todos los datos encontrados en la lista 
#Controlador de borrar registros 
@app.route('/borrar', methods=['POST'])
def borrar():              # La funcion de envio de mensaje borrado se hace mediante codigo Javascript
     ListasApp.clear()
     return redirect(url_for('panelPrincipal'))
  



# ejecutar del main principal de la pagina To DO local host 
if __name__ == '__main__':
    app.run(debug=True)
