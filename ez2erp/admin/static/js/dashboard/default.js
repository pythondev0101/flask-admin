// profile chart start
new Chartist.Bar('.small-chart1', {
    labels: ['Q1', 'Q2', 'Q3', 'Q4', 'Q5', 'Q6', 'Q7','Q8','Q9','Q10','Q11'],
    series: [           
        [100,100,100,100,100,100,100,100,100,100,100]
      ],       
    }, {
      plugins: [

          Chartist.plugins.tooltip({
              appendToBody:false,
              className: "ct-tooltip"
          })
      ],
      stackBars: true,
      axisX: {
          showGrid: false,
          showLabel: false,
          offset: 0
      },
      axisY: {
          low: 0,
          showGrid: false,
          showLabel: false,
          offset: 0,
          labelInterpolationFnc: function(value) {
              return (value / 1000) + 'k';
          }
      }
  }).on('draw', function(data) {
      if(data.type === 'bar') {
          data.element.attr({
              style: 'stroke-width: 3px'
          });
      }
  });   
// profile chart end


// statistics chart start
  var options ={
    series: [
      {
        name:'Statistics',
        data:[20,30, 40, 80, 100, 40, 30]
      },
      {
        name: 'Statistics',
        data: [80,70, 60, 20, 0, 60, 70]
      }
    ],
    chart:{
      type:'bar',
      height:312,
      stacked:true,
      stackType: '100%',
      toolbar:{
        show:false,
      }
    }, 
    plotOptions: {
      bar:{
        horizontal: false,
        columnWidth: '30px',
        borderRadius: 10,
      },
    }, 
    grid: {
      show:false,                  
      xaxis: {
        lines: {
          show: false
        }
      }
    },
    dataLabels:{
      enabled: false,
    },
    fill: {
      opacity: 1
    },
    legend: {
      show:false
    },    
    states: {          
      hover: {
        filter: {
          type: 'darken',
          value: 1,
        }
      }           
    },
    colors:[WingoAdminConfig.primary,'#dce8ff'],
    xaxis: {
      categories:[
        'M','T','W','T','F','S','S'
      ],
      axisBorder:{
       show:false,
     },
      axisTicks:{
      show: false,
    },
    },
    yaxis:{
     labels:{
      show:false,
     },
    },
    responsive: [
        {
          breakpoint:1471,
          options: {
            chart: {
              height:235
            }
          },
        },
        {
          breakpoint:1366,
          options: {
            chart: {
              height:180
            }
          },
        },
        {
          breakpoint:1200,
          options: {
            chart: {
              height:250
            }
          },
        },
        {
          breakpoint:992,
          options: {
            chart: {
              height:168
            }
          },
        },      
    ],
  };
  var chart = new ApexCharts(document.querySelector("#chart-statistics"), options);
  chart.render();
// statistics chart end



// goal chart start
var options4 ={
      series:[65],
      chart:{
        height:380,
        type:'radialBar',
        offsetY:-10,
      },
      plotOptions: {
        radialBar: {
          startAngle: -135,
          endAngle: 135,
          inverseOrder: true,
          hollow: {
            margin:20,
            size:'65%',
            image: '../assets/images/dashboard/impossible.png',
            imageWidth: 80,
            imageHeight: 80,
            imageClipped: false,
            background: '#4d8aff36',
            dropShadow: {
            enabled: false,
            top: 0,
            left: 0,
            blur: 1,
            opacity: 0.3
          },
          },
          track: {
            opacity: 0.7,
            colors:[WingoAdminConfig.primary], 
          },
          dataLabels: {
            name: {
            fontSize: '16px',
            color: '#000',
            offsetY:150
          },
          value: {
            offsetY:110,
            fontSize:'20px',
            color: WingoAdminConfig.primary,
            formatter: function (val) {
              return val + "%";
            }
          },
          },
        }
      },
      responsive: [
        {
          breakpoint:1501,
          options: {
            chart: {
              height:300
            }
          },
        }
      ],
      labels: ['Goal In Progress'],
      colors: [WingoAdminConfig.primary],
    };
    var chart4 = new ApexCharts(document.querySelector(".goal-overview-chart"),
      options4
    );
    chart4.render();
// goal  chart end




// valuation chart start
var options = {
      series: [{
      name: 'Product value',
      data:[
        20,30,50,70,60,75,95,70,80,70,75,80,75,60,90,60,70,45,30,40
      ]         
    },
    {
      name: 'Product value',
      data:[
        -20,-30,-50,-70,-60,-75,-80,-70,-85,-70,-75,-80,-75,-60,-90,-60,-70,-45,-30,-40
      ]
    }
    ],
    chart: {
      type: 'bar',
      height: 320,
      stacked: true,
      toolbar: {
          show: false,
          tools: {
            download: false
        }
      }
    },
    legend:{
      show:false,
    },
    colors:['#dce8ff',WingoAdminConfig.primary],
    plotOptions: {
      bar: {
        horizontal: true,
        barHeight: '70%',
        startingShape: 'rounded',
        endingShape: 'rounded',              
      },
    },
    states: {          
      hover: {
        filter: {
          type: 'darken',
          value: 1,
        }
      }           
    },
    dataLabels: {
      enabled: false
    },
    stroke: {
      width: -1.80,
      colors: ["#fff"]
    },
    grid: {          
      xaxis: {
        lines: {
          show: false
        }
      },

       xaxis: {
            lines: {
                show: false
            }
        },   
        yaxis: {
            lines: {
                show: false
          }
      }, 
    },

    yaxis: {
      min:-100,
      max: 100,          
    },
    tooltip: {
      shared: false,
      x: {
        formatter: function (val) {
          return val
        }
      },
      y: {
        formatter: function (val) {
          return Math.abs(val) + "k"
        }
      }
    },        
    xaxis:{          
      categories:[
        '60k','50k','40k','50k','40k','30k','20k','10k'
      ],
      axisBorder: {
       show: false,
     },
      axisTicks: {
      show: false,
    },
    },
    responsive: [
        {
          breakpoint:1661,
          options: {
            chart: {
              height:270
            }
          },
        },
        {
          breakpoint:1471,
          options: {
            chart: {
              height:258
            }
          },
        },
        {
          breakpoint:1366,
          options: {
            chart: {
              height:375
            }
          },
        },
        {
          breakpoint: 768,
          options: {
            chart: {
              height: 300
            }
          },
        },
      ],
    };
    var chart = new ApexCharts(document.querySelector("#valuation-chart"), options);
    chart.render();
  // valuation chart end

  // letest update chart start
  var options11 = {
      series: [{
      data: [{
              x: new Date(1538778600000),
              y: [6620.81, 6650.5, 6623.04, 6633.33]
            },
            {
              x: new Date(1538780400000),
              y: [6600.01, 6643.59, 6620, 6630.11]
            },
            {
              x: new Date(1538782200000),
              y: [6620.71, 6648.95, 6623.34, 6635.65]
            },
            {
              x: new Date(1538784000000),
              y: [6600.65, 6651, 6629.67, 6638.24]
            },
            {
              x: new Date(1538785800000),
              y: [6638.24, 6640, 6620, 6624.47]
            },
            {
              x: new Date(1538787600000),
              y: [6602.53, 6636.03, 6621.68, 6624.31]
            },
            {
              x: new Date(1538789400000),
              y: [6610.61, 6632.2, 6617, 6626.02]
            },
            {
              x: new Date(1538791200000),
              y: [6627, 6627.62, 6584.22, 6603.02]
            },
            {
              x: new Date(1538793000000),
              y: [6500, 6608.03, 6598.95, 6604.01]
            },
            {
              x: new Date(1538794800000),
              y: [6650.5, 6614.4, 6602.26, 6608.02]
            },
            {
              x: new Date(1538796600000),
              y: [6600.02, 6610.68, 6601.99, 6608.91]
            },
            {
              x: new Date(1538798400000),
              y: [6608.91, 6618.99, 6608.01, 6612]
            },
            {
              x: new Date(1538800200000),
              y: [6612, 6615.13, 6605.09, 6600]
            },
            {
              x: new Date(1538802000000),
              y: [6612, 6624.12, 6608.43, 6622.95]
            },
            {
              x: new Date(1538803800000),
              y: [6623.91, 6623.91, 6615, 6615.67]
            },
            {
              x: new Date(1538805600000),
              y: [6618.69, 6618.74, 6610, 6610.4]
            },
          ]
    }],
    chart: {
      type: 'candlestick',
      height: 250,
      toolbar:{
        show:false,
      }
    },
    xaxis: {
      type: 'datetime',
     axisBorder: {
       show: false,
     },
     axisTicks: {
      show: false,
     },
     labels:{
      show:false,
        offsetX: 0,
      offsetY: 0,
     },
    },
    yaxis: {
      tooltip: {
        enabled: false
      }
    },
    yaxis:{
     labels:{
      show:false,
     },
    },
    stroke: {
       width: 0,
       lineCap:'round',
       curve: 'smooth',
    },
    plotOptions: {
      candlestick: {
        colors: {
          upward: WingoAdminConfig.primary,
          downward: '#dce8ff'
        },
         wick: {
            useFillColor: true,
          },
      },
      bar:{
      startingShape: 'round',
      endingShape: 'round',
      },
    },
    grid: {
      show: false,
    },
    responsive: [      
      {
        breakpoint:1300,
        options: {
          chart: {
            height:210
          }
        }
      }
    ]
    };
    var chart11 = new ApexCharts(document.querySelector("#chart-candle"), 
      options11
    );
    chart11.render();
  // letest update chart end

// chart2.render();
function generateDayWiseTimeSeries(baseval, count, yrange) {
  var i = 0;
  var series = [];
  while (i < count) {
    var x = baseval;
    var y =
      Math.floor(Math.random() * (yrange.max - yrange.min + 1)) + yrange.min;

    series.push([x, y]);
    baseval += 86400000;
    i++;
  }
  return series;
}


// Total Events mixed chart
var options89 = {
      chart:{
        height:175,
        type:'area',
        stacked:true,
        toolbar:{
            show:false
        },
        events: {
          selection: function(chart, e) {
            console.log(new Date(e.xaxis.min) )
          }
        },
      },
      colors:[WingoAdminConfig.primary],
      dataLabels:{
          enabled:false
      },
      grid: {
          borderColor: 'transparent',
          padding: {
              left: -10,
              right: 0,
              bottom: -15,
              top: -40
          }
      },
      stroke: {
        curve: 'straight',
        width: [ 2 ]
      },
      series: [
      {
          name: 'South',
          data: [
            [1351202400000,37.30],
            [1351338000000,36.60],
            [1351424400000,39.50],
            [1351710800000,32.55],
            [1351870000000,32.55],
            [1352056400000,35.60],
            [1352342800000,30.45],
            [1352629200000,39.60],
            [1352815600000,37.50],
            [1352924000000,38.30],
            [1353061200000,36.20],
            [1353134000000,37.25],
            [1353220400000,37.22],
            [1353479600000,33.30],
            [1353566000000,34.23],
            [1353632400000,32.30],
            [1353757200000,34.23],
            [1353857200000,36.30],
            [1353957200000,38.28],
            [1354021500000,37.10],
            [1354175600000,39.28],
            [1354362000000,36.22],
            [1354548400000,36.22],
            [1354634800000,38.55],
            [1354794000000,36.22],
            [1354980400000,40.50],
            [1355166800000,40.80],
            [1355253200000,39.50],
            [1355439600000,37.45],
            [1355698800000,37.51],
            [1355885200000,33.40],
            [1355985200000,36.40],
            [1356085200000,39.40],
        ]
        }
        
      ],
      fill: {
        type: 'gradient',
        gradient: {
          opacityFrom: 0.5,
          opacityTo: 0.2,
        }
      },
      legend: {
        show: false,
        position: 'top',
        horizontalAlign: 'right'
      },
      yaxis: {
        low: 0,
        offsetX: 0,
        offsetY: 0,
        labels: {
            low: 0,
            offsetX: 0,
            show: false,
        },
        axisBorder: {
            low: 0,
            offsetX: 0,
            show: false,
        },
        axisTicks: {
            show: false,
        },
      },
      xaxis: {
        type: 'datetime',
        low: 0,
        offsetX: 0,
        offsetY: 0,
        labels: {
            low: 0,
            offsetX: 0,
            show: false,
        },
        axisBorder: {
            low: 0,
            offsetX: 0,
            show: false,
        },
        axisTicks: {
            show: false,
        },
      },
      responsive: [        
        {
          breakpoint:1300,
          options: {
            chart: {
              height:140
            }           
          }
        }
      ]
    }

    var chart89 = new ApexCharts(
      document.querySelector("#mix1"),
      options89
    );

    chart89.render();

//mix-bar
new Chartist.Bar('.small-mix', {
    labels: ['Q1', 'Q2', 'Q3', 'Q4', 'Q5', 'Q6', 'Q7', 'Q8', 'Q9', 'Q10', 'Q11', 'Q12', 'Q13', 'Q14', 'Q15', 'Q16', 'Q17', 'Q18', 'Q19', 'Q20', 'Q21', 'Q22', 'Q23'],
    series: [
        [13.6, 11, 4, 8, 4, 15, 18, 10, 8, 10, 8, 4, 6, 11, 13.6, 11, 4, 8, 4, 15, 18, 10, 8, 10, 8, 4, 6, 11, 13.6, 11, 4, 8, 4, 15, 18, 10, 18]
    ]
}, {
    low: 0,
    offset: 0,
    chartPadding: {
        top: 0,
        left: 0,
        right: 0,
        bottom: 0
    },
    axisX: {
        low: 0,
        showGrid: false,
        showLabel: false,
        offset: 0
    },
    axisY: {
        low: 0,
        showGrid: false,
        showLabel: false,
        offset: 0,
        labelInterpolationFnc: function(value) {
            return (value / 1000) + 'k';
        }
    }
}).on('draw', function(data) {
    if(data.type === 'bar') {
        data.element.attr({
            style: 'stroke-width: 5px'
        });
    }
});
