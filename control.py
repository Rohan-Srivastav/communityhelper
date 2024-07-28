from flask import *
from flask_sqlalchemy import *
from datetime import timedelta
global us,pas,Email,em,listery
listery=[]
'''def encrypt(x):
    p="abcdefghijklmnopqrstuvwxyz"
    ni="0123456789"
    x=list(x) 
    p=list(p)
    ni=list(ni)
    for i in x:
        if i in p:
            x.index(i)=x[x.index(i)+2]'''
app = Flask(__name__) 
app.secret_key="danke Toni8"
app.permanent_session_lifetime=timedelta(minutes=10)
app.config["SQLALCHEMY_DATABASE_URI"]='sqlite:///users.sqlite3'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"]=False
db=SQLAlchemy(app)
class users(db.Model):
    num=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(500))
    Email=db.Column(db.String(900))
    passw=db.Column(db.String(400))
    def __init__(self,name,Email,passw):
        self.name=name
        self.Email=Email
        self.passw=passw
class volunteer(db.Model):
    k=db.Column(db.Integer,primary_key=True)
    h=db.Column(db.String(2000))
    def __init__(self,h):
        self.h=h
        
@app.route('/loginpage/',methods=["POST","GET"])
def login():
    if request.method=="POST":
        session.permanent=True
        us=request.form["username"]
        em=request.form["Email"]
        pas=request.form["password"]
        a=users.query.filter_by(name=us).first()
        b=users.query.filter_by(Email=em).first()
        c=users.query.filter_by(passw=pas).first()
        if a and b and c:
            session["us"]=us
            session["em"]=em
            session["pas"]=pas
            listery.append(us)
            listery.append(em)
            listery.append(pas)
            return redirect(url_for("work"))
        else:
            f=users(us,em,pas)
            db.session.add(f)
            db.session.commit()
            return render_template("loginpage.html")
        
    return render_template("loginpage.html")
@app.route('/')
def seefirst():
    return render_template("homepage.html")
@app.route('/worker/')
def worka():       
    if ("us"in session ):
        session["us"]=listery[0]
        session["em"]=listery[1]
        session["pas"]=listery[2]
        return '''<!DOCTYPE html>
<html lang="en">

<head>
    <style>
      body {
    font-family: 'Montserrat', sans-serif;
    margin: 0;
    padding: 0;
    background-color: #f4f4f9;
    display: flex;
}

.header {
    background-color: #ff0202;
    color: black;
    padding: 10px;
    text-align: center;
    display: flex;
    align-items: center;
    justify-content: center;
    width: 100%;
    position: fixed;
    top: 0;
    left: 0;
    z-index: 1000;
    border-bottom: 2px solid black;
}

.header .logo {
    height: 50px;
    margin-right: 20px;
}

@keyframes nn{
25%{
    background-color: rgb(255, 4, 4);
}
50%{
    background-color: rgb(0, 179, 255);
}
75%{
    background-color: beige;
}
100%{
    background-color: orangered;
}
}
.sidebar {
    width: 250px;
    position: fixed;
    top: 0;
    left: 0;
    background-color: rgb(255, 4, 4);
    padding-top: 100px;
    height: 100%;
    color: white;
    overflow-y: auto;
    border-right: 3px solid black;
    animation: nn 3s ease-in-out 0.1s infinite alternate-reverse;
    height: 100%;
}

.sidebar a {
    padding: 15px 20px;
    text-decoration: none;
    color: white;
    display: block;
    font-size: 16px;
    border-bottom: 1px solid black;
}

.sidebar a:hover {
    background-color: rgb(255, 0, 225);
}

.sidebar a i {
    margin-right: 10px;
}

.main-content {
    margin-left: 260px;
    padding: 20px;
    padding-top: 120px;
    width: calc(100% - 260px);
}

.profile-card {
    display: flex;
    background-color: white;
    padding: 20px;
    border-radius: 8px;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
    margin-bottom: 20px;
    align-items: center;
    border: 2px solid black;
}

.profile-photo {
    border-radius: 50%;
    width: 150px;
    height: 150px;
    margin-right: 20px;
    border: 2px solid black;
}

.profile-info {
    flex: 1;
}

.profile-info h2 {
    margin-top: 0;
    color: #3b5998;
}

.profile-info p {
    margin: 5px 0;
    color: #555;
}


.edit-btn:hover {
    background-color: #2c3e50;
}

.section {
    background-color: white;
    padding: 20px;
    border-radius: 8px;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
    margin-bottom: 20px;
    border: 2px solid black;
}

.section h2 {
    margin-top: 0;
    color: #000000;
}
#l{
    font-family: cursive;
    margin-right: 20px;
}
#btttn{
    display: inline-block;
}
@keyframes mmm{
    from{
        width: calc(100% - 260px);
    }
    to{
        width: calc(100% - 800px);
    }
}
/* .mnm{ */
    /* animation: mmm 2s ease-in-out 0.1s infinite alternate-reverse; */
/* } */6  
</style>    <title>Community Oraganisation</title>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.3/dist/css/bootstrap.min.css" rel="stylesheet"
        integrity="sha384-rbsA2VBKQhggwzxH7pPCaAqO46MgnOM80zW1RWuH61DGLwZJEdK2Kadq2F9CUG65" crossorigin="anonymous">
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.2.3/dist/js/bootstrap.bundle.min.js"
        integrity="sha384-kenU1KFdBIe4zVF0s0G1M5b4hcpxyD9F7jL+jjXkk+Q2h455rYXK/7HAuoJl+0I4"
        crossorigin="anonymous"></script>
        <link rel="stylesheet" href="k.css">
        <link rel="shortcut icon" href="favicon.jpeg" type="image/x-icon">

</head>
<body>

    <div class="header bg-dark">
        <img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRatOyMT_2GFQJ2zEA53RId1H-bke4LeACt3g&s" alt="School Logo" class="logo">
        <h1><font color="white" id="l">Community Service</font></h1>
        <a  href="/logout"><button class="btn btn-danger" id="btttn"> Logout </button></a>
    </div>
    <div class="sidebar">
        <a href="/workez/"><i class="fas fa-home"></i><b style="color: black">Home</b></a>
       <a href="/workez/a"><i class="fas fa-home"></i><b style="color: black">create form</b></a>
    </div>
    <div class="main-content mnm">
        <div class="profile-card">
            <img src="https://upload.wikimedia.org/wikipedia/commons/6/68/Taj_Mahal%2C_Agra%2C_India.jpg" alt="Student Photo" class="profile-photo">
            <div class="profile-info">
                <h2>Demo Account</h2>
                <p><strong>Name:</strong>MYNAME</p>
                <p><strong>Email</strong>example@gmail.com</p>
                <p><strong>Volunteered for</strong> Event</p>
            </div>
        </div>
    </div>
    <br>
    <a href="/workers/"><button> volunteer options</button></a>
</body>
</html>
'''
@app.route("/workers/")
def ghjy():
    return '''cleanliness drive'''
@app.route('/workez/')
def work():       
    if ("us"in session ):
        session["us"]=listery[0]
        session["em"]=listery[1]
        session["pas"]=listery[2]
        return '''<!DOCTYPE html>
<html lang="en">

<head>
    <style>
      body {
    font-family: 'Montserrat', sans-serif;
    margin: 0;
    padding: 0;
    background-color: #f4f4f9;
    display: flex;
}

.header {
    background-color: #ff0202;
    color: black;
    padding: 10px;
    text-align: center;
    display: flex;
    align-items: center;
    justify-content: center;
    width: 100%;
    position: fixed;
    top: 0;
    left: 0;
    z-index: 1000;
    border-bottom: 2px solid black;
}

.header .logo {
    height: 50px;
    margin-right: 20px;
}

@keyframes nn{
25%{
    background-color: rgb(255, 4, 4);
}
50%{
    background-color: rgb(0, 179, 255);
}
75%{
    background-color: beige;
}
100%{
    background-color: orangered;
}
}
.sidebar {
    width: 250px;
    position: fixed;
    top: 0;
    left: 0;
    background-color: rgb(255, 4, 4);
    padding-top: 100px;
    height: 100%;
    color: white;
    overflow-y: auto;
    border-right: 3px solid black;
    animation: nn 3s ease-in-out 0.1s infinite alternate-reverse;
    height: 100%;
}

.sidebar a {
    padding: 15px 20px;
    text-decoration: none;
    color: white;
    display: block;
    font-size: 16px;
    border-bottom: 1px solid black;
}

.sidebar a:hover {
    background-color: rgb(255, 0, 225);
}

.sidebar a i {
    margin-right: 10px;
}

.main-content {
    margin-left: 260px;
    padding: 20px;
    padding-top: 120px;
    width: calc(100% - 260px);
}

.profile-card {
    display: flex;
    background-color: white;
    padding: 20px;
    border-radius: 8px;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
    margin-bottom: 20px;
    align-items: center;
    border: 2px solid black;
}

.profile-photo {
    border-radius: 50%;
    width: 150px;
    height: 150px;
    margin-right: 20px;
    border: 2px solid black;
}

.profile-info {
    flex: 1;
}

.profile-info h2 {
    margin-top: 0;
    color: #3b5998;
}

.profile-info p {
    margin: 5px 0;
    color: #555;
}


.edit-btn:hover {
    background-color: #2c3e50;
}

.section {
    background-color: white;
    padding: 20px;
    border-radius: 8px;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
    margin-bottom: 20px;
    border: 2px solid black;
}

.section h2 {
    margin-top: 0;
    color: #000000;
}
#l{
    font-family: cursive;
    margin-right: 20px;
}
#btttn{
    display: inline-block;
}
@keyframes mmm{
    from{
        width: calc(100% - 260px);
    }
    to{
        width: calc(100% - 800px);
    }
}
/* .mnm{ */
    /* animation: mmm 2s ease-in-out 0.1s infinite alternate-reverse; */
/* } */6  
</style>    <title>Community Oraganisation</title>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.3/dist/css/bootstrap.min.css" rel="stylesheet"
        integrity="sha384-rbsA2VBKQhggwzxH7pPCaAqO46MgnOM80zW1RWuH61DGLwZJEdK2Kadq2F9CUG65" crossorigin="anonymous">
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.2.3/dist/js/bootstrap.bundle.min.js"
        integrity="sha384-kenU1KFdBIe4zVF0s0G1M5b4hcpxyD9F7jL+jjXkk+Q2h455rYXK/7HAuoJl+0I4"
        crossorigin="anonymous"></script>
        <link rel="stylesheet" href="k.css">
        <link rel="shortcut icon" href="favicon.jpeg" type="image/x-icon">

</head>
<body>

    <div class="header bg-dark">
        <img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRatOyMT_2GFQJ2zEA53RId1H-bke4LeACt3g&s" alt="School Logo" class="logo">
        <h1><font color="white" id="l">Community Service</font></h1>
        <a  href="/logout"><button class="btn btn-danger" id="btttn"> Logout </button></a>
    </div>
    <div class="sidebar">
        <a href="/workez/"><i class="fas fa-home"></i><b style="color: black">Home</b></a>
       <a href="/workez/a"><i class="fas fa-home"></i><b style="color: black">create form</b></a>
    </div>
    <div class="main-content mnm">
        <div class="profile-card">
            <img src="https://upload.wikimedia.org/wikipedia/commons/6/68/Taj_Mahal%2C_Agra%2C_India.jpg" alt="Student Photo" class="profile-photo">
            <div class="profile-info">
                <h2>Demo Account</h2>
                <p><strong>Name:</strong>'''+listery[0]+'''</p>
                <p><strong>Email</strong>'''+listery[1]+'''</p>
            </div>
        </div>
    </div>
</body>
</html>'''
    else:
        return redirect(url_for("login"))
@app.route("/logout")
def logout():
    session.pop("us",None)
    session.pop("em", None)
    session.pop("pasw",None)
    for i in listery:
        del(i)
    return redirect(url_for("login"))
@app.route("/workez/a",methods=["POST","GET"])
def fgh():
    if request.method=="POST":
        d=request.form["workname"]
        do=volunteer(d)
        db.session.add(do)
        db.session.commit()
    return '''<center><form method="POST"><input type="text" name="workname" placeholder="name"></form><center>'''
if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)