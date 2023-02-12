
# Ratchet-DuckDB

Ratchet-DuckDB is a fine-grained suspend/resume prototype system modified from DuckDB 0.6.1.

## Prerequisite

Install pybind11 using `pip3 install pybind11` (system-wide or virtual environment)

`pip3 show pybind11` will tell you where is the pybind11

If you are using CLion IDE for development, and make sure CLion can link all the source code, you may need to add `-DBUILD_PYTHON_PKG=TRUE -DCMAKE_PREFIX_PATH=/path/to/pybind11` in `Settings | Build, Execution, Deployment | CMake | CMake Options`. This will tell Clion where to find pybind11. 

When you want to add a new Python API for DuckDB, we usually need to modify the source code in `tools/pythonpkg/src`. Also, to make sure the newly added Python API can be detected by IDEs, we need to run `scripts/regenerate_python_stubs.sh` to regenerate the corresponding `__ini__.pyi` file, which may also need `mypy` python library. 

## Python Client

Ratchet-DuckDB can be used and tested by a python client. It is recommended to install the python client in a python virtual environment

```bash
source <path/to/python-virtual-environment/bin/activate>
cd <Ratchet-DuckDB>/tools/pythonpkg 
python setup.py install
```

## TPC-H Evaluation

First, you need to generate the original tables using TPC-H tools and then move them to `tpch/tbl` folder. Simply running `tpch_data.py` can convert the table files to `parquet` format, you can move the parquet files to `tpch/parquet` folder.

`tpch_perf` will trigger the original TPC-H queries from q1 to q22.

