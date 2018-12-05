#!/usr/bin/env python
# Html generator, patterned off of piecharts_basic.html

def generateHtmlBegin():
    htmlBegin = """<!DOCTYPE html>
<meta charset='utf-8'>
<!-- saved from url=(0064)https://www.w3schools.com/w3css/tryw3css_templates_marketing.htm -->
<html><head><meta http-equiv="Content-Type" content="text/html; charset=UTF-8"><title>ConTracker</title>

    <script src='https://d3js.org/d3.v3.js'></script>
<!--
<script type='text/javascript' src='script.js'></script>
-->


<meta name="viewport" content="width=device-width, initial-scale=1">
<link rel="stylesheet" href="./static/w3.css">
<link rel="stylesheet" href="./static/css">
<link rel="stylesheet" href="./static/font-awesome.min.css">



<style>
html,body,h1,h2,h3,h4 {font-family:"Lato", sans-serif}
.mySlides {display:none}
.w3-tag, .fa {cursor:pointer}
.w3-tag {height:15px;width:15px;padding:0;margin-top:6px}


body {
  font: 14px sans-serif;
}

.bar rect {
  shape-rendering: crispEdges;
}

.bar text {
  fill: #999999;
}

.axis path, .axis line {
  fill: none;
  stroke: #000;
  shape-rendering: crispEdges;
}
table {  
    color: #333;
    font-family: Helvetica, Arial, sans-serif;
    width: 640px; 
    border-collapse: 
    collapse; border-spacing: 0; 
}

td, th {  
    border: 1px solid transparent; /* No more visible border */
    height: 35px; 
    transition: all 0.3s;  /* Simple transition for hover effect */
}

th {  
    background: #DFDFDF;  /* Darken header a bit */
    font-weight: bold;
}

td {  
    background: #FAFAFA;
    text-align: center;
}


</style>



</head><body>



<div class="w3-top">
  <div class="w3-row w3-large w3-light-grey">
    <div class="w3-col s3">
      <a href="#" class="w3-button w3-block">Home</a>
    </div>
    <div class="w3-col s3">
      <a href="#donation_table" class="w3-button w3-block">Donation Table</a>
    </div>
    <div class="w3-col s3">
      <a href="#warchest_table" class="w3-button w3-block">Warchest Table</a>
    </div>
    <div class="w3-col s3">
      <a href="#Histogram" class="w3-button w3-block">State Donation Totals</a>
    </div>
  </div>
</div>


<!-- Content -->
<div class="w3-content" style="max-width:1100px;margin-top:80px;margin-bottom:80px">

  <div class="w3-center">
    <h1 ><b>ConTracker</b></h1>
  </div>



  <div class="w3-center w3-padding-64" id="bubblechart">
      <span class="w3-xlarge w3-bottombar w3-border-dark-grey w3-padding-16">Party Campaign Contributions by State</span>
      <br><br>
      <br><br>
      <br><br>
      <div id="bubbles_script" style="display: block" >
      </div>
      <br>
      <div id="tables_script" width=100vw height=100vh style="display:block"></div>
      </div>
  </div>

  <div class="w3-center w3-padding-64" id="donation_table">
      <span class="w3-xlarge w3-bottombar w3-border-dark-grey w3-padding-16">Candidate Total Donation Dollars</span>
      <br><br>
      <br><br>
      <div id="donation_script" style="display: block">
      </div>
  </div>
 

    
  <div class="w3-center w3-padding-64" id="warchest_table">
      <span class="w3-xlarge w3-bottombar w3-border-dark-grey w3-padding-16">Candidate Total Warchest Dollars</span>
      <br><br>
      <br><br>
      <div id="warchest_script" style="display: block">
      </div>

      
  </div>

  <div class="Warchest table">
    
   
  </div>
  <div class="w3-row-padding" id="Histogram">
    <div class="w3-center w3-padding-64">
      <span class="w3-xlarge w3-bottombar w3-border-dark-grey w3-padding-16">State Total Donation Dollars</span>
      <br><br>
      <br><br>
    <div id="histogram_script" style="display: block">
    </div>
    </div>

 """ 
    return htmlBegin

def generatePieHtmlDataStr( initials, totalContributions, demPercent, otherPercent, repPercent, topTenDonees, topTenWarChests):
    dataStr = '{"percentages": '
    dataStr = dataStr + '[{"value":' + str(demPercent) + '},'
    dataStr = dataStr + '{"value":' + str(otherPercent) + '},'
    dataStr = dataStr + '{"value":' + str(repPercent) + '}],'
    dataStr = dataStr + '"total":' + str(totalContributions) + ','
    dataStr = dataStr + '"top10Donees":' + str(formatCandidateRows(topTenDonees)) + ','
    dataStr = dataStr + '"top10Warchests":' + str(formatWarchestRows(topTenWarChests)) + ','
    dataStr = dataStr + '"initials":"' + initials + '"}'
    return dataStr

def formatCandidateRows(topTen):
    topStr = '[\n'
    for cand in topTen[:-1]:
        topStr = topStr + formatCandidateRow(cand)
        topStr = topStr + ',\n'
    topStr = topStr + formatCandidateRow(topTen[-1])
    topStr = topStr + ']'
    return topStr

def formatCandidateRow(cand):
    rowStr = '{'
    rowStr = rowStr + '"Name":"' + str(cand[0]) + '",'
    rowStr = rowStr + '"TotalDonations":' + str(cand[1]) + ','
    rowStr = rowStr + '"State":"' + str(cand[2]) + '",'
    rowStr = rowStr + '"Party":"' + str(cand[3]) + '"}'
    return rowStr

def formatWarchestRows(topTen):
    topStr = '[\n'
    for cand in topTen[:-1]:
        topStr = topStr + formatWarchestRow(cand)
        topStr = topStr + ',\n'
    topStr = topStr + formatWarchestRow(topTen[-1])
    topStr = topStr + ']'
    return topStr

def formatWarchestRow(cand):
    rowStr = '{'
    rowStr = rowStr + '"Name":"' + str(cand[0]) + '",'
    rowStr = rowStr + '"Warchest":' + str(cand[1]) + ','
    rowStr = rowStr + '"State":"' + str(cand[2]) + '",'
    rowStr = rowStr + '"Party":"' + str(cand[3]) + '"}'
    return rowStr

#testingTopTen = [("O'ROURKE, ROBERT (BETO)", 70243103.56, 'TX', 'DEM'), ('SCOTT, RICK GOV', 68801011.68, 'FL', 'REP'), ('MCCASKILL, CLAIRE', 33385760.03, 'MO', 'DEM'), ('OSSOFF, T. JONATHAN', 31552052.24, 'GA', 'DEM'), ('HUGIN, ROBERT', 30289561.23, 'NJ', 'REP'), ('CRUZ, RAFAEL EDWARD  TED', 29972337.2, 'TX', 'REP'), ('NELSON, BILL', 26594280.91, 'FL', 'DEM'), ('BALDWIN, TAMMY', 25844219.98, 'WI', 'DEM'), ('HEITKAMP, HEIDI', 25353646.63, 'ND', 'DEM'), ('JONES, DOUG', 25083351.65, 'AL', 'DEM')]
#print(formatWarchestRows(testingTopTen))

def generateHtmlEnd():
    htmlEnd = """
</body></html>"""
    return htmlEnd

def generatePieChartHtmlBegin():
    pieBegin = """<script type="text/javascript">
    // Adapted from http://bl.ocks.org/enjalot/1203641   
var bubbles_script_global = {};  
(function() {
var color = ["#98AFC7", "#B6B6B4", "#FB8885"],
width = 960,
height = 500,
maxRadius = 100,
padding = 1.5;
currentSortMode = 0,
currentAscending = 1,
data = [
    """
    return pieBegin

def generatePieChartHtmlEnd():
    pieEnd = """];
String.prototype.format = function () {
        var args = [].slice.call(arguments);
        return this.replace(/(\{\d+\})/g, function (a){
            return args[+(a.substr(1,a.length-2))||0];
        });
};
// display the pie charts
var links = [];
var numStates = data.length;
var state;
for(state = 0; state < numStates; state++) {
    var radius = 0.004 * Math.sqrt(data[state].total), 
    //alert(radius);
    xStart = (radius/maxRadius);
    if(currentSortMode == 0) 
	xStart = (data[state].percentages[0].value - data[state].percentages[2].value + 100) / 200;
    if(currentSortMode == 2) {
        firstInitialInt = data[state].initials.charAt(0) - 'A';
        secondInitialInt = data[state].initials.charAt(1) - 'A';
        xStart = (firstInitialInt * 26 + secondInitialInt) / 26 / 26;
    }
    if(xStart < 0) alert(xStart);
	
    if(currentAscending == -1) xStart = (1 - xStart);
    xStart = xStart * width
    var yStart = (-0.015+.03*Math.random() + 0.5)*height;
    data[state].x = xStart;
    data[state].y = yStart;
    data[state].radius = radius;
    data[state].percentages[0].radius = radius;
    data[state].percentages[1].radius = radius;
    data[state].percentages[2].radius = radius;
    var anchor = JSON.parse(JSON.stringify(data[state]));
        anchor.fixed = true;
        anchor.anchor = true;
        anchor.percentages[0].anchor = true;
        anchor.percentages[1].anchor = true;
        anchor.percentages[2].anchor = true;
        anchor.y = 0.5*height;
    data.push(anchor);
    links.push({"source":  state, "target":  numStates + state});
    tabulate(data[state].top10Donees, ["Name","TotalDonations","State","Party"], "tables_script", "top10Donees_" + data[state].initials);
    tabulate(data[state].top10Warchests, ["Name","Warchest","State","Party"], "tables_script", "top10Warchests_" + data[state].initials);

}
//alert(JSON.stringify(links))
//alert(JSON.stringify(data[5]))
//alert(JSON.stringify(data[55]))
//alert(JSON.stringify(data))
// mashup from forcelayout.html
var force = d3.layout.force()
    .size([width, height])
    .charge(0)
	.gravity(0)
    .linkDistance(1)
    .linkStrength(0.3)
    .on("tick", tick);

var drag = force.drag()
    .on("dragstart", dragstart);

var svg = d3.select("#bubbles_script").append("svg")
    .attr("width", width)
    .attr("height", height)
    .attr("style", "border:solid;display:block;margin:auto");

var link = svg.selectAll(".link"),
    node = svg.selectAll(".node");

force
    .nodes(data)
    .links(links)
    .start();


link = link.data(links)
nodeOnEnter = node.data(data)
     .enter()

node = nodeOnEnter
     .append("svg:g")
     .attr("width", function(d) { return 2*d.radius; })  
     .attr("height", function(d) { return 2*d.radius; })
     .attr("class", "node")
     .attr("r", function(node){
 	if(node.fixed === true) return 0;
         return node.radius;
 	})
     .on("dblclick", dblclick)
     .call(drag)  
/*
circles = nodeOnEnter
    .append("circle")
    .attr("class", "node")
    .attr("r", function(node){
		if(node.fixed === true) return 0;
        return node.radius;
	})
    .on("dblclick", dblclick)
    .call(drag);
*/
//alert(JSON.stringify(node.data()))
var arcContainers = node
  .append("svg:g")              
    .data(data.map(function(d) { return d.percentages; }) )
    .attr("transform", function(d) { 
        //alert(d);
        return "translate({0},{0})".format(d[0].radius); 
    });     

//alert(JSON.stringify(arcContainers.data()))
var arc = d3.svg.arc()
   .innerRadius(0)            
   .outerRadius(function(d) {  
       if(d.data.anchor) return 0;
       return d.data.radius; } );

var pie = d3.layout.pie()       
   .value(function(d) { return d.value; }).sort(null);  
  
var arcs = arcContainers.selectAll("g.slice")    
   .data(pie)                         
   .enter()                            
   .append("svg:g")                
       .attr("class", "slice");

arcs.append("svg:path")
   .attr("fill", function(d, i) { return color[i]; } )
    .attr("transform", function(d) { 
        return "translate({0},{0})".format(-d.data.radius); 
    })    
   .attr("d", arc);       

//alert(JSON.stringify(arcContainers.data()))
   arcContainers.append("svg:text")
       .data(data)                             
       .attr("text-anchor", "middle")
       .attr("transform", function(d) { 
          return "translate({0},{1})".format(-d.radius, -d.radius + 0.35*d.radius); 
       })    
       .attr("font-family", "Times")
       .attr("font-size", function(d) { 
           return 2*(Math.floor(0.4*d.radius ))+"pt";
       })
       .text(function(d) { 
           if(d.fixed) return "";
           return d.initials; })
       .attr("style.display", function(d) {
           if(d.anchor) return "none";
           return "block";
       })

function tabulate(data, columns, targetDivName, newDivName) {
	var newDiv = d3.select('#' + targetDivName)
		.append('div')
		.attr("id", newDivName)
		.attr("style", "display:none")
	var table = newDiv
		.append('table')
		.attr("style", "margin:auto")
	var thead = table.append('thead')
	var	tbody = table.append('tbody');

	// append the header row
	thead.append('tr')
	  .selectAll('th')
	  .data(columns).enter()
	  .append('th')
	    .text(function (column) { return column; });

	// create a row for each object in the data
	var rows = tbody.selectAll('tr')
	  .data(data)
	  .enter()
	  .append('tr');

	// create a cell in each row for each column
	var cells = rows.selectAll('td')
	  .data(function (row) {
	    return columns.map(function (column) {
	      return {column: column, value: row[column]};
	    });
	  })
	  .enter()
	  .append('td')
	    .text(function (d) { return d.value; });
	newDiv.append('br');

  return table;
}

bubbles_script_global.link = link;
bubbles_script_global.node = node;
bubbles_script_global.data = data;
bubbles_script_global.maxRadius = maxRadius;
bubbles_script_global.padding = padding;
bubbles_script_global.currentClickedInitials = "AB";
showCurrentStateTopTen();
})();

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

function setCurrentStateTopTen(initials) {
    hideCurrentStateTopTen();
    bubbles_script_global.currentClickedInitials = initials;
    showCurrentStateTopTen();
}

function hideCurrentStateTopTen() {
  d3.select("#top10Donees_" + bubbles_script_global.currentClickedInitials)
    .attr("style", "display:none");
  d3.select("#top10Warchests_" + bubbles_script_global.currentClickedInitials)
    .attr("style", "display:none");
}

function showCurrentStateTopTen() {
  d3.select("#top10Donees_" + bubbles_script_global.currentClickedInitials)
    .attr("style", "display:block");
  d3.select("#top10Warchests_" + bubbles_script_global.currentClickedInitials)
    .attr("style", "display:block");
}

function tick() {
    bubbles_script_global.link.attr("x1", function(d) { return d.source.x; })
      .attr("y1", function(d) { return d.source.y; })
      .attr("x2", function(d) { return d.target.x; })
      .attr("y2", function(d) { return d.target.y; });

    bubbles_script_global.node.each(collide(0.5));
    bubbles_script_global.node.attr("transform", function(d) { return "translate(" + d.x + "," + d.y + ")"; })
}


function dblclick(d) {
  d3.select(this).classed("fixed", d.fixed = false);
}

function dragstart(d) {
  setCurrentStateTopTen(d.initials);
}


 // Resolves collisions between d and all other circles.
 // adapted from https://bl.ocks.org/mbostock/1748247
function collide(alpha) {
  var quadtree = d3.geom.quadtree(bubbles_script_global.data.filter(function(d){return !d.fixed}));
  return function(d) {
    if(d.anchor) return true;
    var r = d.radius + bubbles_script_global.maxRadius + bubbles_script_global.padding,
        nx1 = d.x - r,
        nx2 = d.x + r,
        ny1 = d.y - r,
        ny2 = d.y + r;
    quadtree.visit(function(quad, x1, y1, x2, y2) {
      if (quad.point && (quad.point !== d)) {
        var x = d.x - quad.point.x,
            y = d.y - quad.point.y,
            l = Math.sqrt(x * x + y * y),
            r = d.radius + quad.point.radius + bubbles_script_global.padding;
        if (l < r) {
          l = (l - r) / l * alpha;
          d.x -= x *= l;
          d.y -= y *= l;
          quad.point.x += x;
          quad.point.y += y;
        }
      }
      return x1 > nx2 || x2 < nx1 || y1 > ny2 || y2 < ny1;
    });
  };
}

</script>
"""
    return pieEnd

def generateHistogramBegin():
    histogramBegin = """<script>
(function() {
var color = "steelblue";
var randomData =
    """
    return histogramBegin

def generateHistorgramEnd(targetDiv):
    histogramEnd = """
var values = randomData;

// A formatter for counts.
var formatCount = d3.format(",.0f");

var margin = {top: 20, right: 30, bottom: 30, left: 30},
    width = 960 - margin.left - margin.right,
    height = 500 - margin.top - margin.bottom;

var max = d3.max(values);
var min = d3.min(values);
var x = d3.scale.log()
      .domain([min, max])
      .range([0, width]);

// Generate a histogram using twenty uniformly-spaced bins.
var data = d3.layout.histogram()
    .bins(x.ticks(20))
    (values);
var yMax = d3.max(data, function(d){return d.length});
var yMin = d3.min(data, function(d){return d.length});
var colorScale = d3.scale.linear()
            .domain([yMin, yMax])
            .range([d3.rgb(color).brighter(), d3.rgb(color).darker()]);

var y = d3.scale.linear()
    .domain([0, yMax])
    .range([height, 0]);

var xAxis = d3.svg.axis()
    .scale(x)
    .orient("bottom");

var svg = d3.select("#""" + targetDiv+"""").append("svg")
    .attr("width", width + margin.left + margin.right)
    .attr("height", height + margin.top + margin.bottom)
  .append("g")
    .attr("transform", "translate(" + margin.left + "," + margin.top + ")");

var bar = svg.selectAll(".bar")
    .data(data)
  .enter().append("g")
    .attr("class", "bar")
    .attr("transform", function(d) { return "translate(" + x(d.x) + "," + y(d.y) + ")"; });

bar.append("rect")
    .attr("x", 1)
    .attr("width", width/23.5 - 1)
    .attr("height", function(d) { return height - y(d.y); })
    .attr("fill", function(d) { return colorScale(d.y) });

bar.append("text")
    .attr("dy", ".75em")
    .attr("y", -12)
    .attr("x", (width/23.5 -1) / 2)
    .attr("text-anchor", "middle")
    .text(function(d) { return formatCount(d.y); });

svg.append("g")
    .attr("class", "x axis")
    .attr("transform", "translate(0," + height + ")")
    .call(xAxis);
})();

</script>
    """
    return histogramEnd
