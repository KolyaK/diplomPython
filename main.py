from flask import Flask, request, render_template
from ipAddress import testIp
app = Flask(__name__)


@app.route('/')
def my_form():
    return render_template('my_form.html')


@app.route('/', methods=['GET', 'POST'])
def my_form_post():
    text = request.form['text']
    ip = testIp(text)
    ip.ip_to_bin(ip.split_ip())
    return "Address: " + text + "        binary form:         " + ip.get_bin_ip()


if __name__ == '__main__':
    app.run()
