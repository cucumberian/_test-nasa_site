$(document).on('ready', function() {
    
 $('.slider-main').slick({
    slidesToShow: 1,
    slidesToScroll: 1,
    arrows: false,
    fade: true,
    asNavFor: '.slider-nav'
  });


  const get_sliders_count = () => {
    const breakpoint = 720;
    const large_size = 165;
    const small_size = 80;
    const window_width = $(window).width();
    const slider_nav = $('.slider-nav');
    const slider_nav_width = slider_nav.width();
    
    let slider_width = large_size;

    if (window_width < breakpoint) {
      slider_width = small_size;
    }

    const element_count = Math.floor(slider_nav_width / (slider_width + 10)) - 1;

    console.log(slider_nav_width, slider_width, element_count);
    return element_count;
  };

  $('.slider-nav').slick({
    slidesToShow: get_sliders_count(170),
    slidesToScroll: 1,
    asNavFor: '.slider-main',
    dots: false,
    arrows: ($(window).width() < 720) ? false : true,
    centerMode: true,
    focusOnSelect: true
  });

});