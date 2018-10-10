from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index ():
	return 'Index'

@app.route('/<argument>')
def template_example(argument):

	return render_template('example.html', argument=argument)
