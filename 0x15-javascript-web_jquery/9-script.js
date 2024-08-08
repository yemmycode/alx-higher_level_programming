$(document).ready(function () {
  $.ajax({
    method: 'GET',
    url: 'https://hellosalut.stefanbohacek.dev/?lang=fr',
    success: function (response) {
      $('DIV#hello').html(response.hello);
    }
  });
});

