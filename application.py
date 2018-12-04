#from flask import Flask, render_template
from database.queryDatabase import getStateData
from database.queryDatabase import getTopTenOverall
from database.queryDatabase import getTopTenState
from database.queryDatabase import getWarchestOverall
from database.queryDatabase import getWarchestState
#from ConTrackerFetcher import getStateData 
from ConTrackerHtmlGen import generatePieHtmlBegin
from ConTrackerHtmlGen import generatePieHtmlDataStr
from ConTrackerHtmlGen import generatePieHtmlEnd
from ConTrackerHtmlGen import formatCandidateRows
from ConTrackerHtmlGen import formatWarchestRows

states = ["AL", "AK", "AZ", "AR", "CA", "CO", "CT", "DC", "DE", "FL", "GA", 
          "HI", "ID", "IL", "IN", "IA", "KS", "KY", "LA", "ME", "MD", 
          "MA", "MI", "MN", "MS", "MO", "MT", "NE", "NV", "NH", "NJ", 
          "NM", "NY", "NC", "ND", "OH", "OK", "OR", "PA", "RI", "SC", 
          "SD", "TN", "TX", "UT", "VT", "VA", "WA", "WV", "WI", "WY"]

def writeHTMLforStates():
    htmlContent = generatePieHtmlBegin()
    htmlContent = htmlContent + "topTenUSDonees = ["
    htmlContent = htmlContent + formatCandidateRows(getTopTenOverall())
    htmlContent = htmlContent + "]; \ntopTenUSWarchests = ["
    htmlContent = htmlContent + formatWarchestRows(getWarchestOverall())
    htmlContent = htmlContent + "]; \ndata = ["
    for state in states:
        (totalContState,DemPercent,RepPercent,OtherPercent) = getStateData(state)
        topCon = getTopTenState(state)
        topWar = getWarchestState(state)
        htmlContent = htmlContent + generatePieHtmlDataStr(state, totalContState,DemPercent,OtherPercent,RepPercent, topCon, topWar)
        if(state != "WY"):
            htmlContent = htmlContent + ",\n"
        else:
            htmlContent = htmlContent + generatePieHtmlEnd()
    return htmlContent

"""
print(writeHTMLforStates())

html_file = open("website.html", "w+")
html_file.write("%s" % writeHTMLforStates())
html_file.close()
"""
Error404 = "<h1> You encountered a 404 error. Here is a patriotic puppy, do you see that? </h1><br><img src=\"/static/PatrioticPuppy.jpg\"> "

#application = Flask(__name__)

#@application.route("/")
#def main():
#	return writeHTMLforStates()

#@application.errorhandler(404)
def error404(error):
	return Error404,404

#@application.route("/HelloWorld")
def test():
	return "Hello World!"
	
	#return "Hello World"
	#hmtl files need to be insie template 
	#style.css files need to be in static
print(writeHTMLforStates())
#if __name__ == "__main__":
	#application.debug = True
	#application.run()
