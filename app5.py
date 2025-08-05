from flask import Flask, request, render_template, redirect, url_for, flash 
from form import Registrationform
app=Flask(__name__)
app.secret_key = "my-secret-key"

@app.route("/", methods =["POST" ,"GET"])
def register():
   form = Registrationform()
   if form.validate_on_submit():
       name=form.name.data
       email=form.email.data
       flash(f"wellcome, {name}! YOU registered successfully","success")
       return redirect(url_for("success"))
   return render_template("register.html", form=form)
   
@app.route("/success")
def success():
    return render_template("success.html")
    




if __name__=="__main__":
    app.run(debug=True)