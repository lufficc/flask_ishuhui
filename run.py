from ishuhui import create_app

app = create_app('env')
if __name__ == '__main__':
    app.run()
