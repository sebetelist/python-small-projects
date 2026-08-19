import json


def check_file():
    try:
        with open('data.json', 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return []
    except json.decoder.JSONDecodeError:
        return []
        
def write_file(data):
    with open("data.json", "w") as f:
        json.dump(data, f, indent=2)
        
        
scores = check_file() 
new_score = {"difficulty": "Easy", "attempts": 4}  

scores.append(new_score)

write_file(scores)