from glom import glom

data = {
    "user": {
        "profile": {
            "info": {
                "name": "Alice",
                "age": 20
            }
        },
        "id": 123
    }
}

spec = {
    "username": "user.profile.info.name",
    "user_age": "user.profile.info.age",
    "user_id": "user.id"
}

reslut1 = glom(data, spec)
# {'username': 'Alice', 'user_age': 20, 'user_id': 123}
username = reslut1["username"]
user_age = reslut1["user_age"]
print(username, user_age)