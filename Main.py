from flask import Flask, request, render_template
from ipAddress import test_ip
app = Flask(__name__)


@app.route('/')
def my_form():
    return render_template('my_form.html')


@app.route('/', methods=['GET', 'POST'])
def my_form_post():
    text = request.form['text']
    ip = test_ip(text)
    ip.ip_to_bin(ip.split_ip())
    return  str(ip.__str__())


if __name__ == '__main__':
    app.run()
