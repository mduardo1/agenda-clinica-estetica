from decimal import Decimal

from app.models.procedure import Procedure
from app.repositories.procedure_repository import ProcedureRepository


class ProcedureService:
    @staticmethod
    def list_all():
        return ProcedureRepository.ordered_by_name()

    @staticmethod
    def get(procedure_id):
        return ProcedureRepository.get(procedure_id)

    @staticmethod
    def create(data):
        procedure = Procedure(
            name=data["name"].strip(),
            description=data.get("description", "").strip(),
            cost=Decimal(data.get("cost") or "0"),
            price=Decimal(data.get("price") or "0"),
        )
        return ProcedureRepository.add(procedure)
