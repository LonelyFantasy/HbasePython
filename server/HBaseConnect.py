# -*- coding: utf-8 -*-
import happybase
import model.ReturnValue as Value

# Operate State
SUCCESS = Value.SUCCESS
FAILURE = Value.FAILURE


class HBaseConnect:
    def __init__(self):
        """
        建立与thrift server端的连接
        """
        # self.connection = happybase.Connection(host="net.orekimai.icu", port=6051, timeout=None, autoconnect=True,
        #                                        table_prefix=None, table_prefix_separator=b'_', compat='0.98',
        #                                        transport='buffered', protocol='binary')
        self.connection = happybase.Connection(host="192.168.150.130", port=9090, timeout=None, autoconnect=True,
                                               table_prefix=None, table_prefix_separator=b'_', compat='0.98',
                                               transport='buffered', protocol='binary')

    def get_table(self, table_name: str):    # Return Happybase Table
        return self.connection.table(table_name)

    def start(self):    # Start To Connect
        self.connection.open()

    def stop(self):    # Stop To Connect
        self.connection.close()

    def delete_table_row(self, table_name: str, row_id: str):
        self.connection.open()
        try:
            table = self.get_table(table_name)
            table.delete(row_id)
            self.connection.close()
            return SUCCESS
        except Exception as e:
            print(e)
            return FAILURE

    def get_double_table_dict(self, table_name: str):
        first_list = {}
        second_list = {}
        self.connection.open()
        try:
            table = self.get_table(table_name)
            for key, value in table.scan():
                for key1 in value:
                    #     print(str(key1, encoding='utf-8'))
                    #     print(str(value[key1], encoding='utf-8'))
                    second_list[str(key1, encoding='utf-8')] = str(value[key1], encoding='utf-8')
                first_list[str(key, encoding='utf-8')] = second_list
                print(first_list)
            return first_list
        except Exception as e:
            print(e)
            return FAILURE


