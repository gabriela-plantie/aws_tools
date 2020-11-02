```python
import awswrangler as wr
import pandas as pd
```


```python
bucket='bucket-data'
db='database'
athenaDb = AthenaDb(bucket, db)
```


```python
data = pd.DataFrame({ 'a': [1,2,3,4], 'b': [5,6,7,8] })
partition='b'
```


```python
athenaDb.createTableFromData('borrar', data, partition)
```


```python
athenaDb.readSql('select * from database.borrar')
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>a</th>
      <th>b</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>4</td>
      <td>8</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1</td>
      <td>5</td>
    </tr>
    <tr>
      <th>2</th>
      <td>3</td>
      <td>7</td>
    </tr>
    <tr>
      <th>3</th>
      <td>2</td>
      <td>6</td>
    </tr>
  </tbody>
</table>
</div>




```python
query='select * from database.borrar limit 10'
partition='b'
tableName='borrar2'
athenaDb.createTableFromQuery(tableName, query, partition)
```




    '08f50924-5ce6-48d6-bd01-41d3c96b9374'




```python
athenaDb.readSql('select * from database.borrar2')
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>a</th>
      <th>b</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>4</td>
      <td>8</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2</td>
      <td>6</td>
    </tr>
    <tr>
      <th>2</th>
      <td>3</td>
      <td>7</td>
    </tr>
    <tr>
      <th>3</th>
      <td>1</td>
      <td>5</td>
    </tr>
  </tbody>
</table>
</div>




```python
athenaDb.deleteTable('borrar2')
```


```python
try:
    athenaDb.readSql('select * from database.borrar2')
    print("It should never be printed!")
except Exception as error:
    print(error)
```

    SYNTAX_ERROR: line 8:3: Table awsdatacatalog.database.borrar2 does not exist. You may need to manually clean the data at location 's3://aws-athena-query-results-836263452508-us-east-1/tables/1f1278c5-fa5b-48c1-8eb4-22c954b99354' before retrying. Athena will not delete data in your account.

