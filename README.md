<p align="center">
  <img src="https://i.loli.net/2017/08/27/59a2ca890206c.gif" style="width:80%" alt="Ishuhui!"/>
</p>

## Ishuhui

A flask project built for learning. Responsive waterfalls flow by [Masonry](https://masonry.desandro.com/) 
and real time search by [List.js](http://listjs.com).

### Features

* Clear project structure.
* Controllers, logger, scheduler, extensions, models, tasks etc.
* Front end build with [Bootstrap4](https://github.com/twbs/bootstrap), [List.js](http://listjs.com), [Magnific Popup](http://dimsemenov.com/plugins/magnific-popup/), [Masonry](https://masonry.desandro.com/), [MDUI](https://www.mdui.org/), and [imagesLoaded](https://imagesloaded.desandro.com/).
* Add login.
* Message flash.
* Using `celery` to load data asynchronously (Optional), with a progress dashboard.

### Dependencies

- `flask_sqlalchemy`
- `flask_login`
- `celery`

### Usage

1. `git clone https://github.com/lufficc/flask_ishuhui.git`
1. `cd flask_ishuhui`
1. `python run.py`
1. Open localhost:5000
1. Login using `username` and `password`.
1. Set `ENABLE_CELERY` to `True` if you want to use celery.
1. Start celery by `celery -A ishuhui.tasks.celery_task.celery worker -B -E` in `flask_ishuhui` folde(same folder as `run.py`).

NOTE: `username` and `password` are defined in [env.py](env.py)

### More screenshots

<p align="center">
  <img src="https://i.loli.net/2017/12/05/5a26039a3a834.png" style="width:80%" alt="Latest"/>
  <b>Latest</b>
  <img src="https://i.loli.net/2017/12/05/5a2600e3429b8.png" style="width:80%" alt="One Piece"/>
  <b>One Piece</b>
  <img src="https://i.loli.net/2017/12/05/5a26015d390af.png" style="width:80%" alt="Mange"/>
  <b>Mange Dashboard</b>
</p>


### License

Licensed under the [MIT License](LICENSE).
