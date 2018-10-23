$(document).scroll(function() {
    $('nav').toggleClass('brighten', $(this).scrollTop() > 675)
    // $('#bottom-nav').toggleClass('brighten', $(this).scrollTop() > 675)
    
    if($(this).scrollTop() > 675) {
        $('.light-img').addClass('hidden')
        $('.dark-img').removeClass('hidden')
        $('.nav-link').css('color', '#000')
        $('#menu-icon').css('color', '#000')
        $('#bottom-nav').addClass('bottom-nav--light')
    } else {
        $('.light-img').removeClass('hidden')
        $('.dark-img').addClass('hidden')
        $('.nav-link').css('color', '#fff')
        $('#menu-icon').css('color', '#fff')
        $('#bottom-nav').removeClass('bottom-nav--light')
    }
});

