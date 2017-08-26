from flask import Blueprint
from flask import current_app, request, abort, jsonify

import ishuhui.tasks.task as task

bp_admin = Blueprint('admin', __name__, url_prefix='/admin')


def login():
    if current_app.config['USERNAME'] != request.args.get('username') or current_app.config['PASSWORD'] != request.args.get('password'):
        abort(404)


bp_admin.before_request(login)


@bp_admin.route('/refresh_comics')
def refresh_comics():
    return jsonify(task.refresh_comics())


@bp_admin.route('/refresh_chapters')
def refresh_chapters():
    return jsonify(task.refresh_chapters())


@bp_admin.route('/refresh_comic_images')
def refresh_comic_images():
    return jsonify(task.refresh_comic_images())
