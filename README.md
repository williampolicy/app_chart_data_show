# chart-example
# 关于黑屏问题。 需要更换端口号。 
- Front:
python -m SimpleHTTPServer 8000
http://localhost:8000/
8080
8088 等等
使用Chome 黑屏。 ,使用MAC自己的浏览器。 没有问题。  
https://williampolicy.github.io/chart-example/

- Start app

export FLASK_APP=app.py
flask run




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


It can WORK !  Let GO! 
2020.2.14 : git commit -m "set app.static_url_path='/static', It work from Flask to call js ,and data." 

Add chart and text input. It work! well done. 
2020.2.24: git commit -m "Add chart and text input. It work! well done. " 