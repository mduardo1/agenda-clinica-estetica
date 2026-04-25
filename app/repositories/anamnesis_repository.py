from app.models.anamnesis import Anamnesis
from app.repositories.base_repository import BaseRepository


class AnamnesisRepository(BaseRepository):
    model = Anamnesis

    @classmethod
    def by_client(cls, client_id):
        return (
            cls.model.query.filter_by(client_id=client_id)
            .order_by(cls.model.created_at.desc())
            .all()
        )
