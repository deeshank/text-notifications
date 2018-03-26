from flask import Flask

def create_app(**config_overrides):
    app = Flask(__name__)

    app.config.from_pyfile('settings.py')
    app.config.update(config_overrides)

    from sms.views import sms_svc
    app.register_blueprint(sms_svc)

    return app
