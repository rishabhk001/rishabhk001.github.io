
from flask_mysqldb import MySQL
from flask import Flask,render_template,url_for,request,flash
import smtplib
import random
from smtp import *
app=Flask(__name__)
app.config['MYSQL_USER']="root"
app.config['MYSQL_PASSWORD']=""
app.config['MYSQL_HOST']="127.0.0.1"
app.config['MYSQL_DB']="project"
app.secret_key="Some secret"
mysql=MySQL(app)

@app.route('/', methods=['GET','POST'])
def index():
    if request.method=="POST":
        details = request.form
        email = details['email']
        password = details['pass']
        cur = mysql.connection.cursor()
        check=cur.execute("select * from teacher where email=%s and password=%s",(email,password))
        if check==0:
            flash("Email or password is incorrect")
        else:
            return render_template('dashboard.html')
        mysql.connection.commit()
        cur.close()

    return render_template('index.html')
@app.route('/forgot',methods=['GET','POST'])
def main():
    return render_template("main.html")
@app.route('/check',methods=['GET','POST'])
def check():
    if request.method=="POST":
        check.mail=request.form['register']
        cur = mysql.connection.cursor()
        email_check=cur.execute("select * from teacher where email='%s'"%(check.mail))
        if email_check==0:
            flash("Wrong email address")
            return render_template("main.html")
        else:
            check.otp_check=int(sm(check.mail))
            flash("OTP Sent")
            return render_template("otp.html")
    return render_template("main.html")
@app.route('/check_otp',methods=['GET','POST'])
def check_otp():
    if request.method=="POST":
        otp_check=check.otp_check
        get_otp=int(request.form['otp'])
        if get_otp==otp_check:
            cur = mysql.connection.cursor()
            cur.execute("select password from teacher where email='%s'"%(check.mail))
            get_pass=cur.fetchone()
            flash("Your password is : "+str(get_pass[0]))
            mysql.connection.commit()
            cur.close()
        else:
            flash("Incorrect OTP")
    return render_template("otp.html")
if __name__=="__main__":
    app.run(debug=True)