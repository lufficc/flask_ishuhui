from flask import Blueprint
import ishuhui.tasks.task as task
from flask import current_app, request, abort, jsonify

bp_admin = Blueprint('admin', __name__, url_prefix='/admin')


def login():
    if current_app.config['USERNAME'] != request.args.get('username') or current_app.config['PASSWORD'] != request.args.get('password'):
        abort(404)


bp_admin.before_request(login)


@bp_admin.route('/fill_comics')
def fill_comics():
    return jsonify(task.fill_comics())


@bp_admin.route('/fill_chapters')
def fill_chapters():
    return jsonify(task.fill_chapters())


@bp_admin.route('/refresh_comic_image')
def refresh_comic_image():
    return jsonify(task.refresh_comic_image())
