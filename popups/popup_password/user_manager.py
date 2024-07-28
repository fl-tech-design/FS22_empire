# user_manager.py
import bcrypt
from constants import PATH_DIR_U_DAT


class PwManager:
    def __init__(self, app, **kwargs) -> None:
        """
        Initializes the password manager with the given application context.

        Args:
            app: The application context that contains user data.
            **kwargs: Additional arguments for future extensions.
        """
        self.app = app

    def hash_password(self, password: str) -> str:
        """
        Hashes a password using bcrypt.

        Args:
            password (str): The password to hash.

        Returns:
            str: The hashed password.
        """
        return bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt()).decode("utf-8")

    def check_password(self, stored_password: str, provided_password: str) -> bool:
        """
        Checks if a provided password matches the stored hashed password.

        Args:
            stored_password (str): The stored hashed password.
            provided_password (str): The password provided for verification.

        Returns:
            bool: True if the provided password matches the stored password, False otherwise.
        """
        return bcrypt.checkpw(
            provided_password.encode("utf-8"), stored_password.encode("utf-8")
        )

    def validate_user_pw(self, curr_uname: str, password: str) -> bool:
        """
        Validates a user's password against the stored password.

        Args:
            curr_uname (str): The current username.
            password (str): The password to validate.

        Returns:
            bool: True if the username exists and the password is correct, False otherwise.
        """
        if curr_uname in self.app.user_data["uname"] and self.check_password(
            self.app.user_data["password"], password
        ):
            return True
        return False
