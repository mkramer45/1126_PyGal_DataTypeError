from flask import *
from functools import wraps
import sqlite3
from flask_bootstrap import Bootstrap
from wtforms import StringField, PasswordField, BooleanField
from wtforms.validators import InputRequired, Email, Length
from flask_wtf import FlaskForm
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from flask_sqlalchemy  import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from flask_wtf import FlaskForm, CsrfProtect
import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
import pygal


app = Flask(__name__)
app.secret_key = 'my precious'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///C:\Users\Mike\Desktop\PythonSuccess\Beatscrape.db'
bootstrap = Bootstrap(app)
db = SQLAlchemy(app)
app.config.from_object(__name__)
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'
csrf = CsrfProtect(app)





class LoginForm(FlaskForm):
	username = StringField('username', validators=[InputRequired(), Length(min=4, max=15)])
	password = PasswordField('password', validators=[InputRequired(), Length(min=8, max=80)])
	remember = BooleanField('remember me')


class RegisterForm(FlaskForm):
	email = StringField('email', validators=[InputRequired(), Email(message='Invalid email'), Length(max=50)])
	username = StringField('username', validators=[InputRequired(), Length(min=4, max=15)])
	password = PasswordField('password', validators=[InputRequired(), Length(min=8, max=80)])


class User(UserMixin, db.Model):
	id = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.String(15), unique=True)
	email = db.Column(db.String(50), unique=True)
	password = db.Column(db.String(80))

@login_manager.user_loader
def load_user(id):
    return User.query.get(int(id))


   
def connect_db():
	return sqlite3.connect(app.config['DATABASE'])

def connect_db2():
	return sqlite3.connect(app.config['SurfSend'])

@app.route('/')  
def home():
	return render_template('home.html')

@app.route('/welcome')
def welcome():
	return render_template('welcome.html')


#-------------------------- RHODE ISLAND BEACHES--------------------------------
@app.route('/TwoBeach')
@csrf.exempt
def TwoBeach():
	conn = sqlite3.connect('SurfSend.db')
	cursor = conn.cursor()
	cursor.execute("select SwellSizeFt, SwellIntervalSec, WindMPH, WindDescription, AirTemp, beach_name, date_, time_, state from SurfMaster2 where beach_name = '2nd Beach' order by SurfMaster2.beach_name ASC, SurfMaster2.date_ ASC")
	info1 = [dict(SwellSize=row[0], SwellInterval=row[1], WindSpeed=row[2], WindDescription=row[3], AirTemperature=row[4], Beach=row[5], Day=row[6], Tiempo=row[7], St8=row[8]) for row in cursor.fetchall()]
	cursor.close()
	return render_template('TwoBeach.html', selected='submit', info1=info1)


@app.route('/Narragansett')
@csrf.exempt
def Narragansett():
	conn = sqlite3.connect('SurfSend.db')
	cursor = conn.cursor()
	cursor.execute("select SwellSizeFt, SwellIntervalSec, WindMPH, WindDescription, AirTemp, beach_name, date_, time_, state from SurfMaster2 where beach_name = 'Narragansett' order by SurfMaster2.beach_name ASC, SurfMaster2.date_ ASC")
	info1 = [dict(SwellSize=row[0], SwellInterval=row[1], WindSpeed=row[2], WindDescription=row[3], AirTemperature=row[4], Beach=row[5], Day=row[6], Tiempo=row[7], St8=row[8]) for row in cursor.fetchall()]
	cursor.close()
	return render_template('Narragansett.html', selected='submit', info1=info1)



@app.route('/Ruggles')
@csrf.exempt
def Ruggles():
	conn = sqlite3.connect('SurfSend.db')
	cursor = conn.cursor()
	cursor.execute("select SwellSizeFt, SwellIntervalSec, WindMPH, WindDescription, AirTemp, beach_name, date_, time_, state from SurfMaster2 where beach_name = 'Ruggles' order by SurfMaster2.beach_name ASC, SurfMaster2.date_ ASC")
	info1 = [dict(SwellSize=row[0], SwellInterval=row[1], WindSpeed=row[2], WindDescription=row[3], AirTemperature=row[4], Beach=row[5], Day=row[6], Tiempo=row[7], St8=row[8]) for row in cursor.fetchall()]
	cursor.close()
	return render_template('Ruggles.html', selected='submit', info1=info1)



#--------------------------MA BEACHES--------------------------------




@app.route('/Nahant')
@csrf.exempt
def Nahant():
	#code attempting to merge from app.py
	graph = pygal.Line()
	graph.title = '% Change Coolness of programming languages over time.'
	graph.x_labels = ['2011','2012','2013','2014','2015','2016']
	graph.add('Python',  [15, 31, 89, 200, 356, 900])
	graph.add('Java',    [15, 45, 76, 80,  91,  95])
	graph.add('C++',     [5,  51, 54, 102, 150, 201])
	graph.add('All others combined!',  [5, 15, 21, 55, 92, 105])
	graph_data = graph.render_data_uri()
	#original code, used for creating table in Nahant.html
	conn = sqlite3.connect('SurfSend.db')
	cursor = conn.cursor()
	cursor.execute("select SwellSizeFt, SwellIntervalSec, WindMPH, WindDescription, AirTemp, beach_name, date_, time_, state from SurfMaster2 where beach_name = 'Nahant' order by SurfMaster2.beach_name ASC, SurfMaster2.date_ ASC")
	info1 = [dict(SwellSize=row[0], SwellInterval=row[1], WindSpeed=row[2], WindDescription=row[3], AirTemperature=row[4], Beach=row[5], Day=row[6], Tiempo=row[7], St8=row[8]) for row in cursor.fetchall()]
	cursor.close()
	return render_template('Nahant.html', selected='submit', info1=info1, graph_data=graph_data)


@app.route('/Nantasket')
@csrf.exempt
def Nantasket():
	conn = sqlite3.connect('SurfSend.db')
	cursor = conn.cursor()
	cursor.execute("select SwellSizeFt, SwellIntervalSec, WindMPH, WindDescription, AirTemp, beach_name, date_, time_, state from SurfMaster2 where beach_name = 'Nantasket' order by SurfMaster2.beach_name ASC, SurfMaster2.date_ ASC")
	info1 = [dict(SwellSize=row[0], SwellInterval=row[1], WindSpeed=row[2], WindDescription=row[3], AirTemperature=row[4], Beach=row[5], Day=row[6], Tiempo=row[7], St8=row[8]) for row in cursor.fetchall()]
	cursor.close()
	return render_template('Nantasket.html', selected='submit', info1=info1)


@app.route('/Scituate')
@csrf.exempt
def Scituate():
	conn = sqlite3.connect('SurfSend.db')
	cursor = conn.cursor()
	cursor.execute("select SwellSizeFt, SwellIntervalSec, WindMPH, WindDescription, AirTemp, beach_name, date_, time_, state from SurfMaster2 where beach_name = 'Scituate' order by SurfMaster2.beach_name ASC, SurfMaster2.date_ ASC")
	info1 = [dict(SwellSize=row[0], SwellInterval=row[1], WindSpeed=row[2], WindDescription=row[3], AirTemperature=row[4], Beach=row[5], Day=row[6], Tiempo=row[7], St8=row[8]) for row in cursor.fetchall()]
	cursor.close()
	return render_template('Scituate.html', selected='submit', info1=info1)


@app.route('/CapeCod')
@csrf.exempt
def CapeCod():
	conn = sqlite3.connect('SurfSend.db')
	cursor = conn.cursor()
	cursor.execute("select SwellSizeFt, SwellIntervalSec, WindMPH, WindDescription, AirTemp, beach_name, date_, time_, state from SurfMaster2 where beach_name = 'Cape Cod' order by SurfMaster2.beach_name ASC, SurfMaster2.date_ ASC")
	info1 = [dict(SwellSize=row[0], SwellInterval=row[1], WindSpeed=row[2], WindDescription=row[3], AirTemperature=row[4], Beach=row[5], Day=row[6], Tiempo=row[7], St8=row[8]) for row in cursor.fetchall()]
	cursor.close()
	return render_template('CapeCod.html', selected='submit', info1=info1)


@app.route('/GreenHarbor')
@csrf.exempt
def GreenHarbor():
	conn = sqlite3.connect('SurfSend.db')
	cursor = conn.cursor()
	cursor.execute("select SwellSizeFt, SwellIntervalSec, WindMPH, WindDescription, AirTemp, beach_name, date_, time_, state from SurfMaster2 where beach_name = 'Green Harbor' order by SurfMaster2.beach_name ASC, SurfMaster2.date_ ASC")
	info1 = [dict(SwellSize=row[0], SwellInterval=row[1], WindSpeed=row[2], WindDescription=row[3], AirTemperature=row[4], Beach=row[5], Day=row[6], Tiempo=row[7], St8=row[8]) for row in cursor.fetchall()]
	cursor.close()
	return render_template('GreenHarbor.html', selected='submit', info1=info1)

@app.route('/CapeAnn')
@csrf.exempt
def CapeAnn():
	conn = sqlite3.connect('SurfSend.db')
	cursor = conn.cursor()
	cursor.execute("select SwellSizeFt, SwellIntervalSec, WindMPH, WindDescription, AirTemp, beach_name, date_, time_, state from SurfMaster2 where beach_name = 'Cape Ann' order by SurfMaster2.beach_name ASC, SurfMaster2.date_ ASC")
	info1 = [dict(SwellSize=row[0], SwellInterval=row[1], WindSpeed=row[2], WindDescription=row[3], AirTemperature=row[4], Beach=row[5], Day=row[6], Tiempo=row[7], St8=row[8]) for row in cursor.fetchall()]
	cursor.close()
	return render_template('CapeAnn.html', selected='submit', info1=info1)


@app.route('/Devereux')
@csrf.exempt
def Devereux():
	conn = sqlite3.connect('SurfSend.db')
	cursor = conn.cursor()
	cursor.execute("select SwellSizeFt, SwellIntervalSec, WindMPH, WindDescription, AirTemp, beach_name, date_, time_, state from SurfMaster2 where beach_name = 'Devereux Beach' order by SurfMaster2.beach_name ASC, SurfMaster2.date_ ASC")
	info1 = [dict(SwellSize=row[0], SwellInterval=row[1], WindSpeed=row[2], WindDescription=row[3], AirTemperature=row[4], Beach=row[5], Day=row[6], Tiempo=row[7], St8=row[8]) for row in cursor.fetchall()]
	cursor.close()
	return render_template('Devereux.html', selected='submit', info1=info1)


@app.route('/Salisbury')
@csrf.exempt
def Salisbury():
	conn = sqlite3.connect('SurfSend.db')
	cursor = conn.cursor()
	cursor.execute("select SwellSizeFt, SwellIntervalSec, WindMPH, WindDescription, AirTemp, beach_name, date_, time_, state from SurfMaster2 where beach_name = 'Salisbury' order by SurfMaster2.beach_name ASC, SurfMaster2.date_ ASC")
	info1 = [dict(SwellSize=row[0], SwellInterval=row[1], WindSpeed=row[2], WindDescription=row[3], AirTemperature=row[4], Beach=row[5], Day=row[6], Tiempo=row[7], St8=row[8]) for row in cursor.fetchall()]
	cursor.close()
	return render_template('Salisbury.html', selected='submit', info1=info1)


#--------------------------NH BEACHES--------------------------------

@app.route('/Rye')
@csrf.exempt
def Rye():
	conn = sqlite3.connect('SurfSend.db')
	cursor = conn.cursor()
	cursor.execute("select SwellSizeFt, SwellIntervalSec, WindMPH, WindDescription, AirTemp, beach_name, date_, time_, state from SurfMaster2 where beach_name = 'Rye' order by SurfMaster2.beach_name ASC, SurfMaster2.date_ ASC")
	info1 = [dict(SwellSize=row[0], SwellInterval=row[1], WindSpeed=row[2], WindDescription=row[3], AirTemperature=row[4], Beach=row[5], Day=row[6], Tiempo=row[7], St8=row[8]) for row in cursor.fetchall()]
	cursor.close()
	return render_template('Rye.html', selected='submit', info1=info1)

@app.route('/Hampton')
@csrf.exempt
def Hampton():
	conn = sqlite3.connect('SurfSend.db')
	cursor = conn.cursor()
	cursor.execute("select SwellSizeFt, SwellIntervalSec, WindMPH, WindDescription, AirTemp, beach_name, date_, time_, state from SurfMaster2 where beach_name = 'Hampton' order by SurfMaster2.beach_name ASC, SurfMaster2.date_ ASC")
	info1 = [dict(SwellSize=row[0], SwellInterval=row[1], WindSpeed=row[2], WindDescription=row[3], AirTemperature=row[4], Beach=row[5], Day=row[6], Tiempo=row[7], St8=row[8]) for row in cursor.fetchall()]
	cursor.close()
	return render_template('Hampton.html', selected='submit', info1=info1)


@app.route('/Seabrook')
@csrf.exempt
def Seabrook():
	conn = sqlite3.connect('SurfSend.db')
	cursor = conn.cursor()
	cursor.execute("select SwellSizeFt, SwellIntervalSec, WindMPH, WindDescription, AirTemp, beach_name, date_, time_, state from SurfMaster2 where beach_name = 'Seabrook' order by SurfMaster2.beach_name ASC, SurfMaster2.date_ ASC")
	info1 = [dict(SwellSize=row[0], SwellInterval=row[1], WindSpeed=row[2], WindDescription=row[3], AirTemperature=row[4], Beach=row[5], Day=row[6], Tiempo=row[7], St8=row[8]) for row in cursor.fetchall()]
	cursor.close()
	return render_template('Seabrook.html', selected='submit', info1=info1)

@app.route('/NHSeacoast')
@csrf.exempt
def NHSeacoast():
	conn = sqlite3.connect('SurfSend.db')
	cursor = conn.cursor()
	cursor.execute("select SwellSizeFt, SwellIntervalSec, WindMPH, WindDescription, AirTemp, beach_name, date_, time_, state from SurfMaster2 where beach_name = 'NH Seacoast' order by SurfMaster2.beach_name ASC, SurfMaster2.date_ ASC")
	info1 = [dict(SwellSize=row[0], SwellInterval=row[1], WindSpeed=row[2], WindDescription=row[3], AirTemperature=row[4], Beach=row[5], Day=row[6], Tiempo=row[7], St8=row[8]) for row in cursor.fetchall()]
	cursor.close()
	return render_template('NHSeacoast.html', selected='submit', info1=info1)


@app.route('/Plymouth')
@csrf.exempt
def Plymouth():
	conn = sqlite3.connect('SurfSend.db')
	cursor = conn.cursor()
	cursor.execute("select SwellSizeFt, SwellIntervalSec, WindMPH, WindDescription, AirTemp, beach_name, date_, time_, state from SurfMaster2 where beach_name = 'Plymouth' order by SurfMaster2.beach_name ASC, SurfMaster2.date_ ASC")
	info1 = [dict(SwellSize=row[0], SwellInterval=row[1], WindSpeed=row[2], WindDescription=row[3], AirTemperature=row[4], Beach=row[5], Day=row[6], Tiempo=row[7], St8=row[8]) for row in cursor.fetchall()]
	cursor.close()
	return render_template('Plymouth.html', selected='submit', info1=info1)


	

@app.route('/register', methods=['GET', 'POST'])
def register():
	form = RegisterForm()
	if form.validate_on_submit():
		conn = sqlite3.connect('Beatscrape.db')
		cursor = conn.cursor()
		hashed_password = generate_password_hash(form.password.data, method='sha256')
		new_user = User(username=form.username.data, email=form.email.data, password=hashed_password)
		posts = [dict(username=row[0], email=row[1], password=row[2]) for row in cursor.fetchall()]
#        usr = User(username=form.username.data, email=form.email.data, password=hashed_password)
		usrname = form.username.data
		emailname = form.email.data
		pw = password=hashed_password
		cursor.execute("INSERT INTO users VALUES (NULL,?,?,?)", (usrname,emailname,pw,))
		conn.commit()
		cursor.close()
		conn.close()
		flash('User Created')
		#return '<h1>' + form.username.data + ' ' + form.email.data + ' ' + form.password.data + '</h1>'

	return render_template('register.html', form=form)


@app.route('/youtube', methods=['GET', 'POST'])
@csrf.exempt
def youtube():
	if request.method == 'POST':
		URL = request.form['URL']
		TimeMM = request.form['TimeMM']
		TimeSS = request.form['TimeSS']
		scl = '&t='
		m = 'm'
		s = 's'
		appendx = "".join((URL, scl, TimeMM, m, TimeSS, s))

		return render_template('youtube.html', URL=URL, TimeMM=TimeMM, TimeSS=TimeSS, scl=scl, appendx=appendx)
	return render_template('youtube.html')


@app.route('/soundcloud', methods=['GET', 'POST'])
@csrf.exempt
def soundcloud():
	if request.method == 'POST':
		URL_sc = request.form['URL']
		Time_sc = request.form['Time']
		scl_sc = '#t='
		appendx_sc = "".join((URL_sc, scl_sc, Time_sc))

		return render_template('soundcloud.html', URL_sc=URL_sc, Time_sc=Time_sc, scl_sc=scl_sc, appendx_sc=appendx_sc)
	return render_template('soundcloud.html')


@app.route('/sendr', methods=['GET', 'POST'])
@csrf.exempt
def sendr():
	if request.method == 'POST':
		global feed
		conn = sqlite3.connect("C:\\Users\\Mike\Desktop\\PythonSuccess\\StriveDB2.db")
		cursor = conn.cursor()
		posts = [dict(URL_sc=row[0], Time_sc=row[1] ) for row in cursor.fetchall()]
		# FirstName
		FN = request.form['FirstName']
		# Email
		EM = request.form['Email']
		# Radio Button Value
		Radio_sc = request.form['options']
		cursor.execute("INSERT INTO Sendr_Usr VALUES (?,?,?)", (EM,FN,Radio_sc,))
		conn.commit()
		cursor.close()
		conn.close()

		hello = request.form['Email']

		msg = MIMEMultipart()
		msg['From'] = 'Sendr'
		msg['To'] = 'mkramer789@gmail.com'
		msg['Subject'] = 'Sendr Registration Confirmation'
		mes = 'Welcome to Sendr! Thanks for signing up :-)'
		msg.attach(MIMEText(mes))

		mailserver = smtplib.SMTP('smtp.gmail.com',587)
		# identify ourselves to smtp gmail client
		mailserver.ehlo()
		# secure our email with tls encryption
		mailserver.starttls()
		# re-identify ourselves as an encrypted connection
		mailserver.ehlo()
		mailserver.login('mkramer265@gmail.com', 'Celtics123')

		mailserver.sendmail('mkramer265@gmail.com',hello,msg.as_string())

		mailserver.quit()

		flash('Sendr Registration Successful!')


		scl_sc = '#t='
		appendx_sc = "".join((FN, scl_sc, EM))

		return render_template('sendr.html', FN=FN, EM=EM, scl_sc=scl_sc, appendx_sc=appendx_sc)
	return render_template('sendr.html')


@app.route('/exit', methods=['GET', 'POST'])
@csrf.exempt
def exit():
	if request.method == 'POST':
		global feed
		conn = sqlite3.connect('StriveDB2.db')
		cursor = conn.cursor()
		posts = [dict(URL_sc=row[0], Time_sc=row[1] ) for row in cursor.fetchall()]
		# Email
		EM = request.form['EmailX']
		cursor.execute("DELETE FROM Sendr_Usr WHERE email = (?)", (EM,))
		conn.commit()
		cursor.close()
		conn.close()

		return render_template('exit.html', EM=EM)
	return render_template('exit.html')




@app.route('/log', methods=['GET', 'POST'])
@csrf.exempt
def log():
	form = LoginForm()
   
	if form.validate_on_submit():
		username_form  = request.form['username']
		g.db = connect_db()
		user = g.db.execute("SELECT COUNT(1) FROM users WHERE username = (?)", (username_form,))
		# if not user.fetchone()[0]:
		# 	return '<h1>Invalid username or password</h1>'
		if user.fetchone()[0]:
			# if check_password_hash(user.password, form.password.data):
			# 	login_user(user, remember=form.remember.data)
			return redirect(url_for('scrapelist2'))
		else:

			return '<h1>Invalid username or password</h1>'
		#return '<h1>' + form.username.data + ' ' + form.password.data + '</h1>'

	return render_template('log.html', form=form)
	
	

# 11/14 ... updated scrapelist2 in attempts to get the user input to be saved in ArtistMonitor table
@app.route('/scrapelist2', methods=['GET', 'POST'])
@csrf.exempt
def scrapelist2():
	if request.method == 'POST':
		global feed
		conn = sqlite3.connect('Beatscrape.db')
		cursor = conn.cursor()
		posts = [dict(DJname=row[0]) for row in cursor.fetchall()]
		DJname = request.form['Producername']
		cursor.execute("INSERT INTO ArtistMonitor VALUES (NULL,?)", (DJname,))
		conn.commit()
		cursor.close()
		conn.close()
		artists.append(request.form['Producername'])
	g.db = connect_db()
	cur = g.db.execute('select DJName from ArtistMonitor')
	cur2 = g.db.execute('select * from Tracks where artist in (select DJname from ArtistMonitor)')
	pull = [dict(DJname=row[0]) for row in cur.fetchall()]
	watch = [dict(Artist=row[0], Song=row[1], Websource=row[2], Genre=row[3]) for row in cur2.fetchall()]
	g.db.close()
	return render_template('scrapelist2.html', selected='submit', pull=pull, watch=watch)



	
@app.route('/delete_artist/<DJName>', methods=['POST'])
def delete_artist(DJName):
	conn = sqlite3.connect('Beatscrape.db')
	cursor = conn.cursor()
	del1 = [dict(id=row[0], DJName=row[1]) for row in cursor.fetchall()]
#	DJName1 = request.args.get('DJName')
	cursor.execute("DELETE FROM ArtistMonitor WHERE DJName = ?", (DJName,))
	conn.commit()
	cursor.close()
	conn.close()
	flash('Artist Deleted')
	return redirect(url_for('scrapelist2', del1=del1))
	
	
def login_required(test):
	@wraps(test)
	def wrap(*args, **kwargs):
		if 'logged_in' in session:
			return test(*args, **kwargs)
		else:
			flash('You need to login first.')
			return redirect(url_for('log'))
	return wrap


@app.route('/logout')
def logout():
	session.pop('logged_in', None)
	flash('You were logged out')
	return redirect (url_for('log'))

@app.route('/hello')
@login_required
def hello():
	g.db = connect_db()
	cur = g.db.execute('select Artist, Song, Label, Price from BeatPortTechHouse')
	info = [dict(Artist=row[0], Song=row[1], Label=row[2], Price=row[3]) for row in cur.fetchall()]
	g.db.close()
	return render_template('hello.html', info=info)




if __name__ == '__main__':
	app.run(debug=True)