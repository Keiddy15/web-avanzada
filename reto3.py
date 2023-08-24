users_database = {
    "user": {"password": "userpass", "role": "user"},
    "admin": {"password": "adminpass", "role": "admin"},
    "superuser": {"password": "superpass", "role": "superuser"}
}

def authenticate(username, password):
    if username in users_database and users_database[username]["password"] == password:
        return users_database[username]["role"]
    return None

def user_auth_required(func):
    def wrapper(username, password, *args, **kwargs):
        role = authenticate(username, password)
        if role == "user":
            return func(username, password, *args, **kwargs)
        else:
            return "User authentication failed."
    return wrapper

def admin_auth_required(func):
    def wrapper(username, password, *args, **kwargs):
        role = authenticate(username, password)
        if role == "admin":
            return func(username, password, *args, **kwargs)
        else:
            return "Admin authentication failed."
    return wrapper

def superuser_auth_required(func):
    def wrapper(username, password, *args, **kwargs):
        role = authenticate(username, password)
        if role == "superuser":
            return func(username, password, *args, **kwargs)
        else:
            return "Superuser authentication failed."
    return wrapper

@user_auth_required
def user_function(username, password):
    return f"Hello, {username}! This is a user-level function."

@admin_auth_required
def admin_function(username, password):
    return f"Hello, {username}! This is an admin-level function."

@superuser_auth_required
def superuser_function(username, password):
    return f"Hello, {username}! This is a superuser-level function."

# Test the functions
print(user_function("user", "userpass"))
print(admin_function("admin", "adminpass"))
print(superuser_function("superuser", "superpass"))
