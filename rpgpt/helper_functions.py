import random
from rpgpt.gptapi import GPT

def generate_random_name() -> str:
    vowels = 'aeiou'
    consonants = 'bcdfghjklmnpqrstvwxyz'
    syllables = ['mon', 'fay', 'shi', 'zag', 'lyn', 'thor', 'bor', 'gul', 'dor', 'gar', 'thal', 'mor', 'xan', 'val',
                 'el']

    num_syllables = random.randint(2, 3)  # Randomly choose 2 or 3 syllables
    name = ''
    for _ in range(num_syllables):
        syllable = random.choice(syllables)
        if random.random() < 0.5:  # Add a consonant at the beginning
            syllable = random.choice(consonants) + syllable
        if random.random() < 0.5:  # Add a vowel at the end
            syllable += random.choice(vowels)
        name += syllable
    return name.capitalize()

def imagine_characters(n=4, tags=["medieval", "fantasy", "magical"], params = ["race", "class", "name", "hp"]):
    characters = []
    
    gpt = GPT(system_msg=
        "You are a Dungeons and dragons Game Master. Your job is to create characters for upcoming campaign."
        "Campaign story should fit into the following tags: " + ", ".join(tags) + "."
        "You will be asked to fill character sheets for couple of characters.\n"
        "Sheet must contain only the following parameters:\n" + ":\n".join(params))
    
    for i in range(n):
        msg = "Character sheet for character number " + str(i+1) + ".\n"        
        response = gpt.chat(msg, append_to_history=True)

        character = {}
        for line in response.split('\n'):
            if ':' not in line: continue
            param, value = line.split(':')
            param = param.strip().lower()
            if param in params:
                character[param] = value.strip()
        
        characters.append(character)

    return characters