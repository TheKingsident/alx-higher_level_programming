$(document).ready(function () {
    $.get('https://swapi-api.alx-tools.com/api/films/?format=json', function(data) {
        data.results.forEach(function(films) {
            $('#list_movies').append(`<li>${films.title}</li>`);
        });
    });
});
