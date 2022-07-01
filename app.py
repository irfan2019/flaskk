from flask import Flask,render_template,url_for
from forms import registrationform,loginform

app=Flask(__name__)
app.config['SECRET_KEY']='0f4a6e936d64aadde69d5ca764719f9a'


posts=[{
	'id':'5 ',
	'name':'irfan',
	'age':'21'
}
]



@app.route('/')
@app.route('/homee')
def homee():
	return "primary page"

@app.route('/home')
def home():
	return render_template('home.html',posts=posts)

@app.route('/about')
def about():
	return render_template('about.html',title='irfanpage')


@app.route('/register')
def registerr():
	form=registrationform()
	return render_template('register.html',title='Register',form=form)

@app.route('/login')
def login():
	form=loginform()
	return render_template('login.html',title='Login',form=form)





if __name__=="__main__":
	app.run(debug=True)