-- lists all shows contained in the database hbtn_0d_tvshows.
SELECT S.title, G.genre_id
FROM tv_shows as S
LEFT JOIN tv_show_genres as G
ON S.id = G.show_id
ORDER BY S.title, G.genre_id;

