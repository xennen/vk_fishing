import csv
from typing import List
from logging import Logger

class CsvToClickhouse:
    def __init__(self, connection, csv_path: str, log: Logger) -> None:
        self.conn = connection
        self.csv_path = csv_path
        self.log = log
        
    # Записываем 
    def insert_into_clickhouse(self, columns: List) -> None:
        with open(self.csv_path, encoding="utf8") as file_obj: 
            reader_obj = csv.reader(file_obj, delimiter='\t')
            next(reader_obj) # skip header
            reader_obj = list(reader_obj)
            self.conn.insert('stg.group_members', reader_obj, column_names=columns)
            self.log.info("Done inserting into clickhouse")
            
    def execute_query(self, name: str) -> None:
        with open(f"dags/scripts/sql/{name}") as sql_file:
            query = sql_file.read()
            self.log.info(f"Executing query: {query}")
            self.conn.command(query)
        

