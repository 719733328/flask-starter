from flask import Flask


def init_app(app):
    from .errors import init_app as errors_init
    from .users import user_bp
    errors_init(app)
    app.register_blueprint(user_bp)