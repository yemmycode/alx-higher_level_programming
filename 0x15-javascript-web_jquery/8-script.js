$(document).ready(function () {
  $.ajax({
    method: 'GET',
    url: 'https://swapi-api.alx-tools.com/api/films/?format=json',
    success: function (response) {
      $.each(response.results, function (index, film) {
        $('UL#list_movies').append($('<li>').text(film.title));
      });
    }
  });
});

