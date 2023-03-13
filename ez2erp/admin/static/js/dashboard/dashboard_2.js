// business growth
var options = {
    series: [{
      name: "Growth",
      data: [20,30,18,30, 20, 30,40]
      },
      {
        name: 'Growth',
        data: [30, 22, 15, 21, 23,18,27]
      },
  ],
  chart: {
    height:315,
    type: 'line',
    zoom: {
      enabled: false
    },
    toolbar: {
      show:false,
    },
  },
  dataLabels: {
    enabled: false
  },
  legend:{
    show:false,
  },
  stroke: {
    curve: 'straight'
  },        
  colors: [WingoAdminConfig.primary, '#47cf60'],  
  markers: {
    size: 5,
    hover: {
      sizeOffset:1
    }
  },
  yaxis: {
    labels:{
      offsetX: 14,
      offsetY: -5   
    },
    tooltip: {
      enabled: true
    },
    labels: {
      formatter: function (value) {
        return value + "k";
      },
    },
  },
  xaxis: {
    categories: ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'July'],
    axisBorder: {
        show: false
      },
    axisTicks: {
      show: false
    }
  },
  responsive: [
        {
          breakpoint:1501,
          options: {
            chart: {
              height:250
            }
          },
        },
        {
          breakpoint:1366,
          options:{
            chart:{
              height:385
            }
          },
        },
        {
          breakpoint:992,
          options:{
            chart:{
              height:365
            }
          },
        }
    ],
  };
  var chart = new ApexCharts(document.querySelector("#business-chart"), options);
  chart.render();
    

//redial first charts
 var options17 = {
  chart:{
    height: 195 ,
    type: "radialBar",
  },
  series:[30],
  colors:[WingoAdminConfig.secondary],
  plotOptions:{
    radialBar:{
      hollow:{
        margin:20,
        size:"70%",
        background:"#f7316433",
        image:'../assets/images/dashboard-2/c_2.png',
        imageWidth:30,
        imageHeight:30,
        imageClipped:false,
      },
      dataLabels: {
        name:{
          offsetY:-10,
          color:"#fff",
          fontSize:"13px",
          show:false
        },
        value:{
          color:"#fff",
          fontSize:"30px",
          show: false
        }
      }
    }
  },
  fill: {
    type: "gradient",
    gradient: {
      shade: "dark",
      type: "vertical",
      gradientToColors: ["#efb9c7"],
      stops: [0, 100]
    }
  },
  responsive: [
      {
        breakpoint:1501,
        options: {
          chart: {
            height:200
          }
        }
      }
    ],
 
  labels: ["Progress"]
};

var chart17 = new ApexCharts(document.querySelector("#chart-update-2"), 
  options17
  );

chart17.render();


// slider section

$(document).ready(function() {

  var sync1 = $("#sync1");
  var sync2 = $("#sync2");
  var slidesPerPage = 4; //globaly define number of elements per page
  var syncedSecondary = true;

  sync1.owlCarousel({
    items : 1,
    slideSpeed : 2000,
    nav: true,
    autoplay: false,
    dots: false,
    loop: true,
    responsiveRefreshRate : 200,
    navText: ['<svg width="100%" height="100%" viewBox="0 0 11 20"><path style="fill:none;stroke-width: 1px;stroke: #000;" d="M9.554,1.001l-8.607,8.607l8.607,8.606"/></svg>','<svg width="100%" height="100%" viewBox="0 0 11 20" version="1.1"><path style="fill:none;stroke-width: 1px;stroke: #000;" d="M1.054,18.214l8.606,-8.606l-8.606,-8.607"/></svg>'],
  }).on('changed.owl.carousel', syncPosition);

  sync2
    .on('initialized.owl.carousel', function () {
      sync2.find(".owl-item").eq(0).addClass("current");
    })
    .owlCarousel({
    items : slidesPerPage,
    dots: false,
    nav: true,
    smartSpeed: 200,
    slideSpeed : 500,
    slideBy: slidesPerPage, //alternatively you can slide by 1, this way the active slide will stick to the first item in the second carousel
    responsiveRefreshRate : 100
  }).on('changed.owl.carousel', syncPosition2);

  function syncPosition(el) {
    var count = el.item.count-1;
    var current = Math.round(el.item.index - (el.item.count/2) - .5);
    
    if(current < 0) {
      current = count;
    }
    if(current > count) {
      current = 0;
    }
    
    //end block
    sync2
      .find(".owl-item")
      .removeClass("current")
      .eq(current)
      .addClass("current");
    var onscreen = sync2.find('.owl-item.active').length - 1;
    var start = sync2.find('.owl-item.active').first().index();
    var end = sync2.find('.owl-item.active').last().index();
    
    if (current > end) {
      sync2.data('owl.carousel').to(current, 100, true);
    }
    if (current < start) {
      sync2.data('owl.carousel').to(current - onscreen, 100, true);
    }
  }
  
  function syncPosition2(el) {
    if(syncedSecondary) {
      var number = el.item.index;
      sync1.data('owl.carousel').to(number, 100, true);
    }
  }
  
  sync2.on("click", ".owl-item", function(e){
    e.preventDefault();
    var number = $(this).index();
    sync1.data('owl.carousel').to(number, 300, true);
  });
});
    
//redial first charts
var options16 = {
  chart: {
    height: 195,
    type: "radialBar",
  },
  series: [55],
  colors: [WingoAdminConfig.primary],
  plotOptions: {
    radialBar: {
      hollow: {
        margin: 20,
        size: "70%",
        background: "#4d8aff33",
              image: '../assets/images/dashboard-2/c_1.png',
              imageWidth: 30,
              imageHeight: 30,
              imageClipped: false,
      },
      dataLabels: {
        name: {
          offsetY: -10,
          color: "#fff",
          fontSize: "13px",
          show:false
        },
        value: {
          color: "#fff",
          fontSize: "30px",
          show: false
        }
      }
    }
  },
  fill: {
    type: "gradient",
    gradient: {
      shade: "dark",
      type: "vertical",
      gradientToColors: ["#b2c4e6"],
      stops: [0, 100]
    }
  },
   responsive: [
      {
        breakpoint:1501,
        options: {
          chart: {
            height:200
          }
        }
      }
    ],
  labels:["Progress"]
};
var chart16 = new ApexCharts(document.querySelector("#chart-update-1"), 
  options16
);

chart16.render();

//redial-last updation
var options15 = {
  chart: {
    height:195,
    type: "radialBar",
  },
  series: [67],
  colors: ["#46d15e"],
  plotOptions: {
    radialBar: {
      hollow: {
        margin: 20,
        size: "70%",
        background: "#46d15e33",
              image: '../assets/images/dashboard-2/c_3.png',
              imageWidth: 30,
              imageHeight: 30,
              imageClipped: false,
      },
      dataLabels: {
        name: {
          offsetY: -10,
          color: "#fff",
          fontSize: "13px",
          show:false
        },
        value: {
          color: "#fff",
          fontSize: "30px",
          show: false
        }
      }
    }
  },
  fill: {
    type: "gradient",
    gradient: {
      shade: "dark",
      type: "vertical",
      gradientToColors: ["#c4f3cc"],
      stops: [0, 100]
    }
  },
  responsive: [
      {
        breakpoint:1501,
        options: {
          chart: {
            height:200
          }
        }
      }
    ],
 
  labels: ["Progress"]
};

var chart15 = new ApexCharts(document.querySelector("#chart-update"), 
  options15
  );

chart15.render();
// cmorries


var morris_chart = {
    init: function() {
        $(function() {
            Morris.Bar({
                element: 'github-issues',
                data:[{
                    x:"A1",
                    y:25,
                    z:null
                },
                    {
                      x: "A2",
                      y:19,
                      z: null
                    },
                    {
                      x: "A3",
                      y:12,
                      z: null
                    },
                    {
                        x: "A4",
                        y:20,
                        z: null
                    },
                    {
                        x: "A5",
                        y:25,
                        z: null
                    },
                    {
                        x: "A6",
                        y:32,
                        z: null

                    },
                    {
                        x: "A7",
                        y: null,
                        z:38
                    },
                    {
                        x: "A8",
                        y:31,
                        z: null
                    },
                    {
                        x: "A9",
                        y:35,
                        z: null
                    },
                    {
                        x: "A10",
                        y:38,
                        z: null
                    },
                    {
                        x: "A11",
                        y:30,
                        z: null
                    },
                    {
                        x: "A12",
                        y:35,
                        z:25,
                        q:20
                    },
                    {
                        x: "A13",
                        y:18,
                        z: null
                    },
                    {
                        x: "A14",
                        y:21,
                        z: null
                    },
                    {
                        x: "A15",
                        y:30,
                        z: null
                    },
                    {
                        x: "A16",
                        y: null,
                        z:38
                    },
                    {
                        x: "A17",
                        y:17,
                        z: null
                    },
                    {
                        x: "A18",
                        y:25,
                        z: null
                    },
                    {
                        x: "A19",
                        y:38,
                        z: null
                    },
                    {
                        x: "A20",
                        y:25,
                        z: null
                    },
                    {
                        x: "A21",
                        y:30,
                        z: null
                    },
                    {
                        x: "A22",
                        y:30,
                        z: null
                    },
                    {
                        x: "A23",
                        y:38,
                        z: null
                    },
                    {
                        x: "A24",
                        y: null,
                        z:33
                    },
                    {
                        x: "A25",
                        y:23,
                        z: null
                    },
                    {
                        x: "A26",
                        y:12,
                        z: null
                    },
                    {
                        x: "A27",
                        y:21,
                        z: null
                    },
                    {
                        x: "A28",
                        y:18,
                        z: null
                    },
                    {
                        x: "A29",
                        y:15,
                        z: null
                    },
                    {
                        x: "A30",
                        y: 17,
                        z:null
                    },
                    {
                        x: "A31",
                        y:38,
                        z: null
                    },
                    {
                        x: "A32",
                        y:31,
                        z: null
                    },
                    {
                        x: "A33",
                        y: null,
                        z:20
                    },
                    {
                        x: "A34",
                        y:38,
                        z: null
                    },
                    {
                        x: "A35",
                        y:35,
                        z: null
                    },
                    {
                        x: "A36",
                        y:28,
                        z: null
                    },
                    {
                        x: "A37",
                        y:20,
                        z: null
                    },
                    {
                        x: "A38",
                        y:23,
                        z: null
                    },
                    {
                        x: "A39",
                        y:28,
                        z: null
                    },
                    {
                        x: "A40",
                        y:25,
                        z: null
                    },
                    {
                        x: "A41",
                        y: null,
                        z:38
                    },
                    {
                        x: "A42",
                        y:35,
                        z: null
                    },
                    {
                        x: "A43",
                        y:28,
                        z: null
                    },
                    {
                        x: "A44",
                        y:33,
                        z: null
                    }
                   
                   
                    ],

                xkey: "x",
                ykeys: ["y", "z" ,"q"],
                labels: ["Y", "Z" ],
                ymax: 60,
                 numLines: 6,
                 ymin: 10,
                  resize:true,
                  grid:false,
                  barRadius: [5, 5, 5, 5],
                  postUnits:'K',
                  hideHover:'true',
                  xLabels:'day',
                barColors: [WingoAdminConfig.primary ,'#a6c4ff','#dbe8fe' ],
                stacked: !0
            });
        });
    }
};
(function($) {
    "use strict";
    morris_chart.init()
})(jQuery);
// small charts in preview details section

new Chartist.Line('.ct-chart1', {
  labels: [1, 2, 3],
  series: [
    [2, 4,2]
  ]
}, {
   low: 0,
   chartPadding: 5,
   showArea: true,
   showPoint: true,
   fullWidth: true,
   width: 130,
   height: 100,

   axisX: {
   offset: 0
  },
  axisY: {
    offset: 0
  },
  
  lineSmooth: Chartist.Interpolation.simple({
    divisor: 2
  }),
   
});
// second chart
new Chartist.Line('.ct-chart2', {
  labels: [1, 2, 3],
  series: [
    [4, 2,4]
  ]
}, {
  low: 0,
  chartPadding: 5,
   showArea: true,
   showPoint: true,
  fullWidth: true,
  width: 130,
  height: 100,
   axisX: {
    offset: 0
  },
  axisY: {
    offset: 0
  },
  lineSmooth: Chartist.Interpolation.simple({
    divisor: 2,

  }),
});
// thirs charts in chartist chart
new Chartist.Line('.ct-chart3', {
  labels: [1,2,3],
  series: [
    [4,3,4]
  ]
}, {
  low: 0,
  chartPadding: 5,
   showArea: true,
   showPoint: true,
  fullWidth: true,
  width: 130,
  height: 100,
   axisX: {
    offset: 0
  },
  axisY: {
    offset: 0
  },
  lineSmooth: Chartist.Interpolation.simple({
    divisor: 2,

  }),
});

// fourth charts in chartist chart
new Chartist.Line('.ct-chart4', {
  labels: [1,2,3],
  series: [
    [2,4,1]
  ]
}, {
  low: 0,
  chartPadding: 5,
   showArea: true,
   showPoint: true,
  fullWidth: true,
  width: 130,
  height: 100,
   axisX: {
    offset: 0
  },
  axisY: {
    offset: 0
  },
  lineSmooth: Chartist.Interpolation.simple({
    divisor: 2,

  }),
});
// second slider

new Chartist.Line('.ct-chart5', {
  labels: [1, 2, 3],
  series: [
    [2, 4,2]
  ]
}, {
   low: 0,
   chartPadding: 5,
   showArea: true,
   showPoint: true,
   fullWidth: true,
   width: 130,
   height: 100,

   axisX: {
   offset: 0
  },
  axisY: {
    offset: 0
  },
  
  lineSmooth: Chartist.Interpolation.simple({
    divisor: 2
  }),
   
});
// second chart
new Chartist.Line('.ct-chart6', {
  labels: [1, 2, 3],
  series: [
    [4, 2,4]
  ]
}, {
  low: 0,
  chartPadding: 5,
   showArea: true,
   showPoint: true,
  fullWidth: true,
  width: 150,
  height: 100,
   axisX: {
    offset: 0
  },
  axisY: {
    offset: 0
  },
  lineSmooth: Chartist.Interpolation.simple({
    divisor: 2,

  }),
});
// thirs charts in chartist chart
new Chartist.Line('.ct-chart7', {
  labels: [1,2,3],
  series: [
    [4,3,4]
  ]
}, {
  low: 0,
  chartPadding: 5,
   showArea: true,
   showPoint: true,
  fullWidth: true,
  width: 150,
  height: 100,
   axisX: {
    offset: 0
  },
  axisY: {
    offset: 0
  },
  lineSmooth: Chartist.Interpolation.simple({
    divisor: 2,

  }),
});

// fourth charts in chartist chart
new Chartist.Line('.ct-chart8', {
  labels: [1,2,3],
  series: [
    [2,4,1]
  ]
}, {
  low: 0,
  chartPadding: 5,
   showArea: true,
   showPoint: true,
  fullWidth: true,
  width: 150,
  height: 100,
   axisX: {
    offset: 0
  },
  axisY: {
    offset: 0
  },
  lineSmooth: Chartist.Interpolation.simple({
    divisor: 2,
  }),
});

