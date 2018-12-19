--
-- Name: slugdetails; Type: View; Schema: public; Owner: vagrant; Tablespace: 
--

CREATE VIEW slugdetails
AS SELECT title,
    '/article/' || slug as slug_path,
    name 
FROM articles,
    authors
WHERE articles.author = authors.id;