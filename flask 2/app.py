
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/skills")
def skills():
    return render_template("skills.html")

@app.route("/projects")
def projects():
    return render_template("projects.html")

@app.route("/certifications")
def certifications():
    return render_template("certifications.html")

@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        name = request.form.get("name")
        email = request.form.get("email")
        message = request.form.get("message")

        # 👉 Here you can save to database or send an email
        print(f"New Contact: {name}, {email}, {message}")

        return f"<p>Thank you, {name}! Your message has been received.</p>"

    return render_template("contact.html")


if __name__ == "__main__":
    app.run(debug=True)

