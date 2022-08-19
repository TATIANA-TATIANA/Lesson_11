from flask import Flask, render_template
from service import load_json, get_candidate, get_candidates_by_name, get_candidates_by_skill

app = Flask(__name__)


@app.route("/")
def main_page():
    candidates = load_json()
    return render_template("list.html", candidates=candidates)


@app.route("/candidate/<int:uid>")
def candidate_page(uid):
    candidate = get_candidate(uid)
    return render_template("card.html", candidate=candidate)


@app.route("/search/<candidate_name>")
def search_candidates_by_name(candidate_name):
    candidates = get_candidates_by_name(candidate_name)
    return render_template("search.html", candidates=candidates)


@app.route("/skill/<skill_name>")
def search_candidates_by_skill(skill_name):
    candidates = get_candidates_by_skill(skill_name)
    return render_template("skill.html", skill=skill_name, candidates=candidates)


app.run()
