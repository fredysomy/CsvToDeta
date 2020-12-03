
![data](https://raw.githubusercontent.com/fredysomy/CsvToDeta/main/images/20201203_215247_0000~2.png)






## A Lightweight tool to upload CSV files data into Deta Base.
 
 [![PyPI version](https://badge.fury.io/py/csvtodeta.svg)](https://badge/pysondb)
 [![PyPI download day](https://img.shields.io/pypi/dm/csvtodeta.svg)](https://pypi.python.org/pypi/csvtodeta)

 ## CLI operations

 * Needed
   * Secret Id of Deta Base
   * Path to the csv file
   * Database name in Deta


* Data of csv file (sample) :

``` 
name,age
fredy,34
god,34345345
mannu,34
```

***
#### Use
```python
$ csvtodeta --id ID_OF_BASE --path path/to/csv.csv --db DETABASE_NAME
Reading data from DETABASE_NAME
Uploaded ..
Uploaded ..
Uploaded ..
..
..
succesfully uploaded n data to DETABASE_NAME Base
```   



#### Example
```python
$ csvtodeta --id 45345dhsgh3rjdf2ur34hhwf --path path/to/csv.csv --db detabasename
Reading data from src/deta.csv
Uploaded {'name': 'fredy', 'age': '34'}
Uploaded {'name': 'god', 'age': '34345345'}
Uploaded {'name': 'maanu', 'age': '34'}
succesfully uploaded 3 data to detabasename Base
```   


