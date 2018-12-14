from flask import Flask, render_template, url_for
app = Flask(__name__, template_folder="templates", static_folder="static")

posts = [
    {
        'author': 'Marcus Chong',
        'title': 'Welcome to Pokedex:',
        'content': 'SELECT AN OPTION:',
        'info': '1. Print/Export Pokemon Info',
        'filter': '2. Filter Pokemon Info',
        'create': '3. Create a new Pokemon',
        'delete': '4. Delete an existing Pokemon',
        'update': '5. Update a Pokemon\'s Description',
    }
]


@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts=posts)


@app.route("/about")
def about():
    return render_template('about.html', title='About')


if __name__ == '__main__':
    app.run(debug=True)