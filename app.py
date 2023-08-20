#Importar el framework
from flask import Flask, render_template, request, redirect, url_for, flash
from flask_mysqldb import MySQL
from flask_login import LoginManager, login_user,login_required, logout_user, current_user,UserMixin
from datetime import datetime

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

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('login'))

@app.route('/login', methods=['POST'])
def log():
    if request.method == 'POST':
        rfc = request.form['txtCorreo']
        password = request.form['txtContra']

        cursor = mysql.connection.cursor()
        query = 'SELECT id, correo, contra, id_estatus,nombre FROM Personas WHERE correo = %s and contra = %s'
        cursor.execute(query, (rfc, password))
        persona = cursor.fetchone()
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
    
@app.route('/guardar',methods=['GET','POST'])
def registro():
    if request.method == 'POST':
        cs= mysql.connection.cursor()
        vNombre = request.form['txtNombre_guardar']
        vApellido_paterno=request.form['txtApellidoPaterno_guardar']
        vApellido_materno=request.form['txtApellidoMaterno_guardar']
        vGenero=request.form['txtGenero']
        vFechaNac=request.form['txtFechaNac']
        vTelefono=request.form['txtTelefono']
        vCorreo=request.form['txtCorreoElectronico_guardar']
        vContra=request.form['txtContrasena_guardar']    
        cs.execute('insert into Personas(nombre,ap,am,id_genero,fecha_nac,telefono,id_estatus,correo,contra) values(%s,%s,%s,%s,%s,%s,3,%s,%s)',
        (vNombre,vApellido_paterno,vApellido_materno,vGenero,vFechaNac,vTelefono,vCorreo,vContra))
        mysql.connection.commit()
    flash('El registro fue agregado correctamente')
    return redirect(url_for('login'))

@app.route('/indexU')
def indexU():
    return render_template('user.html')

@app.route('/indexM')
def indexM():
    return render_template('medico.html')

@app.route('/historicoreg')
def historicoreg():
    return render_template('historicoreg.html')

@app.route('/indexA')
def indexA():
    return render_template('admin.html')


@app.route('/admmed')
def medicaadm():
    cs = mysql.connection.cursor()
    cs.execute('select p.id, p.nombre, p.ap, p.am, g.descripcion, p.fecha_nac, p.telefono, p.correo, p.contra from personas p inner join generos g on p.id_genero = g.id where id_estatus=1')
    medico = cs.fetchall()
    return render_template('addmed.html', listmedico = medico)

@app.route('/citas')
def citas():
    if current_user:
        id_paciente = current_user.id
    
    cs = mysql.connection.cursor()
    cs.execute('select Pacientes.id from Pacientes inner join Personas on Personas.id = Pacientes.id_persona where Personas.id = '+str(id_paciente))
    var = cs.fetchone()

    cs.execute('select c.folio, p.nombre,p.ap, p.am, c.id_consultorio, c.fecha_agendada, c.hora_cita from citas c inner join medicos m on c.id_doctor = m.id inner join personas p on m.id_persona = p.id where c.estatus = 1 and c.id_paciente =%s',(var))
    queryCitas = cs.fetchall()
    cs.execute('select c.folio, p.nombre,p.ap, p.am, c.id_consultorio, c.fecha_agendada, c.hora_cita from citas c inner join medicos m on c.id_doctor = m.id inner join personas p on m.id_persona = p.id where c.estatus = 0 and c.id_paciente =%s',(var))
    queryCitas0 = cs.fetchall()
    return render_template('citas.html', listCitas = queryCitas, listCitas0 = queryCitas0)

@app.route('/consultas')
def consultas():
    if current_user:
        id_paciente = current_user.id
    consulta= mysql.connect.cursor()
    consulta.execute('select Pacientes.id from Pacientes inner join Personas on Personas.id = Pacientes.id_persona where Personas.id = '+str(id_paciente))
    var = consulta.fetchone()
    consulta.execute('select c.id, p.nombre,p.ap,p.am, c.id, c.fecha_consulta, c.Hora from consultas c inner join medicos m on c.id_doctor = m.id inner join personas p on m.id_persona = p.id where c.estatus = 1 and c.id_paciente =%s',(var))
    conCon= consulta.fetchall()
    #print(conAlbums)
    consulta.execute('select c.id, p.nombre,p.ap,p.am, c.id, c.fecha_consulta, c.Hora from consultas c inner join medicos m on c.id_doctor = m.id inner join personas p on m.id_persona = p.id where c.estatus = 0 and c.id_paciente =%s',(var))
    ConCon1= consulta.fetchall()
    return render_template('consultas.html',lsConsulta = conCon,lsCon = ConCon1)



@app.route('/perfil')
def perfil():
    id_paciente = current_user.id
    cs = mysql.connection.cursor()
    cs.execute('SELECT nombre,ap,am, TIMESTAMPDIFF(YEAR, fecha_nac, CURDATE()), correo FROM personas WHERE id= %s', (id_paciente,))
    queryUsr = cs.fetchall()
    return render_template('Uperfil.html', listUsr=queryUsr)




@app.route('/nuevaconsulta')
def nuevaconsulta():
    return render_template('nuevaconsulta.html')

@app.route('/nuevaconsultaBD',methods=['GET','POST'])
def nuevaconsultaBD():
    if current_user:
        id_paciente = current_user.id
    
    if request.method == 'POST':
        cs= mysql.connection.cursor()
        vFecha = request.form['fecha']
        vHora=request.form['hora']
        vSintomas=request.form['sintomas']
        vAlergias=request.form['alergias']
        vAntecedentes=request.form['antecedentes']
        vTipoDolor=request.form['tipodolor']
        vNivelDolor=request.form['niveldolor']    
        vZona=request.form['zona']
        cs.execute('insert into Consultas(id_paciente,id_zona,sintomas,tipo_dolor,nivel_dolor,fecha_consulta,alergias,antecedentes,Hora,estatus) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,1)',
        (id_paciente,vZona,vSintomas,vTipoDolor,vNivelDolor,vFecha,vAlergias,vAntecedentes,vHora))
        mysql.connection.commit()
    flash('El registro fue agregado correctamente')
    return redirect(url_for('nuevaconsulta'))
    


@app.route('/guardar')
def guardar():
    return render_template('nuevaconsulta.html')



#Ejecucion del Servidor en el puerto 5000
if __name__ == '__main__':
    app.run(port=5000, debug=True)