import json

import const


def load_candidates_from_json(path):
    """
    возвращает список всех кандидатов
    :param path:
    :return:
    """

    with open(path, "r", encoding="utf-8") as file:
        return json.load(file)


def get_all_candidates():
    return load_candidates_from_json(const.path)


def get_candidate_by_pk(pk):
    """
    возвращает одного кандидата по его id
    """

    for candidate in get_all_candidates():
        if candidate["id"] == pk:
            return candidate


def get_candidates_by_name(candidate_name):
    """
    Возвращает кандидатов по имени
    """
    result = []
    for candidate in get_all_candidates():
        if candidate_name in candidate["name"].lower():
            result.append(candidate)
    return result


def get_candidates_by_skill(skill_name):
    """
    возвращает кандидатов по навыку
    :param skill_name:
    :return:
    """
    result = []
    for candidate in get_all_candidates():
        if skill_name in candidate["skills"].lower():
            result.append(candidate)
    return result
