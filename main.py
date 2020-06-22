from flask import Flask, jsonify, request, redirect, Response, render_template
app = Flask(__name__)

@app.route('/')
def home():
	return render_template("index.html")

@app.route('/rover', methods = ['POST'])
def rover():
	rov_name = request.form['optrover']
	print("Selected rover: " + rov_name)
	print(type(rov_name))
	return redirect('/<rov_name>.html')

@app.route('/<rov_name>.html')
def pic_criteria(rov_name):
	return render_template('pic_criteria.html', data=rov_name)

if __name__ == '__main__':
	app.run(debug=True)