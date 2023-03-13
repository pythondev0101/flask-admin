  $('.pro-slide-single').slick({
    slidesToShow: 1,
    slidesToScroll: 1,
    arrows: false,
    fade: true,
    asNavFor: '.pro-slide-right'
  });
  if ($(window).width() > 1199) {
    $('.pro-slide-right').slick({
      vertical: true,
      verticalSwiping: true,
      slidesToShow: 3,
      slidesToScroll: 1,
      asNavFor: '.pro-slide-single',
      arrows: false,
      infinite: true,
      dots: false,
      centerMode: false,
      focusOnSelect: true
    });
  }else{
    $('.pro-slide-right').slick({
      vertical: false,
      verticalSwiping: false,
      slidesToShow: 3,
      slidesToScroll: 1,
      asNavFor: '.pro-slide-single',
      arrows: false,
      infinite: true,
      centerMode: false,
      dots: false,
      focusOnSelect: true,
      responsive: [
        {
          breakpoint: 1200,
          settings: {
            slidesToShow: 3,
            slidesToScroll: 1,                      
          }
        },
        {
          breakpoint: 576,
          settings: {
            slidesToShow: 3,
            slidesToScroll: 1
          }
        }
      ]
    });
  }


$('.slide-1').slick({
  infinite: true,
  slidesToShow: 1,
  slidesToScroll: 1
});


$('.slide-4').slick({
  dots:false,   
  infinite: true,
  slidesToShow: 4,
  slidesToScroll: 4,
    responsive: [
    {
      breakpoint: 1892,
      settings: {
        slidesToShow: 3,
        slidesToScroll: 1,
        infinite: true,        
      }
    },
    {
      breakpoint: 1533,
      settings: {
        slidesToShow: 2,
        slidesToScroll: 1
      }
    },
    {
      breakpoint: 1150,
      settings: {
        slidesToShow: 1,
        slidesToScroll: 1
      }
    },

    {
      breakpoint: 1007,
      settings: {
        slidesToShow: 2,
        slidesToScroll: 1
      }
    },
    {
      breakpoint: 768,
      settings: {
        slidesToShow: 1,
        slidesToScroll: 1
      }
    },   
  ]
});



 $('.single-item').slick({
    dots: true,
    arrows: false,
  });
  $('.single-item-small').slick({
    dots: false,
    responsive: [       
        {
          breakpoint: 576,
          settings: {
            slidesToShow: 2,
            slidesToScroll: 1
          }
        }
      ]
  });
