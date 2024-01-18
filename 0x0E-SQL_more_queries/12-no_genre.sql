-- Script to display shows without a genre.

SELECT tv_shows.title, tv_show_genres.genre_id FROM tv_shows JOIN tv_show_genres WHERE tv_shows.id NOT IN tv_show_genres.genre_id;
