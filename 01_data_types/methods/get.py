# The get() method on dicts and default values

user_id_to_name = {
    100: "John",
    102: "Bobby",
    103: "Susan"
}

def greeting(user_id):
    return "Hi, %s!" % user_id_to_name.get(user_id, 'there')

print(greeting(100))