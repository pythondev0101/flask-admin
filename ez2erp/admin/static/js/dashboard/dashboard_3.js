

// project goal
var options = {
  series: [{
    name: 'Goal',
    data: [20, 100, 40, 30, 50, 80, 33],
  }],
  chart: {
    height: 410,
    type: 'radar',
    toolbar: {
      show: false,
    },
  },   
   plotOptions: {
      radar: {
        size: 140,
        polygons: {
          strokeColors: '#e9e9e9',
          fill: {
            colors:['#edf3ff', '#fff']
          }
        }
      }
    },
    stroke: {
        width: 3,
        curve: 'smooth',
    },
   colors:[WingoAdminConfig.primary],
   markers: {
    size:5,
    colors: ['#fff'],
    strokeColor: WingoAdminConfig.primary,
    strokeWidth: 2, 
    hover: {
      size: 5
    } 
  },
  yaxis: {
    tickAmount: 7,   
  },
  responsive: [
    {
      breakpoint:1661,
      options: {
        chart: {
          height:380
        }
      },
    },
    {
      breakpoint:992,
      options: {
        chart: {
          height:365
        }
      },
    },
    {
      breakpoint:575,
      options: {
        chart: {
          height:350
        }
      },
    },
  ],
  xaxis: {
    categories: ['January', 'February', 'March', 'April', 'May', 'June','July']
  }
  };

  var chart = new ApexCharts(document.querySelector("#radar-chart"), options);
  chart.render();      





  // Earnings  chart
   var options = {
          series: [ {
          name: 'Highest',
          data: [50, 40, 30, 35, 50, 20, 30, 40, 15]
        }, {
          name: 'Lowest',
          data: [30, 20, 60, 50, 40, 60, 40, 60, 40]
        }],
          chart: {
          type: 'bar',
          height: 365,
          toolbar: {
          show:false,
        },
        },
        plotOptions: {
          bar: {
            horizontal: false,
            columnWidth: '30%',            
          },
        },
        dataLabels: {
          enabled: false
        },
        stroke: {
          show: true,
          width: 2,
          colors: ['transparent']
        },
        legend:{
          show:false,
        },
        colors:[WingoAdminConfig.primary,'#dce8ff'],
        states: {          
          hover: {
            filter: {
              type: 'darken',
              value: 1,
            }
          }           
        },
        yaxis: {
          min: 10,
          max: 60,
          tooltip:{
            enabled: true
          },
          
          labels: {            
            formatter: function (value) {
              return value + "k";
            },
          },
        },       
       
        xaxis: {
          categories: ['2010','2011','2012','2013','2014','2015','2016','2017','2018','2019' ],
          axisBorder: {
              show: false
            },
          axisTicks: {
            show: false
          } ,               
        },   
        responsive: [
        {
          breakpoint:1661,
          options: {
            chart: {
              height:300
            }
          },
        }        
        ],                   
        };

        var chart = new ApexCharts(document.querySelector("#earnings-chart"), options);
        chart.render();