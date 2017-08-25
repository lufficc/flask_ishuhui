import lxml.html
from flask import render_template, Blueprint, json, abort

import ishuhui.data as data
from ishuhui.extensions.flasksqlalchemy import db

bp_comic = Blueprint('comic', __name__)


@bp_comic.route('/')
def index():
    comics = data.get_comics()
    return render_template('index.html', comics=comics)


@bp_comic.route('/comics/<int:comic_id>/chapters')
def chapters(comic_id):
    comic = data.get_comic(comic_id)
    chapters = data.get_chapters(comic_id)
    return render_template('chapters.html', comic=comic, chapters=chapters)


def get_images_from_url(url):
    tree = lxml.html.parse(url)
    images = tree.xpath("//img/@src")
    return images


@bp_comic.route('/refresh_chapters/<int:chapter_id>', methods=['GET'])
def refresh_chapter(chapter_id):
    chapter = data.get_chapter(chapter_id)
    url = 'http://www.ishuhui.net/ComicBooks/ReadComicBooksToIsoV1/' + str(
        chapter_id) + '.html'
    images = get_images_from_url(url)
    chapter.images = json.dumps(images)
    db.session.commit()
    return json.dumps(images)


@bp_comic.route('/comics/<int:comic_id>/chapters/<int:chapter_id>')
def chapter(comic_id, chapter_id):
    comic = data.get_comic(comic_id)
    chapter = data.get_chapter(chapter_id)
    next_chapter = data.get_next_chapter(comic_id, chapter.chapter_number)
    prev_chapter = data.get_prev_chapter(comic_id, chapter.chapter_number)
    url = 'http://www.ishuhui.net/ComicBooks/ReadComicBooksToIsoV1/' + str(
        chapter_id) + '.html'
    if chapter.comic_id != comic_id:
        abort(404)
    if chapter.images:
        images = json.loads(chapter.images)
    else:
        images = get_images_from_url(url)
        chapter.images = json.dumps(images)
        db.session.commit()
    return render_template(
        'images.html', comic=comic, chapter=chapter, next_chapter=next_chapter, prev_chapter=prev_chapter,
        images=images, url=url)


@bp_comic.route('/latest')
def latest_chapters():
    chapters = data.get_latest_chapters()
    comic = data.get_comic(2)
    return render_template('chapters.html', comic=comic, chapters=chapters)
