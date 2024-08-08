$(document).ready(function () {
  function translate() {
    $('DIV#hello').html('');
    const langCode = $('INPUT#language_code').val();
    $.ajax({
      method: 'GET',
      url: 'https://www.fourtonfish.com/hellosalut/hello/' + langCode,
      success: function (response) {
        $('DIV#hello').html(response.hello);
      }
    });
  }
  
  $('INPUT#btn_translate').on('click', function () {
    translate();
  });
  
  $('INPUT#language_code').on('keypress', function (event) {
    if (event.which === 13) {
      translate();
    }
  });
});
