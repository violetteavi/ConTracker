from flask import Flask, render_template
from ConTrackerFetcher import getStateData 


states = ["AL", "AK", "AZ", "AR", "CA", "CO", "CT", "DC", "DE", "FL", "GA", 
          "HI", "ID", "IL", "IN", "IA", "KS", "KY", "LA", "ME", "MD", 
          "MA", "MI", "MN", "MS", "MO", "MT", "NE", "NV", "NH", "NJ", 
          "NM", "NY", "NC", "ND", "OH", "OK", "OR", "PA", "RI", "SC", 
          "SD", "TN", "TX", "UT", "VT", "VA", "WA", "WV", "WI", "WY"]

def writeHTMLforStates():

	for state in 'states':
		htmlContent = "";
		(statePercentage,totalContState,DemPercent,RepPercent,OtherPercent) = getStateData(state);
		




app = Flask(__name__)

@app.route("/")
def main():
	return "Hello world"
	#return render_template('index.html')
	#hmtl files need to be insie template 
	#style.css files need to be in static

if __name__ == "__main__":
	app.run(debug=True,host="0.0.0.0",port=80)