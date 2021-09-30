"""
Monitoring service authentication
"""
def validate_password(username, potential_password):
    if potential_password.lower() == username.lower():
        return False
    elif len(potential_password) < 8:
        return False
    elif len(potential_password) > 256:
        return False
    elif potential_password.lower() in ("password", "12345678", "heimdall"):
        return False
    else:
        return True
