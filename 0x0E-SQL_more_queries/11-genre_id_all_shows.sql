-- lists all shows contained in the database hbtn_0d_tvshows.
SELECT S.title,
    CASE WHEN  G.genre_id <> NULL THEN G.genre_id ELSE NULL
    FROM tv_shows as S
    LEFT JOIN tv_show_genres as G
    ON S.id = G.show_id
    ORDER BY S.title, G.genre_id;

