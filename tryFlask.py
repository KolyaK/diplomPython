from flask import Flask

app = Flask(__name__)


@ app.route("/")
def hello():
    return "hello word"


@ app.route("/hi")
def hi():
    user = {'nickname': 'Kolya'}  # пользователь
    return '''
    <html>
      <head>
        <title>Home Page</title>
      </head>
      <body>
        <h1>Hello, ''' + user['nickname'] + '''</h1>
      </body>
    </html>
    '''


@ app.route("/user/<name>")  # прием параметра через  url 
def user(name):
    return "<h1> Hello, {} </h1>".format(name)


# if __name__ == '__main__':
app.run()
