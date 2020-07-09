from flask.blueprints import Blueprint
from app.models import User
from flask import render_template, jsonify, url_for
from app.utils.validator import (
    PATH,
    FORM,
    JSON,
    GET,
    Param,
    Pattern,
    validate_params
)
from app.jobs import send_welcome_email
import logging
from app.extensions import cache

user_bp = Blueprint('users',__name__)


@user_bp.route('/users')
@validate_params(
    Param('name', GET, str, default="lw", required=False)
)

def users(name):
    return render_template("index.html", name=name)
