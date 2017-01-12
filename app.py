import os
import sys
sys.path.insert(0, '/home/iamsonez/public_html/sonez/sonez/lib/python2.7/site-packages')

from flask import Flask, render_template, request
import smtplib
from email.mime.text import MIMEText

app = Flask(__name__, static_url_path='')

@app.route('/')
@app.route('/present')
def present():
	return render_template('present.html')

@app.route('/past')
def past():
	return render_template('past.html')

@app.route('/future')
def future():
	return render_template('future.html')


EMAIL_MESSAGE = "Message from iamsonez.com\n \
				 name: {0}\n \
				 email: {1}\n \
				 message: {2}"

ME = 'mmeier@eng.ucsd.edu'
SONEZ = 'iamsonez.com'

@app.route('/email', methods=['POST'])
def send_email():
	msg = EMAIL_MESSAGE.format(request.form.get("name"), 
							   request.form.get("email"), 
							   request.form.get("message"))

	msg = MIMEText(msg)
	msg['Subject'] = 'New Inquiry From {0}'.format(request.form.get("name"))
	msg['To'] = ME
	msg['From'] = SONEZ

	s = smtplib.SMTP('smtpout.secureserver.net')
	s.sendmail(SONEZ, ME, msg.as_string())
	s.quit()
