import json


def get_task_description() -> dict:
    try:
        with open(r'D:\PycharmProjects\probabilityTheoryLab03\Program\tasks.json', 'r', encoding='utf-8') as f:
            data = json.load(f)
        return data
    except (FileNotFoundError, json.JSONDecodeError, PermissionError):
        return {}