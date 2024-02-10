$(function() {
    function fetchAndDisplayHello() {
        var languageCode = $('#language_code').val();
        var apiUrl = `https://hellosalut.stefanbohacek.dev/?lang=${languageCode}`;

        $.get(apiUrl, function(data) {
            $('#hello').text(data.hello);
        });
    }

    $('#btn_translate').click(function() {
        fetchAndDisplayHello();
    });

    $('#language_code').keypress(function(e) {
        if (e.which == 13) {
            fetchAndDisplayHello();
            e.preventDefault();
        }
    });
});
