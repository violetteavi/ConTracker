#!/usr/bin/env python
# Html generator, patterned off of piecharts.html

def generatePieHtmlBegin():
    htmlBegin = """<!DOCTYPE html>
<html>
  <head>    
    <meta http-equiv="Content-type" content="text/html; charset=utf-8">
    <title>Testing Pie Chart</title>
    <script src='http://d3js.org/d3.v2.js'></script>


    <style type="text/css">
        .slice text {
            font-size: 12pt;
            font-family: Arial;
        }   
    </style>
  </head>
  <body>
    <script type="text/javascript">
// Adapted from http://bl.ocks.org/enjalot/1203641     
    var color = ["#98AFC7", "#B6B6B4", "#FB8885"];

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
    var state;    
    for(state = 0; state < data.length; state++) {
        var r = 0.005 * Math.sqrt(data[state].total), 
        w = 2*r,                  
        h = 2*r;                  
        var vis = d3.select("body")
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

        arcs.append("svg:text")                                 
                .attr("transform", function(d) {               
                //we have to make sure to set these before calling arc.centroid
                d.innerRadius = 0;
                d.outerRadius = r;
                return "translate(" + arc.centroid(d) + ")";     
            })
            .attr("text-anchor", "middle")                     
            .text(function(d, i) { return ""; });   
        // was percentages[state][i].label

        vis.append("svg:text")                             
            .attr("text-anchor", "middle")                      
            .text(function(d, i) { return data[state].initials; });   
    }
    </script>
  </body>
</html>"""
    return htmlEnd

print(generatePieHtmlBegin())
print(generatePieHtmlDataStr('CA', 9001, 75, 5, 20))
print(generatePieHtmlEnd())
