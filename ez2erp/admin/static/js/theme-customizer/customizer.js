if(localStorage.getItem("color"))
    $("#color" ).attr("href", "../assets/css/"+localStorage.getItem("color")+".css" );
if(localStorage.getItem("dark"))
    $("body").attr("class", "dark-only");
$('<div class="customizer-links"> <div class="nav flex-column nac-pills" id="c-pills-tab"> <a class="nav-link" id="c-pills-home-tab" data-bs-toggle="pill" href="#layout-setting"> <div class="settings"> <svg enable-background="new 0 0 512 512" viewbox="0 0 512 512" xmlns="http://www.w3.org/2000/svg"> <path d="m464.866 192.8h-10.87c-3.531-11.05-7.986-21.784-13.323-32.097l7.698-7.698c18.665-18.645 18.165-48.525.006-66.665l-22.711-22.71c-18.129-18.153-48.015-18.679-66.665-.007l-7.704 7.704c-10.313-5.336-21.048-9.792-32.097-13.323v-10.871c0-25.989-21.144-47.133-47.134-47.133h-32.133c-25.989 0-47.133 21.144-47.133 47.133v10.871c-11.049 3.53-21.784 7.986-32.097 13.323l-7.697-7.697c-18.613-18.635-48.498-18.198-66.664-.006l-22.713 22.711c-18.152 18.132-18.677 48.014-.006 66.665l7.704 7.704c-5.337 10.313-9.792 21.046-13.323 32.097h-10.87c-25.989-.001-47.134 21.143-47.134 47.132v32.134c0 25.989 21.145 47.133 47.134 47.133h10.87c3.531 11.05 7.986 21.784 13.323 32.097l-7.698 7.698c-18.665 18.645-18.165 48.525-.006 66.665l22.711 22.71c18.129 18.153 48.015 18.679 66.665.007l7.704-7.704c10.313 5.336 21.048 9.792 32.097 13.323v10.871c0 25.989 21.145 47.133 47.134 47.133h32.133c25.989 0 47.134-21.144 47.134-47.133v-10.871c11.049-3.53 21.784-7.986 32.097-13.323l7.697 7.697c18.613 18.635 48.497 18.198 66.664.006l22.713-22.712c18.152-18.132 18.677-48.014.006-66.665l-7.704-7.704c5.337-10.313 9.792-21.046 13.323-32.097h10.87c25.989 0 47.134-21.144 47.134-47.133v-32.134c-.001-25.987-21.146-47.131-47.135-47.131zm-208.866 174.6c-61.427 0-111.4-49.974-111.4-111.4s49.973-111.4 111.4-111.4 111.4 49.974 111.4 111.4-49.973 111.4-111.4 111.4z"></path> </svg> </div></a> <a class="nav-link" id="c-pills-profile-tab" data-bs-toggle="pill" href="#color-setting"> <div class="settings color-settings"> <svg enable-background="new 0 0 505.299 505.299" viewbox="0 0 505.299 505.299" xmlns="http://www.w3.org/2000/svg"> <g id="XMLID_31_"> <path id="XMLID_1_" d="m239.496 384.74v120.559c49.481-3.235 95.86-22.446 133.137-55.147l-85.248-85.247c-14.076 10.571-30.46 17.358-47.889 19.835z"></path> <path id="XMLID_1531_" d="m212.93 176.436 11.53-1.27 17.378-119.364h-17.342c-55.071 0-107.114 19.664-148.136 55.65l85.251 85.252c14.929-11.232 32.412-18.185 51.319-20.268z"></path> <path id="XMLID_1536_" d="m328.772 293.157c-2.186 18.604-9.102 35.809-20.179 50.529l85.252 85.252c35.987-41.022 55.651-93.064 55.651-148.136v-17.341l-120.725 17.57v12.126z"></path> <path id="XMLID_1540_" d="m140.395 217.913-85.247-85.247c-32.702 37.277-51.913 83.655-55.148 133.137h120.559c2.477-17.429 9.263-33.814 19.836-47.89z"></path> <path id="XMLID_1541_" d="m76.36 450.151c37.276 32.701 83.654 51.912 133.136 55.147v-120.558c-17.429-2.478-33.812-9.265-47.889-19.836z"></path> <path id="XMLID_1542_" d="m120.559 295.803h-120.559c3.235 49.481 22.446 95.859 55.147 133.136l85.247-85.247c-10.572-14.077-17.358-30.461-19.835-47.889z"></path> <path id="XMLID_1543_" d="m385.809 14.537h59.999v149.906h-59.999z" transform="matrix(.707 -.707 .707 .707 58.507 320.23)"></path> <path id="XMLID_1548_" d="m496.513 8.787-.001-.001c-11.715-11.715-30.71-11.715-42.426 0l-17.064 17.064 42.427 42.427 17.064-17.065c11.715-11.715 11.715-30.71 0-42.425z"></path> <path id="XMLID_1574_" d="m198.89 306.409h42.426l153.206-153.206-42.426-42.427-153.206 153.206z"></path> </g> </svg> </div></a> </div></div><div class="customizer-contain"> <div class="tab-content" id="c-pills-tabContent"> <div class="customizer-header"> <i class="icofont-close icon-close"></i> <h5>Customizer</h5> <p class="mb-0">Customize &amp; Preview Real Time</p></div><div class="customizer-body custom-scrollbar"> <div class="tab-pane fade show active" id="layout-setting"> <h6>Dashboard Type</h6> <div id="dashboardtype" class="carousel slide dashboard-type" data-bs-ride="carousel"> <div class="carousel-inner"> <div class="carousel-item active"> <div class="dashboard-box" data-attr="compact-layout"> <div class="img-wrraper"><img class="img-fluid" src="../assets/images/landing/demo/1.jpg" alt=""></div><div class="title-wrraper"> <h3>Defaul layout</h3> </div></div></div><div class="carousel-item"> <div class="dashboard-box" data-attr="compact-sidebar"> <div class="img-wrraper"><img class="img-fluid" src="../assets/images/landing/demo/1.jpg" alt=""></div><div class="title-wrraper"> <h3>Compact layout</h3> </div></div></div><div class="carousel-item"> <div class="dashboard-box" data-attr="material-type"> <div class="img-wrraper"><img class="img-fluid" src="../assets/images/landing/demo/1.jpg" alt=""></div><div class="title-wrraper"> <h3>Material layout</h3> </div></div></div></div><button class="carousel-control-prev" type="button" data-bs-target="#dashboardtype" data-bs-slide="prev"> <span class="carousel-control-prev-icon" aria-hidden="true"></span> </button> <button class="carousel-control-next" type="button" data-bs-target="#dashboardtype" data-bs-slide="next"> <span class="carousel-control-next-icon" aria-hidden="true"></span> </button> </div><h6>Layout Type</h6> <ul class="main-layout layout-grid"> <li class="active" data-attr="ltr"> <div class="header bg-light"> <ul> <li></li><li></li><li></li></ul> </div><div class="body"> <ul> <li class="bg-light sidebar"></li><li class="bg-light body"><span class="badge badge-primary">LTR</span></li></ul> </div></li><li data-attr="rtl"> <div class="header bg-light"> <ul> <li></li><li></li><li></li></ul> </div><div class="body"> <ul> <li class="bg-light body"><span class="badge badge-primary">RTL</span></li><li class="bg-light sidebar"></li></ul> </div></li><li class="box-layout" data-attr="ltr"> <div class="header bg-light"> <ul> <li></li><li></li><li></li></ul> </div><div class="body"> <ul> <li class="bg-light sidebar"></li><li class="bg-light body"><span class="badge badge-primary">Box</span></li></ul> </div></li></ul> <h6>Sidebar Type</h6> <ul class="sidebar-type layout-grid"> <li data-attr="normal-sidebar"> <div class="header bg-light"> <ul> <li></li><li></li><li></li></ul> </div><div class="body"> <ul> <li class="bg-dark sidebar"></li><li class="bg-light body"></li></ul> </div></li><li data-attr="compact-layout"> <div class="header bg-light"> <ul> <li></li><li></li><li></li></ul> </div><div class="body"> <ul> <li class="bg-dark sidebar compact"></li><li class="bg-light body"></li></ul> </div></li></ul> <h6>Sidebar settings</h6> <ul class="sidebar-setting layout-grid"> <li class="active" data-attr="default-sidebar"> <div class="header bg-light"> <ul> <li></li><li></li><li></li></ul> </div><div class="body bg-light"><span class="badge badge-primary">Default</span></div></li><li data-attr="border-sidebar"> <div class="header bg-light"> <ul> <li></li><li></li><li></li></ul> </div><div class="body bg-light"><span class="badge badge-primary">Border</span></div></li><li data-attr="iconcolor-sidebar"> <div class="header bg-light"> <ul> <li></li><li></li><li></li></ul> </div><div class="body bg-light"><span class="badge badge-primary">icon Color</span></div></li></ul> </div><div class="tab-pane fade" id="color-setting"> <h6>Light layout</h6> <ul class="layout-grid customizer-color"> <li class="color-layout" data-attr="color-1" data-primary="#4d8aff" data-secondary="#f73164"> <div></div></li><li class="color-layout" data-attr="color-2" data-primary="#2a9d8f" data-secondary="#f4a261"> <div></div></li><li class="color-layout" data-attr="color-3" data-primary="#e07a5f" data-secondary="#81b29a"> <div></div></li><li class="color-layout" data-attr="color-4" data-primary="#f15bb5" data-secondary="#9b5de5"> <div></div></li><li class="color-layout" data-attr="color-5" data-primary="#f95738" data-secondary="#fcbf49"> <div></div></li><li class="color-layout" data-attr="color-6" data-primary="#06aed5" data-secondary="#086788"> <div></div></li></ul> <h6>Dark Layout</h6> <ul class="layout-grid customizer-color dark"> <li class="color-layout" data-attr="color-1" data-primary="#4d8aff" data-secondary="#f73164"> <div></div></li><li class="color-layout" data-attr="color-2" data-primary="#2a9d8f" data-secondary="#f4a261"> <div></div></li><li class="color-layout" data-attr="color-3" data-primary="#e07a5f" data-secondary="#81b29a"> <div></div></li><li class="color-layout" data-attr="color-4" data-primary="#f15bb5" data-secondary="#9b5de5"> <div></div></li><li class="color-layout" data-attr="color-5" data-primary="#f95738" data-secondary="#fcbf49"> <div></div></li><li class="color-layout" data-attr="color-6" data-primary="#06aed5" data-secondary="#086788"> <div></div></li></ul> <h6>Mix Layout</h6> <ul class="layout-grid customizer-mix"> <li class="color-layout active" data-attr="light-only"> <div class="header bg-light"> <ul> <li></li><li></li><li></li></ul> </div><div class="body"> <ul> <li class="bg-light sidebar"></li><li class="bg-light body"></li></ul> </div></li><li class="color-layout" data-attr="dark-sidebar"> <div class="header bg-light"> <ul> <li></li><li></li><li></li></ul> </div><div class="body"> <ul> <li class="bg-dark sidebar"></li><li class="bg-light body"></li></ul> </div></li><li class="color-layout" data-attr="dark-only"> <div class="header bg-dark"> <ul> <li></li><li></li><li></li></ul> </div><div class="body"> <ul> <li class="bg-dark sidebar"></li><li class="bg-dark body"></li></ul> </div></li></ul> </div></div></div></div>').appendTo($('body'));
(function() {
})();

//live customizer js
$(document).ready(function() {
    $(".customizer-links").click(function(){
        $(".customizer-contain").addClass("open");
        $(".customizer-links").addClass("open");
    });

    $(".close-customizer-btn").on('click', function() {
        $(".floated-customizer-panel").removeClass("active");
    });

    $(".customizer-contain .icon-close").on('click', function() {
        $(".customizer-contain").removeClass("open");
        $(".customizer-links").removeClass("open");
    });

    $(".customizer-color li").on('click', function() {
        $(".customizer-color li").removeClass('active');
        $(this).addClass("active");
        var color = $(this).attr("data-attr");
        var primary = $(this).attr("data-primary");
        var secondary = $(this).attr("data-secondary");
        localStorage.setItem("color", color);
        localStorage.setItem("primary", primary);
        localStorage.setItem("secondary", secondary);
        localStorage.removeItem("dark");
        $("#color" ).attr("href", "../assets/css/"+color+".css" );
        $(".dark-only").removeClass('dark-only');
        location.reload(true);
    });

    $(".customizer-color.dark li").on('click', function() {
        $(".customizer-color.dark li").removeClass('active');
        $(this).addClass("active");
        $("body").attr("class", "dark-only");
        localStorage.setItem("dark", "dark-only");
    });


    $(".customizer-mix li").on('click', function() {
        $(".customizer-mix li").removeClass('active');
        $(this).addClass("active");
        var mixLayout = $(this).attr("data-attr");
        $("body").attr("class", mixLayout);
    });


    $('.sidebar-setting li').on('click', function() {
        $(".sidebar-setting li").removeClass('active');
        $(this).addClass("active");
        var sidebar = $(this).attr("data-attr");
        $(".main-nav").attr("sidebar-layout",sidebar);
    });

    $('.sidebar-main-bg-setting li').on('click', function() {
        $(".sidebar-main-bg-setting li").removeClass('active')
        $(this).addClass("active")
        var bg = $(this).attr("data-attr");
        $(".main-nav").attr("class", "main-nav "+bg);
    });


     $('.main-layout li').on('click', function () {
        $(".main-layout li").removeClass('active');
        $(this).addClass("active");
        var layout = $(this).attr("data-attr");
        $("body").attr("class", layout);
        $("html").attr("dir", layout);
    });
    $('.main-layout .box-layout').on('click', function () {
        $(".main-layout .box-layout").removeClass('active');
        $(this).addClass("active");
        var layout = $(this).attr("data-attr");
        $("body").attr("class", "box-layout");
        $("html").attr("dir", layout);
    });

    $('.sidebar-setting li').on('click', function() {
        $(".sidebar-setting li").removeClass('active');
        $(this).addClass("active");
        var sidebar = $(this).attr("data-attr");
        $(".main-nav").attr("sidebar-layout",sidebar);
    });

    $('.sidebar-type li , .dashboard-type .dashboard-box').on('click', function () {
        // $(".sidebar-type li").removeClass('active');
        var type = $(this).attr("data-attr");

        var boxed = "";
        if($(".page-wrapper").hasClass("box-layout")){
            boxed = "box-layout";
        }
        switch (type) {
            case 'compact-layout':{
                $(".page-wrapper").attr("class", "page-wrapper compact-wrapper " + boxed);
                localStorage.setItem('page-wrapper', 'compact-wrapper');
                break;
            }
            case 'compact-sidebar': {
                $(".page-wrapper").attr("class", "page-wrapper compact-sidebar" + boxed);
                localStorage.setItem('page-wrapper', 'compact-wrapper compact-sidebar');
                break;
            }
            case 'normal-sidebar':{
                $(".page-wrapper").attr("class", "page-wrapper horizontal-wrapper "+boxed);
                $(".page-body-wrapper").attr("class", "page-body-wrapper horizontal-menu");
                $(".logo-wrapper").find('img').attr('src', '../assets/images/logo/logo.png');
                localStorage.setItem('page-wrapper', 'horizontal-wrapper');
                localStorage.setItem('page-body-wrapper', 'horizontal-menu');
                break;
            }
            case 'material-type':{
                $(".page-wrapper").attr("class", "page-wrapper compact-wrapper material-type"+boxed);               
                localStorage.setItem('page-wrapper', 'compact-wrapper material-type');
                break;
            }
            default: {
                $(".page-wrapper").attr("class", "page-wrapper compact-wrapper " + boxed);
                localStorage.setItem('page-wrapper', 'compact-wrapper');
                break;
            }
        }
        // $(this).addClass("active");
        location.reload(true);
    });


});
