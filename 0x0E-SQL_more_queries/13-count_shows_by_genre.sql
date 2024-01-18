-- Script to count linked genres to shows.

SELECT tv_shows.title, count(tv_show_genres WHERE tv_shows.id = tv_show_genres.genre_id) AS number_of_shows FROM tv_shows, tv_show_genres ORDER BY number_of_shows DESC;
