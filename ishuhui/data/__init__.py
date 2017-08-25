from ishuhui.models.chapter import Chapter
from ishuhui.models.comic import Comic
from sqlalchemy import and_


def get_comics():
    return Comic.query.all()


def get_comic(comic_id):
    return Comic.query.get(comic_id)


def get_chapters(comic_id=None):
    if comic_id is None:
        return Chapter.query.order_by(Chapter.chapter_number.desc()).all()
    return Chapter.query.filter_by(comic_id=comic_id).order_by(Chapter.chapter_number.desc()).all()


def get_next_chapter(comic_id, chapter_number):
    chapter = Chapter.query.filter(
        and_(Chapter.comic_id == comic_id, Chapter.chapter_number > chapter_number)).order_by(
        Chapter.chapter_number.asc()).first()
    return chapter


def get_prev_chapter(comic_id, chapter_number):
    chapter = Chapter.query.filter(
        and_(Chapter.comic_id == comic_id, Chapter.chapter_number < chapter_number)).order_by(
        Chapter.chapter_number.desc()).first()
    return chapter


def get_chapter(chapter_id):
    return Chapter.query.get(chapter_id)


def get_latest_chapters():
    return Chapter.query.order_by(Chapter.refresh_time.desc()).limit(10).all()
