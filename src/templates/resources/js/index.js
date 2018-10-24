$(document).scroll(function() {
    $('nav').toggleClass('brighten', $(this).scrollTop() > 675)
    $('#bottom-nav').toggleClass('hidden', $(this).scrollTop() > 4350)
    console.log($(this).scrollTop())
    
    if($(this).scrollTop() > 675) {
        $('.light-img').addClass('hidden')
        $('.dark-img').removeClass('hidden')
        $('#menu-icon').css('color', '#000')
        $('#bottom-nav').addClass('bottom-nav--light')
        // $('.nav-link-login').removeClass('.nav-link--black')
    } else {
        $('.light-img').removeClass('hidden')
        $('.dark-img').addClass('hidden')
        $('.nav-link').css('color', '#fff')
        $('#menu-icon').css('color', '#fff')
        $('#bottom-nav').removeClass('bottom-nav--light')
        // $('.nav-link-login').addClass('.nav-link--black')
    }
});

