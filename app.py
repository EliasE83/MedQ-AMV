#Importar el framework
from flask import Flask, render_template, request, redirect, url_for, flash
from flask_mysqldb import MySQL
from flask_login import LoginManager, login_user,login_required, logout_user, current_user,UserMixin

#Inicializacion del APP
app = Flask(__name__)

#Configuracion de la conexion a la BD
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] ='bdmedq'
app.secret_key = 'mysecretkey'
mysql = MySQL(app)

#login

class User(UserMixin):
    def __init__(self, id, rfc, password, rol,nombre):
        self.id = id
        self.rfc = rfc
        self.password = password
        self.rol = rol
        self.nombre = nombre

    def get_id(self):
        return str(self.id)
    
login_manager = LoginManager(app)
login_manager.login_view = 'login'


@login_manager.user_loader
def load_user(id):
    print("este es mi id: " + id)
    
    cursor = mysql.connection.cursor() 
    cursor.execute('SELECT id, correo, contra, id_estatus, nombre FROM Personas WHERE id = %s', (id,))
    persona = cursor.fetchone()
    if persona:
        print("Metodo: load_user(id), el usuario si coincide.")


        
        return User(id=persona[0], rfc=persona[1],password = persona[2], rol=persona[3],nombre=persona[4])
    
    return None

#Rutas

@app.route('/')
def login():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def log():
    if request.method == 'POST':
        rfc = request.form['txtCorreo']
        password = request.form['txtContra']

        cursor = mysql.connection.cursor()
        query = 'SELECT id, correo, contra, id_estatus,nombre FROM Personas WHERE correo = %s and contra = %s'
        cursor.execute(query, (rfc, password))
        persona = cursor.fetchone()
    
        print("Metodo: login(), rfc y pass que llegan desde front: RFC {} pass {}".format(rfc, persona))
        print("Metodo: rfc(), antes de validar rfc y pass")
        if persona:
            print("Metodo: login(), rfc y pass correctos")
            user = User(id=persona[0], rfc=persona[1], password=persona[2], rol=persona[3],nombre=persona[4])
            if (persona[3] == 1):
                flash('CONECTADO')
                login_user(user)
                return redirect(url_for('indexA'))
            elif(persona[3]==2):
                flash('CONECTADO')
                login_user(user)
                return redirect(url_for('indexM'))
            flash('CONECTADO')
            login_user(user)
            return redirect(url_for('indexU'))
        else:
            print("Usuario o Contraseña Incorrectas")
            flash('Usuario o Contraseña Incorrectas')
            return render_template('login.html')
    else:
        print("Datos login incompletos")
        return render_template('login.html')

@app.route('/indexU')
def indexU():
    return render_template('user.html')

@app.route('/indexM')
def indexM():
    return render_template('/vistas_principales/med.html')

@app.route('/indexA')
def indexA():
    return render_template('/vistas_principales/admin.html')

@app.route('/citas')
def citas():
    return render_template('citas.html')

@app.route('/consultas')
def consultas():
    return render_template('consultas.html')

@app.route('/nuevaconsulta')
def nuevaconsulta():
    return render_template('nuevaconsulta.html')


#Ejecucion del Servidor en el puerto 5000
if __name__ == '__main__':
    app.run(port=5000, debug=True)