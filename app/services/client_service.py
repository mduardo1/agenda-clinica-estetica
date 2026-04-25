from datetime import datetime

from app.models.client import Client
from app.repositories.client_repository import ClientRepository


class ClientService:
    @staticmethod
    def list_all():
        return ClientRepository.ordered_by_name()

    @staticmethod
    def get(client_id):
        return ClientRepository.get(client_id)

    @staticmethod
    def create(data):
        birth_date = None
        if data.get("birth_date"):
            birth_date = datetime.strptime(data["birth_date"], "%Y-%m-%d").date()

        client = Client(
            full_name=data["full_name"].strip(),
            birth_date=birth_date,
            whatsapp=data["whatsapp"].strip(),
            anamnesis_notes=data.get("anamnesis_notes", "").strip(),
            restrictions=data.get("restrictions", "").strip(),
        )
        return ClientRepository.add(client)
