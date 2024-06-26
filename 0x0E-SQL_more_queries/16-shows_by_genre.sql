--- This syntax lists all genres the show dexter is listed under
SELECT tv_shows.title, tv_genres.name 
FROM tv_shows
LEFT JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
LEFT JOIN tv_genres ON tv_show_genres.genre_id = tv_genres.id
WHERE tv_shows.title = 'Dexter'
ORDER BY tv_shows.title, tv_genres.name;
