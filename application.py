from flask import Flask, render_template
from database.queryDatabase import getStateData
from database.queryDatabase import getTopTenOverall
from database.queryDatabase import getTopTenState
from database.queryDatabase import listOfContributions
from database.queryDatabase import listOfWarchests
from ConTrackerHtmlGen import generateHtmlBegin
from ConTrackerHtmlGen import generateHtmlEnd
from ConTrackerHtmlGen import generatePieChartHtmlBegin
from ConTrackerHtmlGen import generatePieHtmlDataStr
from ConTrackerHtmlGen import generatePieChartHtmlEnd
from ConTrackerHtmlGen import generateHistogramBegin
from ConTrackerHtmlGen import generateHistorgramEnd
from ConTrackerHtmlGen import formatCandidateRows
from ConTrackerHtmlGen import formatWarchestRows

states = ["AL", "AK", "AZ", "AR", "CA", "CO", "CT", "DC", "DE", "FL", "GA", 
          "HI", "ID", "IL", "IN", "IA", "KS", "KY", "LA", "ME", "MD", 
          "MA", "MI", "MN", "MS", "MO", "MT", "NE", "NV", "NH", "NJ", 
          "NM", "NY", "NC", "ND", "OH", "OK", "OR", "PA", "RI", "SC", 
          "SD", "TN", "TX", "UT", "VT", "VA", "WA", "WV", "WI", "WY"]

def writeHTMLforStates():
    htmlContent = generateHtmlBegin()
    htmlContent = htmlContent + generatePieChartHtmlBegin()
    stateContributions = []
    for state in states:
        (totalContState,DemPercent,RepPercent,OtherPercent) = getStateData(state)
        stateContributions.append(totalContState)
        htmlContent = htmlContent + generatePieHtmlDataStr(state, totalContState,DemPercent,OtherPercent,RepPercent)
        if(state != "WY"):
            htmlContent = htmlContent + ",\n"
        else:
            htmlContent = htmlContent + generatePieChartHtmlEnd()
    htmlContent = htmlContent + generateHistogramBegin();
    htmlContent = htmlContent + str(listOfContributions())
    htmlContent = htmlContent + generateHistorgramEnd("donation_script");
    htmlContent = htmlContent + generateHistogramBegin();
    htmlContent = htmlContent + str(listOfWarchests())
    htmlContent = htmlContent + generateHistorgramEnd("warchest_script");
    htmlContent = htmlContent + generateHistogramBegin();
    htmlContent = htmlContent + str(stateContributions)
    htmlContent = htmlContent + generateHistorgramEnd("histogram_script");
    htmlContent = htmlContent + generateHtmlEnd();
    return htmlContent

"""
print(writeHTMLforStates())

html_file = open("website.html", "w+")
html_file.write("%s" % writeHTMLforStates())
html_file.close()
"""
Error404 = "<h1> You encountered a 404 error. Here is a patriotic puppy, do you see that? </h1><br><img src=\"/static/PatrioticPuppy.jpg\"> "

application = Flask(__name__)

@application.route("/")
def main():
	return writeHTMLforStates()

@application.errorhandler(404)
def error404(error):
	return Error404,404

@application.route("/HelloWorld")
def test():
	return "Hello World!"
	
	return "Hello World"
	#hmtl files need to be insie template 
	#style.css files need to be in static
#print(writeHTMLforStates())
if __name__ == "__main__":
	#application.debug = True
	application.run()
