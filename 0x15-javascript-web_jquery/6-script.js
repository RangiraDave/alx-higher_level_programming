const $headerElement = $('header');
const $updateHeaderElement = $('div#update_header');

$updateHeaderElement.on('click', () => {
  $headerElement.text('New Header!!!');
});
