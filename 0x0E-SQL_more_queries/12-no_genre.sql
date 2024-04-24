--  lists all shows contained in hbtn_0d_tvshows without a genre linked
SELECT S.title, G.genre_id
    FROM tv_shows AS S
    FULL JOIN tv_show_genres AS G
    ON S.id = G.show_id
    WHERE S.id IS NULL
    OR G.show_id IS NULL
    ORDER BY S.title, G.genre_id
;
