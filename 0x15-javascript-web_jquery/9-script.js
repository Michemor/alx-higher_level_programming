$(document).ready(() => {
  const url = 'https://hellosalut.stefanbohacek.dev/?lang=fr';
  $.get(url, (data) => {
    $('div#hello').append(data.hello);
  });
});
