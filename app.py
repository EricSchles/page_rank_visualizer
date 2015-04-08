from flask import Flask, request, render_template, redirect, url_for
app = Flask(__name__)

@app.route("/",methods=["GET","POST"])
def index():
	# form - request.form
	if request.method == "POST":
		website1 = request.form.get("website1")
		website2 = request.form.get("website2")
		return redirect("https://www.google.com")		
	return render_template("index.html")

@app.route("/thing",methods=["GET","POST"])
def thing():
	# form - request.form
	return "please"


if __name__ == "__main__":
    app.run(debug=True)