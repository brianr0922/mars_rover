from flask import Flask, jsonify, request, redirect, Response, render_template
import requests
from config import api_key, cam_names, rover_det

app = Flask(__name__)

@app.route('/')
def home():
	return render_template("index.html")

@app.route('/rover', methods = ['POST'])
def rover():
	rov_name = request.form['optrover']
	return redirect(f'/{rov_name}.html?emsg=OK')

@app.route('/<rov_name>.html')
def pic_criteria(rov_name):
	err_msg = request.args.get('emsg')
	if err_msg == None:
		err_msg = ""

	rov_det = rover_det[rov_name]
	rov_pic = rov_det["rov_pic"]
	st_date = rov_det["landing_date"]
	end_date = rov_det["max_date"]
	cameras = rov_det["cameras"]

	cam_list = {}
	for cam in cameras:
		cam_list.update({cam:cam_names[cam]})

	return render_template('pic_criteria.html', rname=rov_name, rpic=rov_pic, sdat=st_date, edat=end_date, clist=cam_list, emsg=err_msg)


@app.route('/img_criteria', methods = ['POST'])
def imgcrit():
	rov_name = request.args.get('rov_name')
	form_date = request.form['date']
	form_cam = request.form['optcam']
	return redirect(f'/list.html?rov_name={rov_name}&img_date={form_date}&sel_cam={form_cam}')


@app.route('/list.html')
def img_list():
	rov_name = request.args.get('rov_name')
	img_date = request.args.get('img_date')
	sel_cam = request.args.get('sel_cam')
	img_list = requests.get(f'https://api.nasa.gov/mars-photos/api/v1/rovers/{rov_name}/photos?earth_date={img_date}&camera={sel_cam}&api_key={api_key}')
	if img_list.text == "":
		emsg = 'No images for that camera and date.  Please try again.'
		return redirect(f'/{rov_name}.html?emsg="No images for that camera and date.  Please try again."')
	else:
		img_list = eval(img_list.text)
		img_list = img_list["photos"]
		max_rows = len(img_list)

		rend_list = {}
		for i in range(1, max_rows+1):
			row_cam = img_list[i-1]["camera"]["full_name"]
			row_url = img_list[i-1]["img_src"]
			row_date = img_list[i-1]["earth_date"]
			dictval = {
				"camera":row_cam,
				"img_url":row_url,
				"earth_date":row_date,
				}
			rend_list.update({i:dictval})

		return render_template('list.html', rname=rov_name, ilist=rend_list)


if __name__ == '__main__':
	app.run(debug=True)