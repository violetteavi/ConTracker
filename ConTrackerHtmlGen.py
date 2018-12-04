#!/usr/bin/env python
# Html generator, patterned off of piecharts_basic.html

def generateHtmlBegin():
    htmlBegin = """<!DOCTYPE html>
<meta charset='utf-8'>
<!-- saved from url=(0064)https://www.w3schools.com/w3css/tryw3css_templates_marketing.htm -->
<html><head><meta http-equiv="Content-Type" content="text/html; charset=UTF-8"><title>W3.CSS Template</title>

<script src="http://d3js.org/d3.v3.min.js" charset="utf-8"></script>
<!--
<script type='text/javascript' src='script.js'></script>
-->


<meta name="viewport" content="width=device-width, initial-scale=1">
<link rel="stylesheet" href="./W3.CSS Template_files/w3.css">
<link rel="stylesheet" href="./W3.CSS Template_files/css">
<link rel="stylesheet" href="./W3.CSS Template_files/font-awesome.min.css">



<style>
html,body,h1,h2,h3,h4 {font-family:"Lato", sans-serif}
.mySlides {display:none}
.w3-tag, .fa {cursor:pointer}
.w3-tag {height:15px;width:15px;padding:0;margin-top:6px}

body {
  font: 10px sans-serif;
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


</style>



</head><body>

<script type='text/javascript' src='script.js'></script>


<div class="w3-top">
  <div class="w3-row w3-large w3-light-grey">
    <div class="w3-col s3">
      <a href="W3.CSS Template.html" class="w3-button w3-block">Home</a>
    </div>
    <div class="w3-col s3">
      <a href="#donation table" class="w3-button w3-block">Donation Table</a>
    </div>
    <div class="w3-col s3">
      <a href="#warchest table" class="w3-button w3-block">Warchest Table</a>
    </div>
    <div class="w3-col s3">
      <a href="#Histogram" class="w3-button w3-block">Histogram</a>
    </div>
  </div>
</div>


<!-- Content -->
<div class="w3-content" style="max-width:1100px;margin-top:80px;margin-bottom:80px">

  <div class="w3-panel">
    <h1><b>ConTracker</b></h1>
  </div>



  <div class="bubbles">
      <div id="pieCharts" style="display: block">
      </div>
  </div>

  <div class="w3-center w3-padding-64" id="donation table">
      <span class="w3-xlarge w3-bottombar w3-border-dark-grey w3-padding-16">Donation Table</span>
      <div id="donation_script" style="display: block">
      </div>
  </div>
 

    
  <div class="w3-center w3-padding-64" id="warchest table">
      <span class="w3-xlarge w3-bottombar w3-border-dark-grey w3-padding-16">Warchest Table</span>
      <div id="warchest_script" style="display: block">
      </div>

      
  </div>

  <div class="Warchest table">
    
   
  </div>
  <div class="w3-row-padding" id="Histogram">
    <div class="w3-center w3-padding-64">
      <span class="w3-xlarge w3-bottombar w3-border-dark-grey w3-padding-16">Donations by State (magnitude)</span>
    <div id="histogram_script" style="display: block">
      
    </div>
    </div>
 """ 
    return htmlBegin

def generatePieHtmlDataStr( initials, totalContributions, demPercent, otherPercent, repPercent):
    dataStr = '{"percentages": '
    dataStr = dataStr + '[{"value":' + str(demPercent) + '},'
    dataStr = dataStr + '{"value":' + str(otherPercent) + '},'
    dataStr = dataStr + '{"value":' + str(repPercent) + '}],'
    dataStr = dataStr + '"total":' + str(totalContributions) + ','
    dataStr = dataStr + '"initials":"' + initials + '"}'
    return dataStr

def formatCandidateRows(topTen):
    topStr = '{\n'
    for cand in topTen[:-1]:
        topStr = topStr + formatCandidateRow(cand)
        topStr = topStr + ',\n'
    topStr = topStr + formatCandidateRow(topTen[-1])
    topStr = topStr + '}'
    return topStr

def formatCandidateRow(cand):
    rowStr = '{'
    rowStr = rowStr + '"name":"' + str(cand[0]) + '",'
    rowStr = rowStr + '"totalDonations":' + str(cand[1]) + ','
    rowStr = rowStr + '"initials":"' + str(cand[2]) + '",'
    rowStr = rowStr + '"party":"' + str(cand[3]) + '"}'
    return rowStr

def formatWarchestRows(topTen):
    topStr = '{\n'
    for cand in topTen[:-1]:
        topStr = topStr + formatWarchestRow(cand)
        topStr = topStr + ',\n'
    topStr = topStr + formatWarchestRow(topTen[-1])
    topStr = topStr + '}'
    return topStr

def formatWarchestRow(cand):
    rowStr = '{'
    rowStr = rowStr + '"name":"' + str(cand[0]) + '",'
    rowStr = rowStr + '"warchest":' + str(cand[1]) + ','
    rowStr = rowStr + '"initials":"' + str(cand[2]) + '",'
    rowStr = rowStr + '"party":"' + str(cand[3]) + '"}'
    return rowStr

#testingTopTen = [("O'ROURKE, ROBERT (BETO)", 70243103.56, 'TX', 'DEM'), ('SCOTT, RICK GOV', 68801011.68, 'FL', 'REP'), ('MCCASKILL, CLAIRE', 33385760.03, 'MO', 'DEM'), ('OSSOFF, T. JONATHAN', 31552052.24, 'GA', 'DEM'), ('HUGIN, ROBERT', 30289561.23, 'NJ', 'REP'), ('CRUZ, RAFAEL EDWARD  TED', 29972337.2, 'TX', 'REP'), ('NELSON, BILL', 26594280.91, 'FL', 'DEM'), ('BALDWIN, TAMMY', 25844219.98, 'WI', 'DEM'), ('HEITKAMP, HEIDI', 25353646.63, 'ND', 'DEM'), ('JONES, DOUG', 25083351.65, 'AL', 'DEM')]
#print(formatWarchestRows(testingTopTen))

def generateHtmlEnd():
    htmlEnd = """
</body></html>"""
    return htmlEnd

def generatePieChartHtmlBegin():
    pieBegin = """<script src='https://d3js.org/d3.v3.js'></script>
    <script type="text/javascript">
    </script>
    <button onclick="switchSortMode(0)">Party</button>
    <button onclick="switchSortMode(1)">Total</button>
    <button onclick="switchSortMode(2)">Initials</button>
    <br>
    <br>
    <br>
    <div id="pieCharts" width=100vw height=100vh style="display:block"></div>
    
    <script type="text/javascript">
    // Adapted from http://bl.ocks.org/enjalot/1203641     
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
    pieBegin = """];
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
    xStart = (data[state].percentages[0].value - data[state].percentages[2].value) / 100;
    if(currentSortMode == 2) {
        firstInitialInt = data[state].initials.charAt(0) - 'A';
        secondInitialInt = data[state].initials.charAt(1) - 'A';
        xStart = (firstInitialInt * 26 + secondInitialInt) / 26 / 26;
    }
    
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
    data.push(anchor);
    links.push({"source":  state, "target":  numStates + state});

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
    .linkStrength(0.5)
    .on("tick", tick);

var drag = force.drag()
    .on("dragstart", dragstart);

var svg = d3.select("#pieCharts").append("svg")
    .attr("width", width)
    .attr("height", height);

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
   .attr("d", arc);       

//alert(JSON.stringify(arcContainers.data()))
   arcContainers.append("svg:text")
       .data(data)                             
       .attr("text-anchor", "middle")
       .attr("transform", function(d){ 
            return "translate(0," + 0.35*d.radius + ")";
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


function getTranslateByRadius(d) { 
    return "translate({0},{0})".format(d.radius); 
}
function tick() {
    link.attr("x1", function(d) { return d.source.x; })
      .attr("y1", function(d) { return d.source.y; })
      .attr("x2", function(d) { return d.target.x; })
      .attr("y2", function(d) { return d.target.y; });

    node.each(collide(0.5));
    node.attr("transform", function(d) { return "translate(" + d.x + "," + d.y + ")"; })
}

function dblclick(d) {
  d3.select(this).classed("fixed", d.fixed = false);
}

function dragstart(d) {
  //d3.select(this).classed("selected", d.selected = true);
}
 
 // Resolves collisions between d and all other circles.
 // adapted from https://bl.ocks.org/mbostock/1748247
function collide(alpha) {
  var quadtree = d3.geom.quadtree(data.filter(function(d){return !d.fixed}));
  return function(d) {
    if(d.anchor) return true;
    var r = d.radius + maxRadius + padding,
        nx1 = d.x - r,
        nx2 = d.x + r,
        ny1 = d.y - r,
        ny2 = d.y + r;
    quadtree.visit(function(quad, x1, y1, x2, y2) {
      if (quad.point && (quad.point !== d)) {
        var x = d.x - quad.point.x,
            y = d.y - quad.point.y,
            l = Math.sqrt(x * x + y * y),
            r = d.radius + quad.point.radius + padding;
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
    return pieBegin

def generateHistogramBegin():
    pieBegin = """<script src="http://d3js.org/d3.v3.min.js"></script>
<script>
var color = "steelblue";
var randomData =
    """
    return pieBegin

def generateHistorgramEnd(targetDiv):
    pieBegin = """
var values = randomData;
//d3.values(stateData, function(d) {return stateData.total})
//d3.range(1000).map(d3.random.normal(20, 5));

// A formatter for counts.
var formatCount = d3.format(",.0f");

var margin = {top: 20, right: 30, bottom: 30, left: 30},
    width = 960 - margin.left - margin.right,
    height = 500 - margin.top - margin.bottom;

var max = d3.max(values);
var min = d3.min(values);
var x = d3.scale.linear()
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

var svg = d3.select("#""" + targetDiv + """").append("svg")
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
    .attr("width", (x(data[0].dx) - x(0)) - 1)
    .attr("height", function(d) { return height - y(d.y); })
    .attr("fill", function(d) { return colorScale(d.y) });

bar.append("text")
    .attr("dy", ".75em")
    .attr("y", -12)
    .attr("x", (x(data[0].dx) - x(0)) / 2)
    .attr("text-anchor", "middle")
    .text(function(d) { return formatCount(d.y); });

svg.append("g")
    .attr("class", "x axis")
    .attr("transform", "translate(0," + height + ")")
    .call(xAxis);

/*
* Adding refresh method to reload new data
*/
function refresh(values){
  // var values = d3.range(1000).map(d3.random.normal(20, 5));
  var data = d3.layout.histogram()
    .bins(x.ticks(20))
    (values);

  // Reset y domain using new data
  var yMax = d3.max(data, function(d){return d.length});
  var yMin = d3.min(data, function(d){return d.length});
  y.domain([0, yMax]);
  var colorScale = d3.scale.linear()
              .domain([yMin, yMax])
              .range([d3.rgb(color).brighter(), d3.rgb(color).darker()]);

  var bar = svg.selectAll(".bar").data(data);

  // Remove object with data
  bar.exit().remove();

  bar.transition()
    .duration(1000)
    .attr("transform", function(d) { return "translate(" + x(d.x) + "," + y(d.y) + ")"; });

  bar.select("rect")
      .transition()
      .duration(1000)
      .attr("height", function(d) { return height - y(d.y); })
      .attr("fill", function(d) { return colorScale(d.y) });

  bar.select("text")
      .transition()
      .duration(1000)
      .text(function(d) { return formatCount(d.y); });

}

// Calling refresh repeatedly.
setInterval(function() {
  //var values = randomData
  //refresh(values);
}, 2000);

</script>
    """
    return pieBegin