# routes/__init__.py
from .test_scenario import test_scenario_bp


def register_routes(app):
    """Register all blueprint routes with the app"""
    app.register_blueprint(test_scenario_bp, url_prefix='/api/scenario')
