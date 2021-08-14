from flask import Flask, render_template

# from connection import add_songs
app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

# add_songs()
if __name__ == "__main__":
    app.run(debug=True, threaded=False)