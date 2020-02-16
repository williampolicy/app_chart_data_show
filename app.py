from flask import Flask
from flask import render_template
from flask import url_for
from flask import request   # for call send,ajax,onclick
from flask import jsonify
#url_for('static', filename='main.js')
#url_for('static', filename='data.tsv')

from flask import current_app # call current_app.send_static_file


app = Flask(__name__)


#--------------- 1.    set app.static_url_path        ------------
#---1.0 set app.static_url_path 
app.static_url_path='/static'
#---1.1 remove old static map
url_map = app.url_map
try:
	for rule in url_map.iter_rules('static'):
		url_map._rules.remove(rule)
except ValueError:
    # no static view was created yet
    pass
#---1.2  register new; the same view function is used
app.add_url_rule(
    app.static_url_path + '/<path:filename>',
    endpoint='static', view_func=app.send_static_file)


#--------------- 2.    Set route        ------------

#--- 2.1  route ('/') --
@app.route('/')
def index():
	print ('jump into index()')
	return render_template('index.html')


#--- 2.2  route ('/join') --

@app.route('/join', methods=['GET','POST'])
def my_form_post():
    text1 = request.form['text1']
    word =  request.args.get('text1')
    text2 = request.form['text2']
    #combine = do_something(text1,text2)
    combine = text1
    print('text1=',text1)
    print('word=',word)
    print('combine=',combine)    

    result = {
        "output": combine
    }

    result = {str(key): value for key, value in result.items()}
    print('result2 is',result)
    
    print('result.items() is',result.items())
    
    x = jsonify(result=result)
    print('jsonify(result=result) is : ',x)   

    return jsonify(result=result)


# http://127.0.0.1:5000/favicon.ico
@app.route('/favicon.ico')
def favicon():
    print('jump into favicon() to find favicon.ico')
    return current_app.send_static_file('favicon/favicon.ico')
                                        #static/favicon/favicon.ico , no need to say static again.

#--------------- 2.   define fuction        ------------
def do_something(text1,text2):
   text1 = text1.upper()
   text2 = text2.upper()
   combine = text1 + text2
   return combine




#--------------- 0. Main      ------------

if __name__ == '__main__':
    app.run(debug=True)


