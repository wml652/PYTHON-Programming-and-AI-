from flask import Flask
app = Flask(__name__)

@app.route("/")
def home():
  return "Welcome to the Flask App!"

@app.route("/about")
def about():
   return "This is a simple route example to About page."

@app.route("/contact")
def contact():
  return "<h2>Contact Us</h2><p>Email: waqarmusaloan@gmail.com</p>"

if __name__ == "__main__":
    app.run(debug=True, use_reloader=False)
