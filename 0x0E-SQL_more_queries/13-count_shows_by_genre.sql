-- lists all genres from hbtn_0d_tvshows and displays
-- the number of shows linked to each.
SELECT TG.name AS genre,
    COUNT(*) AS number_of_shows
    FROM tv_genres AS TG
    INNER JOIN tv_show_genres AS TSG
    ON TG.id = TSG.genre_id;
    GROUP BY TSG.genre_id
    ORDER BY number_of_shows DESC
;
