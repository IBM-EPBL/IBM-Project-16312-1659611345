from flask import Flask, render_template,request,session,redirect
import requests
import ibm_db
import ibm_db_dbi
import re
from flask_db2 import DB2


app = Flask(__name__)
app.secret_key = 'secret123'

app.config['database'] = 'bludb'
app.config['hostname'] = '55fbc997-9266-4331-afd3-888b05e734c0.bs2io90l08kqb1od8lcg.databases.appdomain.cloud'
app.config['port'] = '31929'
app.config['protocol'] = 'tcpip'
app.config['uid'] = 'ntj24419'
app.config['pwd'] = 'fTbavf47TXpOwDUw'
app.config['security'] = 'SSL'
try:
    mysql = DB2(app)

    conn_str='database=bludb;hostname=55fbc997-9266-4331-afd3-888b05e734c0.bs2io90l08kqb1od8lcg.databases.appdomain.cloud;port=31929;protocol=tcpip;uid=ntj24419;pwd=fTbavf47TXpOwDUw;security=SSL'
    ibm_db_conn = ibm_db.connect(conn_str,'','')
        
    print("Database connected without any error !!")
except:
    print("IBM DB Connection error   :     " + ibm_db.conn_errormsg())


@app.route('/')
def home():
    #url = "https://newsapi.org/v2/top-headlines?country=in&category=general&apiKey=7e1737d3191d4fe894fc579df01b7bde"
    #r= requests.get(url).json()
    #case = {
    #    'articles': r['articles']
    #}
    return render_template('login.html')#cases = case)

@app.route('/index')
def index():
    url = "https://newsapi.org/v2/top-headlines?country=in&category=general&apiKey=7e1737d3191d4fe894fc579df01b7bde"
    r= requests.get(url).json()
    case = {
        'articles': r['articles']
    }
    return render_template('index.html',cases=case)

@app.route('/sports')
def sports():
    url = "https://newsapi.org/v2/top-headlines?country=in&category=sports&apiKey=7e1737d3191d4fe894fc579df01b7bde"
    r= requests.get(url).json()
    case = {
        'articles': r['articles']
    }
    return render_template('sports.html',cases = case)

@app.route('/business')
def business():
    url = "https://newsapi.org/v2/top-headlines?country=in&category=business&apiKey=7e1737d3191d4fe894fc579df01b7bde"
    r= requests.get(url).json()
    case = {
        'articles': r['articles']
    }
    return render_template('business.html',cases = case)

@app.route('/technology')
def technology():
    url = "https://newsapi.org/v2/top-headlines?country=in&category=technology&apiKey=7e1737d3191d4fe894fc579df01b7bde"
    r= requests.get(url).json()
    case = {
        'articles': r['articles']
    }
    return render_template('tech.html',cases = case)

@app.route('/science')
def science():
    url = "https://newsapi.org/v2/top-headlines?country=in&category=science&apiKey=7e1737d3191d4fe894fc579df01b7bde"
    r= requests.get(url).json()
    case = {
        'articles': r['articles']
    }
    return render_template('science.html',cases = case)

@app.route('/health')
def health():
    url = "https://newsapi.org/v2/top-headlines?country=in&category=health&apiKey=7e1737d3191d4fe894fc579df01b7bde"
    r= requests.get(url).json()
    case = {
        'articles': r['articles']
    }
    return render_template('health.html',cases = case)

@app.route('/reg')
def reg():
    return render_template('register.html')

@app.route('/register',methods=["GET","POST"])
def register():
    username = request.form.get("name")
    email = request.form.get("email")
    password = request.form.get("password")

    try:
        connectionID = ibm_db_dbi.connect(conn_str, '', '')
        cursor = connectionID.cursor()
    except:
        print("No connection Established")

    sql = "SELECT * FROM register WHERE username = ?"
    stmt = ibm_db.prepare(ibm_db_conn, sql)
    ibm_db.bind_param(stmt, 1, username)
    ibm_db.execute(stmt)
    result = ibm_db.execute(stmt)
    print(result)
    account = ibm_db.fetch_row(stmt)
    print(account)

    param = "SELECT * FROM register WHERE username = " + "\'" + username + "\'"
    res = ibm_db.exec_immediate(ibm_db_conn, param)
    print("---- ")
    dictionary = ibm_db.fetch_assoc(res)
    while dictionary != False:
        print("The ID is : ", dictionary["USERNAME"])
        dictionary = ibm_db.fetch_assoc(res)
  
    if account:
        msg = 'Username already exists !'
    elif not re.match(r'[^@]+@[^@]+\.[^@]+', email):
        msg = 'Invalid email address !'
    elif not re.match(r'[A-Za-z0-9]+', username):
        msg = 'name must contain only characters and numbers !'
    else:
        sql2 = "INSERT INTO register (username, email,password) VALUES (?, ?, ?)"
        stmt2 = ibm_db.prepare(ibm_db_conn, sql2)
        ibm_db.bind_param(stmt2, 1, username)
        ibm_db.bind_param(stmt2, 2, email)
        ibm_db.bind_param(stmt2, 3, password)
        ibm_db.execute(stmt2)
        msg = 'You have successfully registered !'
        print(msg)

    return render_template('login.html')


@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/loginn',methods =['GET', 'POST'])
def loginn():
    title = "Home"
    if request.method == 'POST' :
        username = request.form['uname']
        password = request.form['password']
        
        sql = "SELECT * FROM register WHERE username = ? and password = ?"
        stmt = ibm_db.prepare(ibm_db_conn, sql)
        ibm_db.bind_param(stmt, 1, username)
        ibm_db.bind_param(stmt, 2, password)
        result = ibm_db.execute(stmt)
        print(result)
        account = ibm_db.fetch_row(stmt)
        print(account)
        
        param = "SELECT * FROM register WHERE username = " + "\'" + username + "\'" + " and password = " + "\'" + password + "\'"
        res = ibm_db.exec_immediate(ibm_db_conn, param)
        dictionary = ibm_db.fetch_assoc(res)

        if account:
            session['loggedin'] = True
            session['username'] = dictionary["USERNAME"]
            session['email'] = dictionary["EMAIL"]

            #return render_template('base.html')
            return redirect('/index')
        else:
            return render_template('login.html')

    return render_template('login.html')


if __name__ == '__main__':
    app.run(debug=True)