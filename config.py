cam_names = {
	"FHAZ": "Front Hazard Avoidance Camera",
	"RHAZ":"Rear Hazard Avoidance Camera",
	"MAST":"Mast Camera",
	"CHEMCAM":"Chemistry and Camera Complex",
	"MAHLI":"Mars Hand Lens Imager",
	"MARDI":"Mars Descent Imager",
	"NAVCAM":"Navigation Camera",
	"PANCAM":"Panoramic Camera",
	"MINITES":"Miniature Thermal Emission Spectrometer (Mini-Tes)",
	}

rover_det = {
	"Curiosity": {
		"landing_date":"2012-08-06",
		"max_date":"2020-06-19",
		"cameras": ["FHAZ", "RHAZ", "MAST", "CHEMCAM", "MAHLI", "MARDI", "NAVCAM"],
	},
	"Opportunity": {
		"landing_date":"2004-01-25",
		"max_date":"2018-06-11",
		"cameras": ["FHAZ", "RHAZ", "NAVCAM", "PANCAM", "MINITES"],
	}
	"Spirit": {
		"landing_date":"2004-01-04",
		"max_date":"2010-03-21",
		"cameras": ["FHAZ", "RHAZ", "NAVCAM", "PANCAM", "MINITES"],
	}
	}
}