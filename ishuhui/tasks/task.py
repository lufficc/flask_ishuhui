import datetime
import json
import requests

import ishuhui.data as data
from ishuhui.extensions.flasksqlalchemy import db
from ishuhui.models.chapter import Chapter
from ishuhui.models.comic import Comic


def load_comics(page):
    response = requests.get(
        "http://www.ishuhui.net/ComicBooks/GetAllBook",
        params={"PageIndex": page})
    return response.json()['Return']['List']


def parse_date(time_str):
    """
    :param time_str: like "/Date(1453196817000)/"
    :return: datetime
    """
    timestamp = int(time_str[6:-2])
    return datetime.datetime.fromtimestamp(timestamp / 1e3)


def fill_comics():
    page = 0
    comics = load_comics(page)
    print('get {} comics of page {}'.format(len(comics), page))
    result = []
    while len(comics) > 0:
        for comic in comics:
            try:
                if Comic.query.get(comic['Id']):
                    print('comic {} already existed'.format(comic['Id']))
                    continue
                newComic = Comic()
                newComic.id = comic['Id']
                newComic.title = comic['Title']
                newComic.description = comic['Explain']
                newComic.refresh_time = parse_date(comic['RefreshTime'])
                newComic.author = comic['Author']
                newComic.classify_id = comic['ClassifyId']
                newComic.front_cover = comic['FrontCover']
                db.session.add(newComic)
                db.session.commit()
                result.append(comic['Id'])
            except Exception as e:
                print('exception occur when save comic {} :{}'.format(comic['Id'], e))
        page += 1
        comics = load_comics(page)
    return result


def load_chapters(page, comic_id):
    response = requests.get(
        "http://www.ishuhui.net/ComicBooks/GetChapterList",
        params={"PageIndex": page,
                "id": comic_id})
    return response.json()['Return']['List']


def fill_chapters():
    comics = data.get_comics()
    result = {}
    for comic in comics:
        comic_id, saved_chapter_num = refresh_chapter(comic.id)
        result[comic_id] = saved_chapter_num
    return result


def refresh_comic_image():
    comics = data.get_comics()
    result = dict()
    for comic in comics:
        front_cover = comic.front_cover
        if 'i.loli.net' in front_cover or 'ooo.0o0.ooo' in front_cover:
            print('comic {} already refreshed'.format(comic.id))
            continue
        image = requests.get(front_cover).content
        files = {'smfile': image}
        response = json.loads(
            requests.post('https://sm.ms/api/upload', files=files).text)
        if response.get('code') == 'success':
            url = response.get('data')['url']
            comic.front_cover = url
            db.session.commit()
            result[comic.id] = url
            print('refresh comic {} cover succeed, url :{}'.format(
                comic.id, url))
        else:
            print('failed comic {}'.format(comic.id))
    return result


def refresh_chapter(comic_id):
    page = 0
    chapters = load_chapters(page, comic_id)
    saved_chapter_num = 0
    while len(chapters) > 0:
        for chapter in chapters:
            try:
                if Chapter.query.get(chapter['Id']):
                    print('Chapter {} already existed'.format(chapter['Id']))
                    continue
                newChapter = Chapter()
                newChapter.id = chapter['Id']
                newChapter.title = chapter['Title']
                newChapter.comic_id = comic_id
                newChapter.chapter_number = chapter['ChapterNo']
                newChapter.front_cover = chapter['FrontCover']
                newChapter.refresh_time = parse_date(chapter['RefreshTime'])
                db.session.add(newChapter)
                saved_chapter_num += 1
            except Exception as e:
                # print(e)
                pass
        page += 1
        chapters = load_chapters(page, comic_id)
    db.session.commit()
    print('saved {} chapters of comic {}'.format(saved_chapter_num, comic_id))
    return comic_id, saved_chapter_num
