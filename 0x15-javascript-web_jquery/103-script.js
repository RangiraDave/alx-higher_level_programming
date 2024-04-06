$('document').ready(function () {
  $('INPUT#btn_translate').click(translator);
  $('INPUT#language_code').focus(function () {
    $(this).keydown(function (enter) {
      if (enter.keycode === 13) {
        translator();
      }
    });
  });
});

function translator () {
  const url = 'https://www.fourtonfish.com/hellosalut/?';
  $.get(url + $.param({ lang: $('INPUT#language_code').val() }), function (data) {
    $('DIV#hello').html(data.hello);
  });
}
