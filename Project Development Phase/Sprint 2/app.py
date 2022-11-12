from flask import Flask,render_template,request
app = Flask(__name__)


@app.route('/')
def index():
    title = "News App"
    return render_template('index.html',title=title)


@app.route('/register')
def register():
    title1 = "News App Register"
    return render_template('register_page.html',title=title1)


@app.route('/login')
def login():
    title2 = "News App Login"
    return render_template('login.html',title = title2)


@app.route('/',methods=["POST"])
def form():
    title = "Home"
    name = request.form.get("name")
    email = request.form.get("email")
    password = request.form.get("password")
    
    if not name or not email or not password:
        error_statement = "Please fill the details!!!"
        return render_template('home.html',title = title, name= name,email=email,password=password)

