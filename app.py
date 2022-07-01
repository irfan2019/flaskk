from flask import Flask,render_template,url_for
app=Flask(__name__)


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

if __name__=="__main__":
	app.run(debug=True)