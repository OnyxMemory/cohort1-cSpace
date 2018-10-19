$(document).scroll(function() {
    $('nav').toggleClass('brighten', $(this).scrollTop() > 675)
    
    if($(this).scrollTop() > 675) {
        $('.light-img').addClass('hidden')
        $('.dark-img').removeClass('hidden')
        $('.nav-link').css('color', '#000')
    } else {
        $('.light-img').removeClass('hidden')
        $('.dark-img').addClass('hidden')
        $('.nav-link').css('color', '#fff')
    }
});





