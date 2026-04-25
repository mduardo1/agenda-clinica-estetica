from app.models.user import User
from app.repositories.base_repository import BaseRepository


class UserRepository(BaseRepository):
    model = User

    @classmethod
    def find_by_username(cls, username):
        return cls.model.query.filter_by(username=username).first()
