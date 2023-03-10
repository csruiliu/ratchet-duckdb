import duckdb
import argparse

from queries import *

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-q", "--query", 
                        type=str, 
                        action="store", 
                        choices=['q1', 'q2', 'q3', 'q4', 'q5', 'q6', 'q7', 'q8', 'q9', 'q10', 'q11', 
                                 'q12', 'q13', 'q14', 'q15', 'q16', 'q17', 'q18', 'q19', 'q20', 'q21', 'q22'], 
                        help="indicate the query id")
    parser.add_argument("-sf", "--scale_factor", type=int, action="store", help="indicate scale factor of the dataset")

    args = parser.parse_args()
    
    qid = args.query
    sf = "SF" + str(args.scale_factor)
    data_path = "parquet/" + sf

    query = globals()[qid].query
    exec_query = query.replace("TPCH_DATAPATH", data_path)
    
    con = duckdb.connect(database=':memory:')

    query_len = len(exec_query)
    results = None
    if isinstance(exec_query, list):
        for idx, query in enumerate(exec_query):
            if idx == query_len - 1:
                results = con.execute(query).fetchdf()
            else:
                con.execute(query)
    else:
        results = con.execute(exec_query).fetchdf()

    print(results)


if __name__ == "__main__":
    main()
