from app.models.user import User
from app.repositories.user_repository import UserRepository


class AuthService:
    @staticmethod
    def authenticate(username, password):
        user = UserRepository.find_by_username(username)
        if user and user.check_password(password):
            return user
        return None


def ensure_default_admin():
    if UserRepository.find_by_username("admin"):
        return

    user = User(username="admin")
    user.set_password("admin123")
    UserRepository.add(user)
