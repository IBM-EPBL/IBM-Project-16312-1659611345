from flask import Flask,render_template,request
import requests 
import ibm_db
app = Flask(__name__)

# dsn_hostname = "55fbc997-9266-4331-afd3-888b05e734c0.bs2io90l08kqb1od8lcg.databases.appdomain.cloud" 
# dsn_uid= "ntj24419"
# dsn_pwd= "fTbavf47TXpOwDUw" 
# dsn_driver = "{IBM DB2 ODBC DRIVER}"
# dsn_database = "BLUDB"
# dsn_port = "31929"
# dsn_protocol = "TCPIP"
# dsn_security="SSL"


# dsn = (
# "DRIVER={0};"
# "DATABASE ={1};"
# "HOSTNAME={2};"
# "PORT={3};"
# "PROTOCOL ={4};"
# "UID={5};"
# "PWD={6}:").format(dsn_driver, dsn_database, dsn_hostname, dsn_port, dsn_protocol, dsn_uid, dsn_pwd)
# print(dsn)


# try:
#      conn= ibm_db.connect(dsn,"ntj24419","fTbavf47TXpOwDUw") 
#      print("Connected to database: ", dsn_database, "as user: ", dsn_uid, "on host: ", dsn_hostname)

# except: 
#     print ("Unable to connect: ", ibm_db.conn_errormsg())



# server = ibm_db.server_info(conn)
# print ("DBMS_NAME: ", server. DBMS_NAME)
# print ("DBMS_VER: ", server.DBMS_VER)
# print ("DB_NAME: ", server.DB_NAME)



@app.route('/')
def index():
    title = "News App"
    return render_template('index.html',title=title)


@app.route('/register')
def register():
    title = "News App Register"
    return render_template('register_page.html',title=title)


@app.route('/login')
def login():
    title = "News App Login"
    return render_template('login.html',title = title)


@app.route('/',methods=["POST"])
def form():
    title = "Home"
    name = request.form.get("name")
    email = request.form.get("email")
    password = request.form.get("password")
    username = request.form.get("uname")
    
    if not name or not email or not password:
        error_statement = "Please fill the details!!!"
        return render_template('home.html',title = title, name= name,email=email,password=password)
   
    else:
         url ="https://newsapi.org/v2/top-headlines?country=in&apiKey=7e535c4ed1044f4ab17b70d0efd2a84b"
         r = requests.get(url).json()
         case = {
             'articles': r['articles']
         }
         return render_template('home.html',title=title,name= name,email=email,password=password,cases = case)

if __name__ == '__main__':
    app.run(debug = True)

    #GET https://newsapi.org/v2/top-headlines?country=in&apiKey=7e535c4ed1044f4ab17b70d0efd2a84b


