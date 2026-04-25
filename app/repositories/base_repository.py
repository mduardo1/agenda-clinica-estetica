from app.database.db import db


class BaseRepository:
    model = None

    @classmethod
    def all(cls):
        return cls.model.query.all()

    @classmethod
    def get(cls, item_id):
        return db.session.get(cls.model, item_id)

    @classmethod
    def add(cls, entity):
        db.session.add(entity)
        db.session.commit()
        return entity

    @classmethod
    def delete(cls, entity):
        db.session.delete(entity)
        db.session.commit()
