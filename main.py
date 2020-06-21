from flask import Flask, jsonify, request, redirect, Response, render_template
app = Flask(__name__)

@app.route('/')
def home():
	return render_template("index.html")

@app.route('/rover', methods = ['POST'])
def rover():
	rov_name = request.form['optrover']
#	if request.form['optrover'] == 'on':
#		rov_name = 'Curiosity'
#	elif request.form['optopp'] == 'on':
#		rov_name = 'Opportunity'
#	else:
#		rov_name = 'Spirit'
	print("Selected rover: " + rov_name)
	print(type(rov_name))
	return redirect('/')

if __name__ == '__main__':
	app.run(debug=True)