$(function() {
    $('#btn_translate').click(function() {
        var languageCode = $('#language_code').val();
        var apiUrl = `https://hellosalut.stefanbohacek.dev/?lang=${languageCode}`;

        $.get(apiUrl, function(data) {
            $('#hello').text(data.hello);
        });
    });
});
