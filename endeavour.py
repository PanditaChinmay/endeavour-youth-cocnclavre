pip install Flask 
from flask import Flask, render_template

app = Flask(_name_)

@app.route('/')
def home():
return render_template('index.html')

if _name_ == '_main_':
app.run(debug=True)

!DOCTYPE html>
<html>
<head>
<title>ENDEAVOR YOUTH CONCLAVE</title>
<style>
body {
background-color: white;
color: red;
}
</style>
</head>
<body>
<h1>Welcome to ENDEAVOR YOUTH CONCLAVE</h1>
<p>This is your editable MUN website.</p>
</body>
</html>
from flask import Flask, render_template

app = Flask(__name)

@app.route('/')
def home():
return render_template('index.html')

@app.route('/secretariat')
def secretariat():
return render_template('secretariat.html')

@app.route('/committees')
def committees():
return render_template('committees.html')

@app.route('/what-is-mun')
def what_is_mun():
return render_template('what_is_mun.html')

if _name_ == '_main_':
app.run(debug=True)
from flask import Flask, render_template
app = Flask(__name)
@app.route('/')
def home():
return render_template('index.html')
@app.route('/secretariat')
def secretariat():
return render_template('secretariat.html')
if _name_ == '_main_':
app.run(debug=True)
from flask import Flask, render_template

app = Flask(__name)

@app.route('/')
def home():
return render_template('index.html')

@app.route('/secretariat')
def secretariat():
return render_template('secretariat.html')

@app.route('/committees')
def committees():
return render_template('committees.html')

if _name_ == '_main_':
app.run(debug=True)