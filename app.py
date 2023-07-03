from flask import Flask, app
from flask import Response

app=Flask(__name__)

@app.route("/",methods=['GET','POST'])
def index():
    return "Starting top to bottom deployment"

if __name__ == "__main__":
    app.run(debug=True, port=9090)