from flask import Flask, render_template

app = Flask( __name__)

@app.route("/")
def home():
   return render_template("home.html", name="Waqar")


# we make the temolated of html and then we can use them in place of _____.html portion and can easily acess our we
# website from there 

if __name__ = "__Home__": 
   app.run(debug=True)
