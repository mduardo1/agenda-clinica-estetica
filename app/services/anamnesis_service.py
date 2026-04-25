from app.models.anamnesis import Anamnesis
from app.repositories.anamnesis_repository import AnamnesisRepository


class AnamnesisService:
    @staticmethod
    def list_by_client(client_id):
        return AnamnesisRepository.by_client(client_id)

    @staticmethod
    def create(data):
        record = Anamnesis(
            client_id=int(data["client_id"]),
            notes=data.get("notes", "").strip(),
            restrictions=data.get("restrictions", "").strip(),
            care_instructions=data.get("care_instructions", "").strip(),
        )
        return AnamnesisRepository.add(record)
