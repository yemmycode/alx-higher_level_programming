$(document).ready(function () {
  $.ajax({
    method: 'GET',
    url: 'https://swapi-api.alx-tools.com/api/people/5/?format=json',
    success: function (response) {
      $('DIV#character').text(response.name);
    }
  });
});
