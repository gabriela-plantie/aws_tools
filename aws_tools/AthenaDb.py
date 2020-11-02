import awswrangler as wr

class AthenaDb:
    
    def __init__(self, bucket, db):
        self.bucket = bucket
        self.db = db
        

    def createTableFromQuery(self, tableName, query, partition, asyncCall=False):
        self.deleteTable(tableName)
        
        if type(partition) == str:
            partition = [partition]
        
        partitions = 'ARRAY[' + (','.join(map(lambda x: '\''+x+'\'', partition))) + ']'
            
        query=f'''CREATE TABLE  {self.db}.{tableName}
        with (format = 'parquet',
              parquet_compression = 'SNAPPY',
              external_location = 's3://{self.bucket}/{self.db}/{tableName}',
              partitioned_by = {partitions} )
        AS {query}'''
        
        query_exec_id = wr.athena.start_query_execution(sql=query, database=self.db)
        if not asyncCall:
            wr.athena.wait_query(query_execution_id=query_exec_id)

        return query_exec_id
    
    
    def createTableFromData(self, tableName, data, partition):
        self.deleteTable(tableName)
        self.appendData(tableName, data, partition)
        
    
    def appendData(self, tableName, data, partition):
        if type(partition) == str:
            partition = [partition]
        
        wr.s3.to_parquet(
            data,
            path=f"""s3://{self.bucket}/{self.db}/{tableName}/""",
            database=self.db,
            dataset=True,
            table=tableName,
            partition_cols=partition,
            mode='append',
            compression='snappy'
        )
        
    
    def readSql(self, query):
        return wr.athena.read_sql_query(sql=query, database=self.db)
    
    
    def deleteTable(self, tableName):
        wr.catalog.delete_table_if_exists(database=self.db, table=tableName)
        wr.s3.delete_objects(f"s3://{self.bucket}/{self.db}/{tableName}/")
