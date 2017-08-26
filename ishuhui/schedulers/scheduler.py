from apscheduler.triggers.interval import IntervalTrigger
from flask_apscheduler import APScheduler

from ishuhui.tasks import task

scheduler = APScheduler()


def init_scheduler(app):
    scheduler.init_app(app)

    def __refresh_comics():
        with app.app_context():
            task.refresh_comics()
            task.refresh_comic_images()

    def __refresh_chapters():
        with app.app_context():
            task.refresh_chapters()

    scheduler.add_job('refresh_comics', __refresh_comics, max_instances=1,
                      trigger=IntervalTrigger(weeks=1))

    scheduler.add_job('refresh_chapters', __refresh_chapters, max_instances=1,
                      trigger=IntervalTrigger(hours=1))
    scheduler.start()
