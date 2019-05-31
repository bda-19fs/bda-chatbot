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