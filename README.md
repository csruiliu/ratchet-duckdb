
## DuckDB
DuckDB is a high-performance analytical database system. It is designed to be fast, reliable and easy to use. DuckDB provides a rich SQL dialect, with support far beyond basic SQL. DuckDB supports arbitrary and nested correlated subqueries, window functions, collations, complex types (arrays, structs), and more. For more information on the goals of DuckDB, please refer to [the Why DuckDB page on our website](https://duckdb.org/why_duckdb).

## Installation
If you want to install and use DuckDB, please see [our website](https://www.duckdb.org) for installation and usage instructions.

## Data Import
For CSV files and Parquet files, data import is as simple as referencing the file in the FROM clause:

```sql
SELECT * FROM 'myfile.csv';
SELECT * FROM 'myfile.parquet';
```

Refer to our [Data Import](https://duckdb.org/docs/data/overview) section for more information.

## SQL Reference
The [website](https://duckdb.org/docs/sql/introduction) contains a reference of functions and SQL constructs available in DuckDB.

## Development 
For development, DuckDB requires [CMake](https://cmake.org), Python3 and a `C++11` compliant compiler. Run `make` in the root directory to compile the sources. For development, use `make debug` to build a non-optimized debug version. You should run `make unit` and `make allunit` to verify that your version works properly after making changes. To test performance, you can run `BUILD_BENCHMARK=1 BUILD_TPCH=1 make` and then perform several standard benchmarks from the root directory by executing `./build/release/benchmark/benchmark_runner`. The detail of benchmarks is in our [Benchmark Guide](benchmark/README.md).

Please also refer to our [Contribution Guide](CONTRIBUTING.md).
