from flask import Blueprint, render_template, current_app
from bottler.auth import requires_auth

plan = Blueprint('index', __name__)


@plan.route('/', methods=['GET'])
@requires_auth
def root():
    return render_template('index.html',
                           site_name=current_app.config.get('SITE_NAME'))
