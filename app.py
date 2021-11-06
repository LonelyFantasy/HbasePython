from flask import Flask

import server.HBaseConnect

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    connection = server.HBaseConnect.HBaseConnect()
    data = connection.get_table("student")
    print(data)
    return 'Hello World!'


if __name__ == '__main__':
    app.run()