-- Script to display all shows.

SELECT tv_shows.title, tv_show_genres.genre_id, NULL IF NOT tv_show_genres.genre_id FROM tv_shows, tv_show_genres ORDER BY tv_shows.title, tv_show_genres.genre_id ASC;
