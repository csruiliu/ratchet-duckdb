query = ["""
CREATE TEMP VIEW REVENUE (SUPPLIER_NO, TOTAL_REVENUE) AS
	SELECT	L_SUPPKEY,
			sum(L_EXTENDEDPRICE * (1 - L_DISCOUNT))
    FROM	'parquet/lineitem.parquet'
    WHERE	L_SHIPDATE >= '1996-01-01'
			AND L_SHIPDATE < '1996-04-01'
    GROUP BY	L_SUPPKEY
""", """
SELECT	S_SUPPKEY,
		S_NAME,
		S_ADDRESS,
		S_PHONE,
		TOTAL_REVENUE
FROM	'parquet/supplier.parquet',
		REVENUE
WHERE	S_SUPPKEY = SUPPLIER_NO
		AND TOTAL_REVENUE = (
			SELECT	MAX(TOTAL_REVENUE)
			FROM	REVENUE
		)
ORDER BY	S_SUPPKEY
""", """
DROP VIEW REVENUE
"""]