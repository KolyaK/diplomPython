from flask import Flask, request, render_template
from сalculateIP import СalculateIp
app = Flask(__name__)


@app.route('/')
def my_form():
    return render_template('HomePage.html')


@app.route('/', methods=['GET', 'POST'])
def my_form_post():
    ip_address = request.form['text']
    mask = request.form['mask']
    ip = СalculateIp(ip_address)
    ip.set_mask(mask)
    ip.ip_to_bin()
    return render_template("result.html", ipAddress = ip_address,
                           binaryForm = ip.get_bin_ip(),
                           mask = mask,
                           binary_mask = ip.bin_mask(),
                           decimal_wildcard = ip.get_dec_wildcard(),
                           network = ip.get_network(),
                           hosts = ip.host(),
                           broadcast = ip.decimal_broadcast(),
                           classIP = ip.class_of_ip(mask),)


if __name__ == '__main__':
    app.run()
