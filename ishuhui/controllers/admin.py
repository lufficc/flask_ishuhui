from flask import Blueprint, render_template, current_app
from flask import abort, jsonify
from flask_login import current_user

import ishuhui.tasks.task as task
from ..models.chapter import Chapter
from ..models.comic import Comic
from ..tasks.celery_task import refresh_chapters_task

bp_admin = Blueprint('admin', __name__, url_prefix='/admin')


@bp_admin.before_request
def login():
    if not current_user.is_authenticated:
        abort(403)


@bp_admin.route('/mange', methods=['GET'])
def mange():
    return render_template('mange.html', chapter_count=Chapter.query.count(),
                           comic_count=Comic.query.count(),
                           comics=Comic.query.all(),
                           enable_celery=current_app.config['ENABLE_CELERY'])


@bp_admin.route('/refresh_comics')
def refresh_comics():
    return jsonify(task.refresh_comics())


@bp_admin.route('/refresh_chapters')
def refresh_chapters():
    if current_app.config['ENABLE_CELERY']:
        t = refresh_chapters_task.apply_async()
        return t.id
    return jsonify(task.refresh_chapters())


@bp_admin.route('/tasks/status/<task_id>')
def task_status(task_id):
    result = refresh_chapters_task.AsyncResult(task_id)
    if result.state == 'PENDING':
        response = {
            'state': result.state,
            'progress': 0,
        }
    elif result.state != 'FAILURE':
        response = {
            'state': result.state,
            'progress': result.info.get('progress', 0),
        }
        if 'result' in result.info:
            response['result'] = result.info['result']
    else:
        # something went wrong in the background job
        response = {
            'state': result.state,
            'progress': 0,
            'status': str(result.info),  # this is the exception raised
        }
    return jsonify(response)


@bp_admin.route('/refresh_comic_images')
def refresh_comic_images():
    return jsonify(task.refresh_comic_images())
