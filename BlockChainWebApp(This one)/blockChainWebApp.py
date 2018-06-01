from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("home.html")

@app.route('/registration/')
def registration():
    return render_template("registration.html")

@app.route('/adminTransRequest/')
def adminTransRequest():
    return render_template("admin_transcript_request.html")

@app.route('/keyRequest/')
def keyRequest():
    return render_template("key_request.html")

@app.route('/blockRequest/')
def blockRequest():
    return render_template("blockchain_request.html")

@app.route('/networkRequest/')
def networkRequest():
    return render_template("network_transmission.html")
if __name__ == "__main__":
    app.run(debug=True)
