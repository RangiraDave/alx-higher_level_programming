-- Script to display genres for Dexter show.

SELECT tv_genres.name FROM tv_genres JOIN tv_shows ON tv_shows.id = tv_genres.genre_id AND tv_shows.name = 'Dexter' ORDER BY tv_genres.name ASC;
