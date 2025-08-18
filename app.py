from flask import Flask
import os

app = Flask(__name__)

@app.get("/")
def hello():
    return "Hola Mundo desde Flask + Docker + GitHub Actions + Render!"

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))
    app.run(host="0.0.0.0", port=port)
