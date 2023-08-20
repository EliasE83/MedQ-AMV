#Importar el framework
from flask import Flask, render_template, request, redirect, url_for, flash, send_file, Response
from flask_mysqldb import MySQL
from flask_login import LoginManager, login_user,login_required, logout_user, current_user,UserMixin
from datetime import datetime
from flask_login import LoginManager, login_required, login_user, logout_user
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Flowable, PageBreak
from reportlab.lib.styles import getSampleStyleSheet
from io import BytesIO
from xhtml2pdf import pisa
import openai



openai.api_key = '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'

def get_completion(prompt, model="gpt-3.5-turbo"):
    messages = [{"role": "user", "content": prompt}]
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=0,
    )
    return response.choices[0].message["content"]




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
    cursor.execute('SELECT Pacientes.id, Personas.correo, Personas.contra, Personas.id_estatus, Personas.nombre FROM Personas inner join Pacientes on Pacientes.id_persona = Personas.id WHERE Pacientes.id = %s', (id,))
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
        query = 'SELECT Pacientes.id, Personas.correo, Personas.contra, Personas.id_estatus,Personas.nombre FROM Personas inner join Pacientes on Pacientes.id_persona = Personas.id WHERE Personas.correo = %s and Personas.contra = %s'
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
    return render_template('med.html')

@app.route('/historicoreg')
def historicoreg():
    return render_template('historicoreg.html')

@app.route('/indexA')
def usuarios():
    return render_template('usuarios.html')

@app.route('/citas')
def citas():
    if current_user:
        id_paciente = current_user.id
    
    cs = mysql.connection.cursor()
    cs.execute('select c.folio, p.nombre,p.ap, p.am, c.id_consultorio, c.fecha_agendada, c.hora_cita from citas c inner join medicos m on c.id_doctor = m.id inner join personas p on m.id_persona = p.id where c.estatus = 1 and c.id_paciente ='+str(id_paciente))
    queryCitas = cs.fetchall()
    cs.execute('select c.folio, p.nombre,p.ap, p.am, c.id_consultorio, c.fecha_agendada, c.hora_cita from citas c inner join medicos m on c.id_doctor = m.id inner join personas p on m.id_persona = p.id where c.estatus = 0 and c.id_paciente ='+str(id_paciente))
    queryCitas0 = cs.fetchall()
    return render_template('citas.html', listCitas = queryCitas, listCitas0 = queryCitas0)

@app.route('/consultas')
def consultas():
    if current_user:
        id_paciente = current_user.id
    consulta= mysql.connect.cursor()
    consulta.execute('select c.id, p.nombre,p.ap,p.am, c.id, c.fecha_consulta, c.Hora from consultas c inner join medicos m on c.id_doctor = m.id inner join personas p on m.id_persona = p.id where c.estatus = 1 and c.id_paciente ='+str(id_paciente))
    conCon= consulta.fetchall()
    #print(conAlbums)
    consulta.execute('select c.id, p.nombre,p.ap,p.am, c.id, c.fecha_consulta, c.Hora from consultas c inner join medicos m on c.id_doctor = m.id inner join personas p on m.id_persona = p.id where c.estatus = 0 and c.id_paciente ='+str(id_paciente))
    ConCon1= consulta.fetchall()
    return render_template('consultas.html',lsConsulta = conCon,lsCon = ConCon1)



@app.route('/perfil')
def perfil():
    id_paciente = current_user.id
    cs = mysql.connection.cursor()
    cs.execute('SELECT p.nombre,p.ap,p.am, TIMESTAMPDIFF(YEAR, p.fecha_nac, CURDATE()), p.correo FROM personas p INNER JOIN pacientes pa on pa.id_persona = p.id WHERE pa.id= %s', (id_paciente,))
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

        cs.execute('select descripcion from zonacuerpos where id = %s;', (vZona,))
        vZonaC = cs.fetchone()


        prompt = "Imagina que eres un medico, es importante que NO me recalques que no eres un medico a la hora de darme tu respuesta, tengo los siguientes sintomas: "+vSintomas+" tengo un dolor "+vTipoDolor+" en la zona "+vZonaC[0]+" y mi nivel de dolor es "+vNivelDolor+" de 10, tengo las siguientes alergias: "+vAlergias+" y mis antecedentes son: "+vAntecedentes+" ¿Que me recomiendas?. Reitero, porfavor no me recalques que no eres un medico real, solo quiero que me des una respuesta como si fueras un medico real."
        response = get_completion(prompt)
        print(response) 

        cs.execute('insert into Consultas(id_paciente,id_zona,sintomas,tipo_dolor,nivel_dolor,fecha_consulta,alergias,antecedentes,Hora,estatus, diagnostico) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,1,%s)',
        (id_paciente,vZona,vSintomas,vTipoDolor,vNivelDolor,vFecha,vAlergias,vAntecedentes,vHora,response))
        mysql.connection.commit()

        


    cur = mysql.connection.cursor()
    cur.execute('select personas.nombre, personas.ap,personas.am,zonacuerpos.descripcion, sintomas, tipo_dolor, alergias, antecedentes, fecha_consulta, Hora from consultas inner join pacientes on pacientes.id = consultas.id_paciente inner join personas on pacientes.id_persona = personas.id inner join zonacuerpos on zonacuerpos.id = consultas.id_zona where consultas.id = %s;', (id_paciente,))
    data = cur.fetchall()
    cur.close()

    #return render_template('Medico/receta.html', pacientes = data)

    html_content = render_template('receta.html', pacientes=data, respuesta=response)

    response = Response(content_type='application/pdf')
    response.headers['Content-Disposition'] = 'inline; filename=receta.pdf'

    buffer = BytesIO()

    doc = SimpleDocTemplate(buffer, pagesize=letter)
    story = []

    # Convertir el HTML a PDF utilizando xhtml2pdf
    result = pisa.CreatePDF(html_content, dest=buffer)

    if not result.err:
        pdf_data = buffer.getvalue()
        buffer.close()

        response.data = pdf_data
        return response
    else:
        buffer.close()
        return "Error generando el PDF"
""" 
    flash('El registro fue agregado correctamente')
    return redirect(url_for('nuevaconsulta'))
     """


@app.route('/guardar')
def guardar():
    return render_template('nuevaconsulta.html')

@app.route('/reimprimir/<id>')
def reimprimir(id):
    if current_user:
        id_paciente = current_user.id

    cur = mysql.connection.cursor()
    cur.execute('select personas.nombre, personas.ap,personas.am,zonacuerpos.descripcion, sintomas, tipo_dolor, alergias, antecedentes, fecha_consulta, Hora from consultas inner join pacientes on pacientes.id = consultas.id_paciente inner join personas on pacientes.id_persona = personas.id inner join zonacuerpos on zonacuerpos.id = consultas.id_zona where consultas.id = %s;', (id,))
    data = cur.fetchall()
    cur.execute('select diagnostico from consultas where id = %s;', (id,))
    data2 = cur.fetchone()

    #return render_template('Medico/receta.html', pacientes = data)

    html_content = render_template('receta.html', pacientes=data, respuesta=data2[0])

    response = Response(content_type='application/pdf')
    response.headers['Content-Disposition'] = 'inline; filename=receta.pdf'

    buffer = BytesIO()

    doc = SimpleDocTemplate(buffer, pagesize=letter)
    story = []

    # Convertir el HTML a PDF utilizando xhtml2pdf
    result = pisa.CreatePDF(html_content, dest=buffer)

    if not result.err:
        pdf_data = buffer.getvalue()
        buffer.close()

        response.data = pdf_data
        return response
    else:
        buffer.close()
        return "Error generando el PDF"    



#Ejecucion del Servidor en el puerto 5000
if __name__ == '__main__':
    app.run(port=5000, debug=True)