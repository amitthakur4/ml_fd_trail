from flask import Flask
# from crypt import methods

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    return "Starting top to bottom deployment"

if __name__ == "__main__":
    app.run(debug=True)