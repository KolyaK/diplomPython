from flask import Flask, request, render_template
from ipAddress import testIp
app = Flask(__name__)


@app.route('/')
def my_form():
    return render_template('my_form.html')


@app.route('/', methods=['GET', 'POST'])
def my_form_post():
    ip_address = request.form['text']
    mask = request.form['mask']
    ip = testIp(ip_address)
    ip.set_mask(mask)
    ip.ip_to_bin()
    return "Address: " + ip_address + "        binary form:         " + ip.get_bin_ip() + "<br>" + \
           "Mask: " + mask + "<br>"\
            "Binary mask: " + ip.bin_mask() + "<br>"\
            "Binary wildcard: " + ip.bin_wildcard() +" <br>" \
          #  "Network: " + ip.network() + "<br>"\
          #  "Broadcast: " + ip.broadcast() + "<br>"\
          #  "Hosts: " + ip.host()


if __name__ == '__main__':
    app.run()
