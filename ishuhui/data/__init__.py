from ishuhui.models.chapter import Chapter
from ishuhui.models.comic import Comic


def get_comics():
    return Comic.query.all()


def get_comic(id):
    return Comic.query.order_by(Comic.id.asc()).get(id)


def get_chapters(comic_id=None):
    if comic_id is None:
        return Chapter.query.all()
    return Chapter.query.filter_by(comic_id=comic_id).order_by(Chapter.chapter_number.desc()).all()


def get_chapter(id):
    return Chapter.query.get(id)