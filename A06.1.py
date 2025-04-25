class PasswordManager:
    def __init__(self):
        self.old_passwords = []

    def get_password(self):
        """Returns the current password (last item in the list)."""
        return self.old_passwords[-1] if self.old_passwords else None

    def set_password(self, new_password):
        """Sets a new password only if it's not in old_passwords."""
        if new_password not in self.old_passwords:
            self.old_passwords.append(new_password)
            return True
        return False

    def is_correct(self, password):
        """Checks if the given password matches the current password."""
        return password == self.get_password()

pm = PasswordManager()
pm.set_password("password123")
pm.set_password("securePass")  
print(pm.get_password())    
print(pm.is_correct("securePass")) 
print(pm.is_correct("wrongPass"))  
pm.set_password("password123")
