from ishuhui import create_app

app = create_app('env')
if __name__ == '__main__':
    app.run(host=app.config['HOST'], port=int(app.config['PORT']), debug=app.config['DEBUG'])
