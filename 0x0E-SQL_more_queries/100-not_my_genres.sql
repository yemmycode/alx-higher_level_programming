--- This syntax lists all genres the show dexter is listed under
CREATE TABLE IF NOT EXISTS dexter_genres AS (
  SELECT tv_genres.id, tv_genres.name
  FROM tv_genres
  INNER JOIN tv_show_genres ON tv_genres.id = tv_show_genres.genre_id
  INNER JOIN tv_shows ON tv_shows.id = tv_show_genres.show_id
  WHERE tv_shows.title = 'Dexter'
);

SELECT tv_genres.name
FROM tv_genres
WHERE tv_genres.id NOT IN (
  SELECT id FROM dexter_genres
)
ORDER BY tv_genres.name;
