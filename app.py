from flask import Flask

app = Flask(__name__)
@app.route("/")
def index():
    return "浪晋的测试小讲堂"

if __name__ == "__main__":
    app.run()


