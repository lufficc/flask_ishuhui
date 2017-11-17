from celery.schedules import crontab
from celery.task import periodic_task

from .. import create_app
from ..extensions.celeryext import create_celery
from ..tasks import task

app = create_app('env', False)
celery = create_celery(app)


@periodic_task(run_every=(crontab(minute='*/10', hour='3,14,17,20', day_of_week='thu,fri')), name="scheduled_refresh_chapters_task", ignore_result=True)
def scheduled_refresh_chapters_task():
    with app.app_context():
        task.refresh_chapters()


@celery.task(bind=True)
def refresh_chapters_task(self):
    def listener(current, total, result):
        self.update_state(state='PROGRESS', meta={'progress': current / total})

    with app.app_context():
        return {'progress': 1, 'result': task.refresh_chapters(listener)}
