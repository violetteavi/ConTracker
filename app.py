from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def main():
	return "Hello world"
	#return render_template('index.html')
	#hmtl files need to be insie template 
	#style.css files need to be in static

if __name__ == "__main__":
	app.run(debug=True,host="0.0.0.0",port=80)