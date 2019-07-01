$(function () {
    $('td').on('click', function () {
        $(this).css('background-color', 'orange');
        var day = $(this).text();
        location.href=url

    });
})