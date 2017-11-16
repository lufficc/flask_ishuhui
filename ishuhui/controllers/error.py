from flask import render_template, Blueprint

bp_error = Blueprint('error', __name__, template_folder="../templates/error")


@bp_error.app_errorhandler(403)
def page_not_found(error):
    return render_template('error.html', error=error), 403


@bp_error.app_errorhandler(404)
def page_not_found(error):
    return render_template('error.html', error=error), 404


@bp_error.app_errorhandler(500)
def server_error(error):
    return render_template('error.html', error=error), 500
