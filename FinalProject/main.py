from pokedex import *
from flask import Flask, render_template, url_for
app = Flask(__name__, template_folder="templates")

# apply the blueprints to the app
import pokedex
app.register_blueprint(pokedex.bp)


@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html')

@app.route("/info")
def hello():
    return render_template('info.html')

if __name__ == '__main__':
    app.run(debug=True)

print("------------------------------")
print("WELCOME TO MARCUS'S POKEDEX!!!")
print("------------------------------")

request = -1

while True:
    print("SELECT AN OPTION:")
    print("0. Exit")
    print("1. Print/Export Pokemon Info")
    print("2. Filter Pokemon Info")
    print("3. Create a new Pokemon")
    print("4. Delete an existing Pokemon")
    print("5. Update a Pokemon's Description")

    request = input()

    if request == "0":
        break
    elif request == "1":
        printTable()
    elif request == "2":
        filter()
    elif request == "3":
        create()
    elif request == "4":
        delete()
    elif request == "5":
        updateDescription()
