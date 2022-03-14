import json

def get_error_message(json_str):
    json_data = json.loads(json_str)
    return json_data["message"]