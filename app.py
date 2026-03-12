from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello! My Flask API is running."

@app.route("/api")
def api():
    return {"message": "Welcome to my API"}

if __name__ == "__main__":
    app.run()
