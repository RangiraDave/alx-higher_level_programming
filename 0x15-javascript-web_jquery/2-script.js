const $headerElement = $('header');
const $divRedHeader = $('div#red_header');

$divRedHeader.on('click', function () {
  $headerElement.css('color', '#FF0000');
});
