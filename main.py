from website import create_app

app = create_app()

if __name__ == '__main__': #makes sure the below is executed only when you run main.py file not when you import it
    app.run(debug=True)