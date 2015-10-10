from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def index_page():
    """Show an index page."""
    return render_template("index.html")

@app.route("/application-form")
def application():
    
    return render_template("application-form.html")

@app.route("/application", methods=["POST"])
def application_response():
    user_name = request.form.get("name")
    print user_name
    user_lastname = request.form.get("lastname")
    user_job = request.form.get("job")
    return render_template("application-response.html",name=user_name,lastname=user_lastname,job=user_job)
    
if __name__ == "__main__":
    app.run(debug=True)
