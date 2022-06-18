from flask import Flask, render_template, request

from repos.exceptions import GitHubApiException
from repos.api import repos_with_most_stars

app = Flask(__name__)
available_languages = ["Javascript", "Python", "Go", "Java", "Kotlin", "Ruby", "PHP"]

@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'GET':
        selected_languages = available_languages
    elif request.method == 'POST':
        selected_languages = request.form.getlist("languages")
    results = repos_with_most_stars(selected_languages)

    return render_template(
        'index.html',
        selected_languages=selected_languages,
        available_languages=available_languages,
        results=results
    )

@app.errorhandler(GitHubApiException)
def handle_api_error(error):
    return render_template('error.html', message=error)