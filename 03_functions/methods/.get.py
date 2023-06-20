# The get() method on dicts and default values

name_for_userid = {
    100: "John",
    102: "Bobby",
    103: "Susan"
}

def greeting(userid):
    return "Hi %s" % name_for_userid.get(userid, "there")

print(greeting(100))  # -> Hi John