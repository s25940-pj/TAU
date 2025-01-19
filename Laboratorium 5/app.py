from flask import Flask, jsonify, request, Response

app = Flask(__name__)


@app.route("/users", methods=["GET", "POST"])
def handle_users():
    users = [
        {"id": 1, "name": "Jan Kowalski", "email": "jan@kowalski.pl"},
        {"id": 2, "name": "Anna Nowak", "email": "anna@nowak.pl"},
    ]

    if request.method == "POST":
        data = request.get_json()
        if (
            data.get("id") != None
            and data.get("name") != None
            and data.get("email") != None
        ):
            user = {
                "id": int(data.get("id")),
                "name": data.get("name"),
                "email": data.get("email"),
            }

            users.append(user)

            return jsonify(user), 201
        else:
            return Response(status=500)

    return jsonify(users)


@app.route("/users/<int:id>", methods=["GET", "PUT", "DELETE"])
def handle_user_by_id(id):
    users = [
        {"id": 1, "name": "Jan Kowalski", "email": "jan@kowalski.pl"},
        {"id": 2, "name": "Anna Nowak", "email": "anna@nowak.pl"},
    ]

    if request.method == "GET":
        for user in users:
            if user.get("id") == id:
                return jsonify(user)

    if request.method == "PUT":
        data = request.get_json()
        for user in users:
            if user.get("id") == id:
                user["name"] = (
                    data.get("name") if data.get("name") is not None else user["name"]
                )
                user["email"] = (
                    data.get("email")
                    if data.get("email") is not None
                    else user["email"]
                )
                return jsonify(user)
        return Response(status=500)

    if request.method == "DELETE":
        for i, user in enumerate(users):
            if user.get("id") == id:
                del users[i]

                return Response(status=204)


if __name__ == "__main__":
    app.run()
