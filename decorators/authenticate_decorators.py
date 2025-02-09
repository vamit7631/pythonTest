def authenticate(user_role):
    def decorator(func):
        def wrapper(*args, **kwargs):
            if user_role != "admin":
                print("Access denied! Admins only.")
                return
            return func(*args, **kwargs)
        return wrapper
    return decorator

@authenticate(user_role="admin")
def delete_user(username):
    print(f"User {username} has been deleted.")

@authenticate(user_role="guest")
def modify_settings():
    print("Settings modified!")

delete_user("John")  # Allowed
modify_settings()  # Denied
