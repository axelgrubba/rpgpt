import openai

# this shouldnt be here probably
openai.api_key = open("OPENAI_API_KEY.txt", "r").read().strip("\n")

def generate_image(prompt):
    return openai.Image(prompt=prompt)
