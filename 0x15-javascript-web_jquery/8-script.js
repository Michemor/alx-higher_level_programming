$(document).ready(() => {
  const url = 'https://swapi-api.alx-tools.com/api/films/?format=json';
  $.get(url, (data) => {
    const titles = data.results.map(movie => {
      return movie.title;
    });
    titles.forEach((t) => {
      $('ul#list_movies').append('<li>' + t + '</li>');
    });
  });
});
