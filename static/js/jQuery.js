let width = window.innerWidth;
let height = window.innerHeight;


$('.fullscreen-height').css('height', (height - 60) + 'px');

window.addEventListener('resize', () => {
    let width = window.innerWidth
    let height = window.innerHeight
    $('.fullscreen-height').css('height', (height - 60) + 'px');
});

var showSearchBar = false;
var show = false;
window.addEventListener('dblclick', () => {
    if (showSearchBar == true) {
        showSearchBar = false;
        $('.search-body').removeClass("show-search-bar");
    };
    if (show == true) {
        show = false;
        $('.main-list-little').removeClass("main-list-little-show");
    };
});
$('.btn-main-list-little').click(function () {
    if (showSearchBar == true) {
        showSearchBar = false;
        $('.search-body').removeClass("show-search-bar");
    }
    if (show == false) {
        $('.main-list-little').addClass("main-list-little-show");
        show = true;
    } else {
        $('.main-list-little').removeClass("main-list-little-show");
        show = false;
    };
});
$('.btn-search').click(function () {
    if (show == true) {
        show = false;
        $('.main-list-little').removeClass("main-list-little-show");
    }
    if (showSearchBar == false) {
        $('.search-body').addClass("show-search-bar");
        showSearchBar = true;
    } else {
        $('.search-body').removeClass("show-search-bar");
        showSearchBar = false;
    };

});

$('.btn-list-little').click(function () {
    $('.list-little').slideToggle();
});

$(window).scroll(function (event) {
    var HeightScroll = $(window).scrollTop();
    $('#btn-top-page').click(function () {
        $(window).scrollTop('1');
    });
    if (HeightScroll > 100.8) {
        $('.row-animation-systems').addClass("row-animation-systems-on");
        $('.row-animation-systems').removeClass("row-animation-systems-off");
        $('.systems-title-underline').addClass("systems-title-underline-animations-on");
        console.log(HeightScroll)
    } else {
        $('.row-animation-systems').addClass("row-animation-systems-off");
        $('.row-animation-systems').removeClass("row-animation-systems-on");
        $('.systems-title-underline').removeClass("systems-title-underline-animations-on");
    };

    if (HeightScroll > 458) {
        $('.notifications-title-underline').addClass("notifications-title-underline-animation-on");
        $('.notifications-icon-title').addClass("notifications-icon-title-animation-on");
    } else {
        $('.notifications-title-underline').removeClass("notifications-title-underline-animation-on");
        $('.notifications-icon-title').removeClass("notifications-icon-title-animation-on");
    };

    if (HeightScroll > 508) {
        $('.notification-list').addClass("notification-list-animation-on");
    } else {
        $('.notification-list').removeClass("notification-list-animation-on");
    };

    if (HeightScroll > 700) {
        $('.newss-title-underline').addClass("newss-title-underline-animation-on");
    } else {
        $('.newss-title-underline').removeClass("newss-title-underline-animation-on");
    };

    if (HeightScroll > 772.80) {
        $('.news-list').addClass("news-list-animation-on");
        $('.newss-icon-title').addClass("newss-icon-title-animation-on");

    } else {
        $('.news-list').removeClass("news-list-animation-on");
        $('.newss-icon-title').removeClass("newss-icon-title-animation-on");
    };

    if (HeightScroll > 1300) {
        $('.events-icon-title').addClass("events-icon-title-animation-on");
        $('.events-title-underline').addClass("events-title-underline-animation-on");
    } else {
        $('.events-icon-title').removeClass("events-icon-title-animation-on");
        $('.events-title-underline').removeClass("events-title-underline-animation-on");
    }

    if (HeightScroll > 1317.5) {
        $('.events-list').addClass("events-list-animation-on");
    } else {
        $('.events-list').removeClass("events-list-animation-on");
    }

});
var SpanWidthRes = $('.event-body').width();
SetSpanWidthRes = SpanWidthRes - 90;
$('.event-title').css({ 'width': SetSpanWidthRes + 'px' });
console.log(SetSpanWidthRes);
window.addEventListener('resize', () => {
    var SpanWidthRes = $('.event-body').width();
    SetSpanWidthRes = SpanWidthRes - 90;
    $('.event-title').css({ 'width': SetSpanWidthRes + 'px' });
});





