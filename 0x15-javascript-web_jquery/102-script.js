$(document).ready(function () {
  $('INPUT#btn_translate').on('click', function () {
    $('DIV#hello').html(''); 
    const langCode = $('INPUT#language_code').val();
    $.ajax({
      method: 'GET',
      url: 'https://fourtonfish.com/hellosalut/?lang=' + langCode,  
      success: function (response) {
        $('DIV#hello').html(response.hello);  
      }
    });
  });
});

