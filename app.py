# credit: code taken from
# https://github.com/Code-Institute-Solutions/TaskManagerAuth/tree/main/08-SearchingWithinTheDatabase/01-text_index_searching
# and edited to fit project needs

import os
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for, jsonify)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
if os.path.exists("env.py"):
    import env

app = Flask(__name__)


app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)


@app.route("/get_clientInfo")
def get_clientInfo():
    clientInfo = list(mongo.db.clientInfo.find().sort("client_organization",
                      1))
    return render_template("clientInfo.html", clientInfo=clientInfo)


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        # check if username already exists in db
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            flash("Username already exists")
            return redirect(url_for("register"))

        register = {
            "username": request.form.get("username").lower(),
            "password": generate_password_hash(request.form.get("password"))
        }
        mongo.db.users.insert_one(register)

        # put the new user into 'session' cookie
        session["user"] = request.form.get("username").lower()
        flash("Registration Successful!")
    return render_template("register.html")


@app.route("/")
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        # check if username exists in db
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            # ensure hashed password matches user input
            if check_password_hash(
                    existing_user["password"], request.form.get("password")):
                session["user"] = request.form.get("username").lower()
                return redirect(url_for(
                                        "profile", username=session["user"]))
            else:
                # invalid password match
                flash("Incorrect Username and/or Password")
                return redirect(url_for("login"))

        else:
            # username doesn't exist
            flash("Incorrect Username and/or Password")
            return redirect(url_for("login"))

    return render_template("login.html")


@app.route("/profile/<username>", methods=["GET", "POST"])
def profile(username):
    # grab the session user's username from db
    username = mongo.db.users.find_one(
        {"username": session["user"]})["username"]
    return render_template("profile.html", username=username)


@app.route("/logout")
def logout():
    # remove user from session cookie
    flash("You have been logged out")
    session.clear()
    return redirect(url_for("login"))


@app.route("/add_client", methods=["GET", "POST"])
def add_client():
    if request.method == "POST":
        mongo.db.clientInfo.insert_one(request.form.to_dict())
        flash("Client Successfully Added")
        return redirect(url_for("get_clientInfo"))

    categories = mongo.db.categories.find().sort("category_name", 1)
    return render_template("addClient.html", categories=categories)


@app.route("/edit_clientInfo/<clientInfo_id>", methods=["GET", "POST"])
def edit_clientInfo(clientInfo_id):
    if request.method == "POST":
        submit = {
            "client_organization": request.form.get("client_organization"),
            "client_name": request.form.get("client_name"),
            "client_position": request.form.get("client_position"),
            "client_email": request.form.get("client_email"),
            "category_name": request.form.get("category_name")
        }
        mongo.db.clientInfo.update({"_id": ObjectId(clientInfo_id)}, submit)
        flash("Client Successfully Updated")
        return redirect(url_for("get_clientInfo"))

    clientInfo = mongo.db.clientInfo.find_one({"_id": ObjectId(clientInfo_id)})
    categories = mongo.db.categories.find().sort("category_name", 1)
    return render_template("editClient.html", clientInfo=clientInfo,
                           categories=categories)


@app.route("/delete_clientInfo/<clientInfo_id>")
def delete_clientInfo(clientInfo_id):
    mongo.db.clientInfo.remove({"_id": ObjectId(clientInfo_id)})
    flash("Client Information Successfully Deleted")
    return redirect(url_for("get_clientInfo"))


@app.route("/invoice", methods=["GET", "POST"])
def invoice():
    if request.method == "GET":
        clientInfos = mongo.db.clientInfo.find().sort("client_organization", 1)
        rateTypes = list(mongo.db.rateType.find().sort("rate_type", 1))
        interpretingAmounts = list(mongo.db.interpretingAmount.find().sort(
            "interpreting_amount", 1))
        consultings = mongo.db.consulting.find().sort("consulting", 1)
        consultingAmounts = mongo.db.consultingAmount.find().sort(
            "consulting_amount", 1)
        return render_template("invoice.html", clientInfos=clientInfos,
                               rateTypes=rateTypes,
                               interpretingAmounts=interpretingAmounts,
                               consultings=consultings,
                               consultingAmounts=consultingAmounts)


# credit: thank you to Joshua Ugba for guiding me in understanding how to
# access exactly the information I needed to access.
@app.route("/api/invoice", methods=["GET", "POST"])
def invoice_api():
    if request.method == "GET":
        clientInfos = list(mongo.db.clientInfo.find().sort(
            "client_organization", 1))
        for clientInfo in clientInfos:
            clientInfo['_id'] = str(clientInfo['_id'])
        print(clientInfos)
        return jsonify(clientInfos)


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=False)