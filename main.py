from website import create_app

app = create_app()

if __name__ == '__main__':
    # meaning the server is gonna rerun every time we change the code
    app.run(debug=True)
