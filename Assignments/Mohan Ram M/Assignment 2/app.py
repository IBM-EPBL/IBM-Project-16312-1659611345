from flask import Flask, render_template, request, redirect
import sqlite3 as sql
import database as dbHandler

app = Flask(__name__)
app.secret_key = '101010'

@app.route('/')
def home():
   returnrender_template('home.html')

@app.route('/adduser')
defnew_user():
   returnrender_template('add_user.html')

@app.route('/addrec',methods = ['POST', 'GET'])
defaddrec():
   ifrequest.method == 'POST':
      try:
         email = request.form['email']
         un = request.form['username']
         rn = request.form['rollnumber']
         pin = request.form['pin']
         
         withsql.connect("User_database.db") as con:
            cur = con.cursor()
            cur.execute("INSERT INTO users (email,username,rollnumber,pin) VALUES (?,?,?,?)",(email,un,rn,pin) )
            con.commit()
            msg = "Record successfully added!"
      except:
         con.rollback()
         msg = "error in insert operation"
     
      finally:
         returnrender_template("list.html",msg = msg)
         con.close()

@app.route('/list')
def list():
   con = sql.connect("User_database.db")
   con.row_factory = sql.Row
   
   cur = con.cursor()
   cur.execute("select * from users")
   
   users = cur.fetchall()
   returnrender_template("list.html", users = users)

if __name__ == '__main__':
   app.run(debug = True)

@app.route("/delete")  
def delete():  
    returnrender_template("delete.html")

@app.route('/deleterecord',methods = ["POST"])  
defdeleterecord():  
    un = request.form['username']
    withsql.connect("User_database.db") as con:
        try:  
            cur = con.cursor()  
            cur.execute("DELETE FROM users WHERE username = ?",[un])
            con.commit()
            msg = "Record successfully deleted"
        except:
            msg = "can't be deleted"  
        finally:  
            returnrender_template("home1.html",msg = msg)

if __name__ == '__main__':
   app.run(debug = True)

@app.route('/deldb', methods = ["POST"])
defdeldb():
   con = sql.connect('User_database.db')
   cur = con.cursor()
   cur.execute('DELETE FROM users;')
   con.commit()
   con.close()
   msg = 'All the data has been deleted'
   returnrender_template("home1.html",msg = msg)

@app.route("/log")  
def log():  
    returnrender_template("login.html")

@app.route('/login', methods =['GET', 'POST'])
def login():
   un = request.form['username']
   ifrequest.method=='POST':
         users = dbHandler.retrieveUsers()
         msg = 'Logged in successfully!'
         returnrender_template('welcome.html', users=un, msg=msg)
   else:
         msg = 'Not registered please register'
         returnrender_template('home1.html', msg=msg)

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0')
