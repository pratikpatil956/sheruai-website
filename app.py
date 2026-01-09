from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/capabilities")
def capabilities():
    return render_template("capabilities.html")

@app.route("/agentic-ai")
def agentic():
    return render_template("agentic.html")

@app.route("/genai")
def genai():
    return render_template("genai.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

if __name__ == "__main__":
    import os
    # port = int(os.environ.get("PORT"))
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
