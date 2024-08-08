$(document).ready(function () {
  $("DIV#add_item").on('click', function () {
    $('<li>').text('Item').appendTo('ul.my_list');
  });
});
