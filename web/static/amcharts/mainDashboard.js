var graphColors = ['#7aaebc', '#7aae00', '#B888C7', '#E6E47C', '#D86881', '#286271', '#D9D900', '#6D1A99', '#235C1A', '#2E4263', '#FF0440', '#B5E982', '#40293F', '#8C1F1D'];
	var chart1=AmCharts.makeChart( "databaseChart", {
		"type": "pie",
		"theme": "light",
		  "dataLoader": {
		    "url": '<c:url value="/chart/getDatabaseUsage.do"/>',
		    "format": "json",
		    "reload":10,
		 //   "playAnimation": false
		  },
		  "valueField": "value",
		  "titleField": "key",
		  "labelText": '[[title]]',
		  "balloonText": '[[percents]]%([[value]]MB)',
		"radius": '35%',
		"innerRadius": '60%',
		   "balloon":{
		   "fixedPosition":true
		  },
		  "listeners": [{
			    "event": "init",
			    "method": function(event) {
			      // apply slice colors to their labels
			      var chart = event.chart;
			      if (chart.labelColorField === undefined)
			        chart.labelColorField = "labelColor";
			      for(var i = 0; i < chart.chartData.length; i++) {
			        chart.dataProvider[i][chart.labelColorField] = chart.chartData[i].color;
			      }
			      chart.validateData();
			      chart.animateAgain();
			    }
			}]
		} );
		
	var chart2=AmCharts.makeChart( "agentPresentListChart", {
			"type": "pie",
			"theme": "light",
			  "dataLoader": {
			    "url": '<c:url value="/chart/getAgentPresentList.do"/>',
			    "format": "json",
			    "reload":10,
			 //   "playAnimation": false
			  },
			  "valueField": "value",
			  "titleField": "key",
			  "labelText": '[[title]]',
			  "balloonText": '[[percents]]%([[value]])',
			"radius": '35%',
			"innerRadius": '60%',
			   "balloon":{
			   "fixedPosition":true
			  },
			  "listeners": [{
				    "event": "init",
				    "method": function(event) {
				      // apply slice colors to their labels
				      var chart2 = event.chart;
				      if (chart2.labelColorField === undefined)
				        chart2.labelColorField = "labelColor";
				      for(var i = 0; i < chart.chartData.length; i++) {
				        chart.dataProvider[i][chart.labelColorField] = chart.chartData[i].color;
				      }
				      chart2.validateData();
				      chart2.animateAgain();
				    }
				}]
			} );
	
/**
 * AmCharts plugin: automatically color each individual column
 * -----------------------------------------------------------
 * Will apply to graphs that have autoColor: true set
 */
var chart3 = AmCharts.makeChart( "packetChart", {
  "type": "serial",
  "theme": "light",
  "dataProvider": [ {
    "country": "USA",
    "visits": 2025
  }, {
    "country": "China",
    "visits": 1882
  }, {
    "country": "South Korea",
    "visits": 443
  } ],
  "startDuration": 1,
  "graphs": [ {
    "balloonText": "[[category]]: <b>[[value]]</b>",
    "fillAlphas": 0.8,
    "lineAlpha": 0.2,
    "type": "column",
    "valueField": "visits",
    "autoColor": true
  } ],
  "chartCursor": {
    "categoryBalloonEnabled": false,
    "cursorAlpha": 0,
    "zoomable": false
  },
  "categoryField": "country",
  "categoryAxis": {
    "gridPosition": "start",
    "gridAlpha": 0,
    "tickPosition": "start"
  }

} );

AmCharts.addInitHandler(function(chart3) {
  // check if there are graphs with autoColor: true set
  for(var i = 0; i < chart3.graphs.length; i++) {
    var graph = chart3.graphs[i];
    if (graph.autoColor !== true)
      continue;
    var colorKey = "autoColor-"+i;
    graph.lineColorField = colorKey;
    graph.fillColorsField = colorKey;
    for(var x = 0; x < chart3.dataProvider.length; x++) {
      var color = chart3.colors[x]
      chart3.dataProvider[x][colorKey] = color;
    }
  }
  
}, ["serial"]);