# Download Categories
https://dumps.wikimedia.org/enwiki/latest/enwiki-latest-categorylinks.sql.gz

# mysql
1. Start MySQL Workbench and connect to bdaf19-tbjauner.el.eee.intern
2. Change to bda database (use bda;)
3. Execute Wiki SQL Skript
4. Execute Filter SQL Query

# SQL Query to filter domain articles

SELECT 
	cl_from, 
    GROUP_CONCAT(CONVERT((cl_to) using utf8)) as cl_to
FROM categorylinks
GROUP BY cl_from
HAVING 
	(
		cl_to like 'digitale_medien'
		or cl_to like '%windows%'
		or cl_to like '%computer%'
		or cl_to like '%apple%'
		or cl_to like '%linux%'
        or cl_to like '%mac-os%'
    ) and not
    (
		cl_to like '%spiel%'
        or cl_to like '%mann%'
        or cl_to like '%frau%'
        or cl_to like '%person%'
		or cl_to like 'begriffserklärung'
	)
INTO OUTFILE '/var/lib/mysql-files/bda_id_whitelist.csv'


# copy the csv out of the docker container
docker cp <container id>:/var/lib/mysql-files/bda_id_whitelist.csv ./




# SPARQL
SELECT ?food, ?id
WHERE {
  ?food rdf:type dbo:Food .
  ?food dbo:wikiPageID ?id
}