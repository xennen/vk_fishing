import clickhouse_connect
import vk


class ConnectionManager:
    @staticmethod
    def get_clickhouse_connect(host, username, password):
        client = clickhouse_connect.get_client(
            host=host, username=username, port=8123, password=password)
        return client
      
    @staticmethod
    def get_vk_connect(access_token):
        V = '5.199'
        api = vk.API(access_token=access_token, v=V)
        return api