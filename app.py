from flask import Flask, render_template
from ConTrackerFetcher import getStateData 
from ConTrackerHtmlGen import generatePieHtmlBegin
from ConTrackerHtmlGen import generatePieHtmlDataStr
from ConTrackerHtmlGen import generatePieHtmlEnd

states = ["AL", "AK", "AZ", "AR", "CA", "CO", "CT", "DC", "DE", "FL", "GA", 
          "HI", "ID", "IL", "IN", "IA", "KS", "KY", "LA", "ME", "MD", 
          "MA", "MI", "MN", "MS", "MO", "MT", "NE", "NV", "NH", "NJ", 
          "NM", "NY", "NC", "ND", "OH", "OK", "OR", "PA", "RI", "SC", 
          "SD", "TN", "TX", "UT", "VT", "VA", "WA", "WV", "WI", "WY"]

def writeHTMLforStates():

	htmlContent = generatePieHtmlBegin();
	for state in states:	
		(statePercentage,totalContState,DemPercent,RepPercent,OtherPercent) = getStateData(state)
		
		
		htmlContent = htmlContent + generatePieHtmlDataStr(state,totalContState,DemPercent,OtherPercent,RepPercent)  
		if(state != "WY"):
			htmlContent = htmlContent + ",\n"
		
		else:
			htmlContent = htmlContent + generatePieHtmlEnd()
		


	return htmlContent


print(writeHTMLforStates())

html_file = open("website.html", "w+")
html_file.write("%s" % writeHTMLforStates())
html_file.close()



#app = Flask(__name__)

@app.route("/")
def main():
    print(writeHTMLForStates())
    return writeHTMLforStates()
    #return render_template('website.html')
    #hmtl files need to be insie template 
    #style.css files need to be in static

#if __name__ == "__main__":
	#app.run(debug=True,host="0.0.0.0",port=80)
