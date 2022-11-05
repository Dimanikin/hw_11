from flask import Flask, render_template

import utils

app = Flask(__name__)


@app.route('/')
def all_candidate():
    candidates = utils.get_all_candidates()
    return render_template('list.html', candidates=candidates)


@app.route('/candidate/<int:pk>')
def get_candidates_by_id(pk):
    candidates = utils.get_candidate_by_pk(pk)
    return render_template('card.html', candidates=candidates)


@app.route('/search/<candidate_name>')
def search_candidate_by_name(candidate_name):
    candidates = utils.get_candidates_by_name(candidate_name)
    len_by_candidates = len(candidates)
    return render_template('search.html', candidates=candidates, len_by_candidates=len_by_candidates)


@app.route('/skills/<skill>')
def search_candidate_by_skills(skill):
    candidates = utils.get_candidates_by_skill(skill.lower())
    len_by_candidates = len(candidates)
    return render_template('skill.html', candidates=candidates, len_by_candidates=len_by_candidates)


if __name__ == '__main__':
    app.run()
