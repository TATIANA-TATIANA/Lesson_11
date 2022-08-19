import json


def load_json():
    """
    Возвращает список всех кандидатов
    """
    with open("candidates.json", "r", encoding="utf-8") as i:
        new_list = json.load(i)
        return new_list


def get_candidate(id):
    """
    Возвращает одного кандидата по его id
    """
    candidates_list = load_json()
    for candidate in candidates_list:
        if candidate["id"] == id:
            return candidate


def get_candidates_by_name(candidate_name):
    """
    Возвращает кандидатов по имени
    """
    candidates_list = load_json()
    suitable_candidates = []
    for candidate in candidates_list:
        if candidate["name"] == candidate_name:
            suitable_candidates.append(candidate)
    return suitable_candidates


def get_candidates_by_skill(skill):
    """
    Возвращает кандидатов по навыку
    """
    candidates_list = load_json()
    suitable_candidates = []
    for candidate in candidates_list:
        if skill.lower() in candidate["skills"].lower().split(", "):
            suitable_candidates.append(candidate)
    return suitable_candidates
