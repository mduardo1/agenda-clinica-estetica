from app.routes.anamnesis_routes import anamnesis_bp
from app.routes.appointment_routes import appointments_bp
from app.routes.auth_routes import auth_bp
from app.routes.client_routes import clients_bp
from app.routes.main_routes import main_bp
from app.routes.procedure_routes import procedures_bp


def register_routes(app):
    app.register_blueprint(auth_bp)
    app.register_blueprint(main_bp)
    app.register_blueprint(clients_bp)
    app.register_blueprint(procedures_bp)
    app.register_blueprint(appointments_bp)
    app.register_blueprint(anamnesis_bp)
