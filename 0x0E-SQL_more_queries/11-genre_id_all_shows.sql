-- lists all shows contained in the database hbtn_0d_tvshows.
SELECT S.title, G.genre_id
    FROM tv_show_genres as G
    RIGHT JOIN tv_shows as S
    ON G.show_id = S.id
    ORDER BY S.title, G.genre_id
;
