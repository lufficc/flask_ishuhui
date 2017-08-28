<p align="center">
  <img src="https://i.loli.net/2017/08/27/59a2ca890206c.gif" style="width:80%" alt="Ishuhui!"/>
</p>

## Ishuhui

A flask project built for learning. Responsive waterfalls flow by [Masonry](https://masonry.desandro.com/) 
and real time search by [List.js](http://listjs.com).

### Features

* Clear project structure.
* Controllers, logger, scheduler, extensions, models, tasks etc.
* Front end build with [Bootstrap4](https://github.com/twbs/bootstrap), [List.js](http://listjs.com), [Viewer.js](https://fengyuanchen.github.io/viewerjs/), [Masonry](https://masonry.desandro.com/), [MDUI](https://www.mdui.org/), and [imagesLoaded](https://imagesloaded.desandro.com/).

### Dependencies

- `flask_apscheduler`
- `flask_sqlalchemy`
- `lxml`

### Usage

1. `git clone https://github.com/lufficc/flask_ishuhui.git`
1. `cd flask_ishuhui`
1. `python run.py`
1. Open localhost:5000
1. Visit `/admin/refresh_comics?username=<username>&password=<password>` to fill all comics to database.
1. Visit `/admin/refresh_chapters?username=<username>&password=<password>` to fill all chapters to database.

NOTE: `username` and `password` are defined in [env.py](env.py)

### License

Licensed under the [MIT License](http://kbrsh.github.io/license).