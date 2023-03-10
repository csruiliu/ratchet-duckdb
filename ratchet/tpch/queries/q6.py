query = """
SELECT	sum(L_EXTENDEDPRICE * L_DISCOUNT) AS REVENUE
FROM	'TPCH_DATAPATH/lineitem.parquet'
WHERE	CAST(L_SHIPDATE AS DATE) >= '1994-01-01'
        AND CAST(L_SHIPDATE AS DATE) < '1995-01-01'
        AND L_DISCOUNT BETWEEN 0.05 AND 0.06
        AND L_QUANTITY < 24
"""
