import boto3
import clickhouse_connect


class ConnectionManager:
    @staticmethod
    def get_s3_client(self):
        s3 = boto3.client('s3',
                          endpoint_url='http://172.17.0.1:9000',
                          aws_access_key_id='minio_admin',
                          aws_secret_access_key='minio_admin')
        return s3
    
    @staticmethod
    def get_clickhouse_conn(self):
        client = clickhouse_connect.get_client(
            host='172.17.0.1', username='clickhouse_admin', port=8123, password='clickhouse_admin')
        return client