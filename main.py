from flask import Flask
import os

app = Flask(__name__)

@app.route("/")
def index():
    return "✅ Бот запущен — всё работает!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.getenv("PORT", 8000)))

