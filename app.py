from flask import Flask,render_template,request
app=Flask(__name__)
@app.route("/")
def login():
    return render_template("login.html")
@app.route("/submit",methods=["POST"])
def submit():
    username = request.form.get("username")
    password = request.form.get("password")

        
    valid_users={
        'admin':'123', 
        'raj':'sss',
        'sujal':'sdf'
    }
    
    if username in valid_users and password == valid_users[username]:
        return render_template("welcome.html", name=username)    
        
    else:
        return "invalid credentials"
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
if __name__=="__main__":
    app.run(debug=True)