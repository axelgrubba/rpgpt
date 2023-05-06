import random


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
