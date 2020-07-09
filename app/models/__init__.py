from sqlalchemy_utils import force_auto_coercion
force_auto_coercion()
from .user import User, Role

def init_app(app):
    pass