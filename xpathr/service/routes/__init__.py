from .test_scenario import test_scenario_bp

SCENARIO = '/api/scenario'


def register_routes(app):
    app.register_blueprint(test_scenario_bp, url_prefix=SCENARIO)
