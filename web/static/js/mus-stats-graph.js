AmCharts.ready(function () {
    dataChart = new AmCharts.AmSerialChart();
    dataChart.dataProvider = chartData;
    dataChart.categoryField = "date";
    dataChart.startDuration = 1;

    lineChart = new AmCharts.AmSerialChart();
    lineChart.dataProvider = chartData;
    lineChart.categoryField = "date";
    lineChart.startDuration = 1;

    var categoryAxis = dataChart.categoryAxis;
    categoryAxis.gridPosition = "start";
    
    lineChart.categoryAxis.gridPosition = "start";

    var dataValueAxis = new AmCharts.ValueAxis();
    dataValueAxis.axisAlpha = 0;
    dataValueAxis.gridAlpha = 0.1;
    dataValueAxis.position = "top";
    
    dataChart.addValueAxis(dataValueAxis);

    var lineValueAxis = new AmCharts.ValueAxis();
    lineValueAxis.axisAlpha = 0;
    lineValueAxis.gridAlpha = 0.1;
    lineValueAxis.position = "top";
    lineChart.addValueAxis(lineValueAxis);
    
    // line graph
    var lineGraph = new AmCharts.AmGraph();
    lineGraph.type = "line";
    lineGraph.lineColor = "#27c5ff";
    lineGraph.bulletColor = "#FFFFFF";
    lineGraph.bulletBorderColor = "#27c5ff";
    lineGraph.bulletBorderThickness = 2;
    lineGraph.bulletBorderAlpha = 1;
    lineGraph.title = "Total";
    lineGraph.valueField = "sum";
    lineGraph.lineThickness = 2;
    lineGraph.bullet = "round";
    lineGraph.fillAlphas = 0;
    lineGraph.balloonText = "<span style='font-size:13px;'>[[title]] in [[category]]:<b>[[value]]</b></span>";
    lineChart.addGraph(lineGraph);

    for(idx in categories) {
        var graph = new AmCharts.AmGraph();
        graph.type = "column";
        graph.title = categories[idx]; //"Income";
        graph.valueField = categories[idx]; //"income";
        graph.balloonText = categories[idx] + ":[[value]]"; //"Income:[[value]]";
        graph.lineAlpha = 0;
        graph.fillAlphas = 1;
        dataChart.addGraph(graph);
    }
    
    dataChart.write("datachart");
    lineChart.write("linechart");
});

