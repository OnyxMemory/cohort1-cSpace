$(document).scroll(function() {
    $('nav').toggleClass('brighten', $(this).scrollTop() > 675)
    
    if($(this).scrollTop() > 675) {
        $('.light-img').addClass('hidden')
        $('.dark-img').removeClass('hidden')
    } else {
        $('.light-img').removeClass('hidden')
        $('.dark-img').addClass('hidden')
    }
});





