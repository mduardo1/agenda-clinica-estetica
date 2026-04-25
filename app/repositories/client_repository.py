from app.models.client import Client
from app.repositories.base_repository import BaseRepository


class ClientRepository(BaseRepository):
    model = Client

    @classmethod
    def ordered_by_name(cls):
        return cls.model.query.order_by(cls.model.full_name.asc()).all()
