from gpt import GPT

def chgen(n=4, tags=["medieval", "fantasy", "magical"], params = ["race", "class", "name", "hp"]):
    
    characters = []
    
    gpt = GPT(system_msg=
        "You are a Dungeons and dragons Game Master. Your job is to create characters for upcoming campaign."
        "Campaign story should fit into the following tags: " + ", ".join(tags) + "."
        "You will be asked to fill character sheets for couple of characters.\n"
        "Sheet must contain only the following parameters:\n" + ":\n".join(params))
    
    for i in range(n):
        msg = "Character sheet for character number " + str(i+1) + ".\n"        
        response = gpt.chat(msg, append_to_history=False)

        character = {}
        for line in response.split('\n'):
            if ':' not in line: continue
            param, value = line.split(':')
            param = param.strip().lower()
            if param in params:
                character[param] = value.strip()
        
        characters.append(character)

    return characters
        
def example_usage(n=3):
    characters = chgen(n=n, tags=["medieval", "magical", "fantasy"], params=["name", "wealth", "age", "hp"])
    
    for character in characters:
        print("Character: " + character["name"])
        for param, value in character.items():
            if param == "name": continue
            print(param + ": " + value)
        print()

