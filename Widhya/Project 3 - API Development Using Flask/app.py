#Imports
from flask import Flask, request, jsonify, abort, make_response
from flask_httpauth import HTTPBasicAuth

app = Flask(__name__) #App Instance
auth = HTTPBasicAuth()#Authentication Instance

#(dummy data)
Data =  [{"username": "Alexander", "secret": "f201alex"},
         {"username": "marina891", "secret": "blushy235"}
         ]

@auth.verify_password
def verify_password(username, password):
    for data in Data:
        if data["username"] == username and data["secret"] == password:
            return username
            
@auth.error_handler
def unauthorized():
    return make_response(jsonify({'error': 'Unauthorized access'}), 401)

@app.errorhandler(404)
def not_found(error):
    """To Handle 404 error pages"""
    return make_response(jsonify({"error":"Not Found!"}), 404)

#curl -i -v -u marina891:blushy235 http://localhost:5000/list
@app.route("/list", methods=["GET"])
@auth.login_required
def get_users():
    """List all Users"""
    return jsonify(Data)

#curl -i -v -u marina891:blushy235 http://localhost:5000/fetch/Alexander
@app.route("/fetch/<user>", methods=["GET"])
@auth.login_required
def fetch_user(user):
    """Fetch a User based on his username (case sensitive)"""
    for data in Data:
        if user == data["username"]:
            return jsonify(data)

    return abort(404)

#Use this curl form for windows cmd
#curl -i -v -u marina891:blushy235 -H "Content-Type: application/json" -X POST -d "{ \"username\" : \"test\", \"secret\" : \"test\" }" http://localhost:5000/add
@app.route("/add", methods=["POST"])
@auth.login_required
def add_users():
    """Add Users"""
    if not request.json or not "username" in request.json or not "secret" in request.json:
        abort(400)

    data = {"username": request.json["username"],
            "secret": request.json["secret"]
            }

    Data.append(data)

    return jsonify({"User": data}), 201

#Use this curl form for windows cmd
#curl -i -v -u marina891:blushy235 -H "Content-Type: application/json" -X PUT -d "{ \"username\" : \"test\", \"secret\" : \"test\" }" http://localhost:5000/edit/Alexander
@app.route("/edit/<user>", methods=["PUT"])
@auth.login_required
def edit_users(user):
    """Edit the info of an existing user"""
    if not request.json or not "username" in request.json or not "secret" in request.json:
        abort(404)

    check=0
    for i in range(len(Data)):
        if Data[i]["username"] == user:
            check=1
            Data[i]["username"] = request.json["username"]
            Data[i]["secret"] = request.json["secret"]
            break

    if check == 0:
        abort(404)

    return jsonify({"edit on user": user, "new data": request.json, "success":"201"})

#curl -i -v -u marina891:blushy235 -X DELETE http://localhost:5000/delete/Alexander
@app.route("/delete/<user>", methods=["Delete"])
@auth.login_required
def delete_users(user):
    """Delete a user entry"""
    to_rmv = [data for data in Data if data["username"] == user]

    if not to_rmv:
        abort(404)

    Data.remove(to_rmv[0])
    return jsonify({"Date Removed": to_rmv[0], "success":"201"})

#Start Checkpoint
if __name__ == "__main__":
    app.debug = True
    app.run(host="0.0.0.0", port=5000)
