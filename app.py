from flask import Flask
from flask import render_template
from flask import url_for

#url_for('static', filename='main.js')
#url_for('static', filename='data.tsv')

app = Flask(__name__)
app.static_url_path='/static'

#--------------- set app.static_url_path ------------
# remove old static map
url_map = app.url_map
try:
	for rule in url_map.iter_rules('static'):
		url_map._rules.remove(rule)
except ValueError:
    # no static view was created yet
    pass
# register new; the same view function is used
app.add_url_rule(
    app.static_url_path + '/<path:filename>',
    endpoint='static', view_func=app.send_static_file)


@app.route('/')
def index():
	print ('jump into index()')
	return render_template('index.html')

#https://stackoverflow.com/questions/48047533/d3-does-not-load-tsv-data-in-python-flask-script
# Make sure you configured your static file path somewhere in you app code
# 1. app = Flask(name)
# 2. app.static_url_path='/static'
# Put you data.tsv file in the static file directory
# In your index.html template, modify the path to the TSV file in the javascript part accordingly to the path of your TSV file:



# How to set app.static_url_path
#https://stackoverflow.com/questions/26722279/how-to-set-static-url-path-in-flask-application
# 1. Flask creates the URL route when you create the Flask() object. You'll need to re-add that route:
# 2. It'll be easier just to configure your Flask() object with the correct static URL path.


