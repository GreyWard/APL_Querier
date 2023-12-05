# database client for Google Big Query database
# Cara pakai:
# import .py ini ke program yang ingin menggunakannya
# inisiasi variabel baru dengan kelas databaseClient
# contoh: client = databaseClient('file credential')
from google.oauth2 import service_account
from google.cloud import bigquery
class databaseClient:
    # Initialize database connection through credential filename
    def __init__(self,credential):
        self.credentials = service_account.Credentials.from_service_account_file(credential)
        self.client = bigquery.Client(credentials=self.credentials)
    
    # fetch database metadata and convert it into string
    def fetch_metadata(self):
        query = """
        SELECT table_name, column_name, data_type
        FROM `querier-test-01.Test_01`.INFORMATION_SCHEMA.COLUMNS
        ORDER BY table_name, ordinal_position
        """
        query_job = client.query(query)
        # Convert to tables
        tables = {}
        for table_name, column_name, datatype in query_job:
            if table_name not in tables:
                tables[table_name] = []
            tables[table_name].append(f"{column_name} {datatype}")
        # Convert to sql_statements
        sql_statements = []
        for table_name, columns in tables.items():
            columns_str = ",\n".join(columns)
            sql_statement = f"CREATE TABLE {table_name} (\n{columns_str}\n);"
            sql_statements = append(sql_statement)
        return sql_statements
    
    # Send query and get the response
    def send_query(self,query):
        response = self.client.query(query).to_dataframe()
        return response
    