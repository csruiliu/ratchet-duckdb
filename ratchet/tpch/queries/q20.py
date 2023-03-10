query = """
SELECT	S_NAME,
		S_ADDRESS
FROM	'TPCH_DATAPATH/supplier.parquet',
		'TPCH_DATAPATH/nation.parquet'
WHERE	S_SUPPKEY IN (
		SELECT	PS_SUPPKEY
		FROM	'TPCH_DATAPATH/partsupp.parquet'
		WHERE	PS_PARTKEY IN (
			SELECT	P_PARTKEY
			FROM	'TPCH_DATAPATH/part.parquet'
			WHERE	P_NAME LIKE 'forest%'
		)
		AND PS_AVAILQTY > (
			SELECT	0.5 * SUM(L_QUANTITY)
			FROM	'TPCH_DATAPATH/lineitem.parquet'
			WHERE	L_PARTKEY = PS_PARTKEY
					AND L_SUPPKEY = PS_SUPPKEY
					AND L_SHIPDATE >= '1994-01-01'
					AND L_SHIPDATE < '1995-01-01'
			)
		)
		AND S_NATIONKEY = N_NATIONKEY
		AND N_NAME = 'CANADA'
ORDER BY	S_NAME;
"""
