from app.models.procedure import Procedure
from app.repositories.base_repository import BaseRepository


class ProcedureRepository(BaseRepository):
    model = Procedure

    @classmethod
    def ordered_by_name(cls):
        return cls.model.query.order_by(cls.model.name.asc()).all()
