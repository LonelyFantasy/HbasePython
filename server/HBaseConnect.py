# -*- coding: utf-8 -*-
import happybase
import thrift


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


