#!/usr/bin/env python
# Html generator, patterned off of piecharts_basic.html

def generatePieHtmlBegin():
    htmlBegin = """<!DOCTYPE html>
<html>
  <head>    
    <meta http-equiv="Content-type" content="text/html; charset=utf-8">
    <title>ConTracker v1.1</title>
    <script src='https://d3js.org/d3.v3.js'></script>


    <style type="text/css">
        .slice text {
            font-size: 12pt;
            font-family: Arial;
        }   
    </style>
  </head>
  <body>
    <script type="text/javascript">
    </script>
    <button onclick="switchSortMode(0)">Party</button>
    <button onclick="switchSortMode(1)">Total</button>
    <button onclick="switchSortMode(2)">Initials</button>
    <br>
    <br>
    <br>
    <div id="pieCharts01" width=100vw height=100vh style="display:block"></div>
    <div id="pieCharts0-1" width=100vw height=100vh style="display:none"></div>
    <div id="pieCharts11" width=100vw height=100vh style="display:none"></div>
    <div id="pieCharts1-1" width=100vw height=100vh style="display:none"></div>
    <div id="pieCharts21" width=100vw height=100vh style="display:none"></div>
    <div id="pieCharts2-1" width=100vw height=100vh style="display:none"></div>
    
    <script type="text/javascript">
    // Adapted from http://bl.ocks.org/enjalot/1203641     
var color = ["#98AFC7", "#B6B6B4", "#FB8885"],
currentSortMode = 0,
currentAscending = 1,
data = ["""
    return htmlBegin

def generatePieHtmlDataStr( initials, totalContributions, demPercent, otherPercent, repPercent):
    dataStr = '{"percentages": '
    dataStr = dataStr + '[{"value":' + str(demPercent) + '},'
    dataStr = dataStr + '{"value":' + str(otherPercent) + '},'
    dataStr = dataStr + '{"value":' + str(repPercent) + '}],'
    dataStr = dataStr + '"total":' + str(totalContributions) + ','
    dataStr = dataStr + '"initials":"' + initials + '"}'
    return dataStr

def generatePieHtmlEnd():
    htmlEnd = """];

drawPieDisplay(0,1);
drawPieDisplay(0,-1);
drawPieDisplay(1,1);
drawPieDisplay(1,-1);
drawPieDisplay(2,1);
drawPieDisplay(2,-1);
function drawPieDisplay(sortMode, ascending) {
    if(sortMode == 0) sortByDominance(data, ascending);
    if(sortMode == 1) sortByTotals(data, ascending);
    if(sortMode == 2) sortByInitials(data, ascending);

    // display the pie charts
    var state;   
    for(state = 0; state < data.length; state++) {
        var r = 0.006 * Math.sqrt(data[state].total), 
        w = 2*r,                  
        h = 2*r;

        var vis = d3.select("#pieCharts" + sortMode + "" + ascending)
        .append("svg:svg")              
        .data([data[state].percentages])               
            .attr("width", w)          
            .attr("height", h)
        .append("svg:g")             
            .attr("transform", "translate(" + r + "," + r + ")") 

        var arc = d3.svg.arc()            
        .outerRadius(r);

        var pie = d3.layout.pie()       
        .value(function(d) { return d.value; }).sort(null);  
  
        var arcs = vis.selectAll("g.slice")    
        .data(pie)                         
        .enter()                            
            .append("svg:g")                
                .attr("class", "slice");

        arcs.append("svg:path")
                .attr("fill", function(d, i) { return color[i]; } ) 
                .attr("d", arc);       

        vis.append("svg:text")                             
            .attr("text-anchor", "middle")
            .attr("transform", "translate(" + 0 + "," + 0.35*r + ")")
            .attr("font-family", "Times")
            .attr("font-size", function(d,i) { 
                return 2*(Math.floor(0.4*r))+"pt";
            })
            .text(function(d, i) { return data[state].initials; });   
    }
}

function sortByDominance(data, ascending) {
    // sort the data by rep, dem
    data.sort(function(a,b) { 
         var aDemDominance = a.percentages[0].value - a.percentages[2].value;
         var bDemDominance = b.percentages[0].value - b.percentages[2].value;
         return ascending*(aDemDominance - bDemDominance);
    });
}

function sortByInitials(data, ascending) {
    data.sort(function(a,b) { 
    // from https://stackoverflow.com/questions/51165/how-to-sort-strings-in-javascript
    if (a.initials < b.initials)
        return -1 * ascending;
    if ( a.initials > b.initials)
        return 1 * ascending;
    return 0 * ascending;
    });
}

function sortByTotals(data, ascending) {
    data.sort(function(a,b) { return ascending * (a.total - b.total); });
}


function switchSortMode(newSortMode){
    if(newSortMode != currentSortMode) setCurrentSorting(newSortMode, 1);
    else toggleAscending();
}

function toggleAscending() {
    setCurrentSorting(currentSortMode, currentAscending * -1);
}

function setCurrentSorting(newSortMode, newAscending) {
    hideCurrent();
    currentSortMode = newSortMode;
    currentAscending = newAscending;
    showCurrent();
}

function hideCurrent() {
    var pieCharts = document.getElementById("pieCharts"+ currentSortMode + "" + currentAscending);
    pieCharts.style.display = "none";
}

function showCurrent() {
    var pieCharts = document.getElementById("pieCharts"+ currentSortMode + "" + currentAscending);
    pieCharts.style.display = "block";
}
    </script>
  </body>
</html>"""
    return htmlEnd
