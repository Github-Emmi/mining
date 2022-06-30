/**
* cube.js generated using cube cli tool
* @date: 27th-Mar-2018
**/

$(function () {

    $('select[value]').each(function () {
        $(this).val($(this).attr('value'))
    })

    $(window).scroll(function () {
        let current_pos = $(window).scrollTop()
        if(current_pos > pos) {
            $('.main-header').addClass('main-header--active')
            return
        }
        $('.main-header').removeClass('main-header--active')
    })

    $('.dashboard-header__bar').click(function (e) {
        e.preventDefault()
        $('.main-container__sidebar').toggleClass('main-container__sidebar--is-active')
    })

    $('#nav-opener').click(function(e){
        e.preventDefault()
        $('.main-header__nav').toggleClass('hide-s')
    })

    let pos = $('.main-header').height()

    $('.slide-box__slider').bxSlider({
        auto: true,
        autoHover: true
    })
})

//AOS.init()