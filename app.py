from flask import Flask
app = Flask(__name__)

@app.route('/')
@app.route('/present')
def present():
	return 'present' 

@app.route('/past')
def past():
	return 'past'

@app.route('/future')
def future():
	return 'future'

if __name__ == '__main__':
	app.run()