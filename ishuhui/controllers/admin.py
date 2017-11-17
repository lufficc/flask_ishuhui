from flask import Blueprint, render_template
from flask import abort, jsonify
from flask_login import current_user

import ishuhui.tasks.task as task
from ..models.chapter import Chapter
from ..models.comic import Comic

bp_admin = Blueprint('admin', __name__, url_prefix='/admin')


def login():
    if not current_user.is_authenticated:
        abort(403)


bp_admin.before_request(login)


@bp_admin.route('/mange', methods=['GET'])
def mange():
    return render_template('mange.html', chapter_count=Chapter.query.count(), comic_count=Comic.query.count(), comics=Comic.query.all())


@bp_admin.route('/refresh_comics')
def refresh_comics():
    return jsonify(task.refresh_comics())


@bp_admin.route('/refresh_chapters')
def refresh_chapters():
    return jsonify(task.refresh_chapters())


@bp_admin.route('/refresh_comic_images')
def refresh_comic_images():
    return jsonify(task.refresh_comic_images())
