-- Display best records with this format (score name) in descendent order
SELECT score, name
  FROM second_table
  WHERE score >= 10
  ORDER BY score DESC;
