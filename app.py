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


EMAIL_MESSAGE = "<b>Name:</b> {0}<br>\
<b>Email Address:</b> {1}<br>\
<b>Subject:</b> {2}<br>\
<b>Message:</b> {3}"

ME = 'mmeier@eng.ucsd.edu'
SONEZ = 'iamsonez.com'

@app.route('/email', methods=['POST'])
def send_email():
	msg = EMAIL_MESSAGE.format(request.form.get("name"), 
							   request.form.get("email"),
							   request.form.get("subject"), 
							   request.form.get("message"))

	msg = MIMEText(msg, 'html')
	msg['Subject'] = 'Sonez Inquiry - {0}'.format(request.form.get("subject"))
	msg['To'] = ME
	msg['From'] = SONEZ

	s = smtplib.SMTP_SSL('smtpout.secureserver.net', '465')
	s.sendmail(SONEZ, ME, msg.as_string())
	s.quit()

if __name__ == '__main__':
	app.run()