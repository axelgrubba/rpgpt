import openai

# this shouldnt be here probably
openai.api_key = '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'

class GPT:
    def __init__(self, model="gpt-3.5-turbo", system_msg=None):
        self.model = model
        self.system_msg = system_msg
        self.message_history = []

        if self.system_msg is not None:
            self.message_history.append({"role": "user", "content": self.system_msg})
            self.message_history.append({"role": "assistant", "content": "Sure thing!"})

    def chat(self, input, append_to_history=False):
        
        self.message_history.append({"role": "user", "content": input})
    
        completion = openai.ChatCompletion.create(
          model=self.model,
          messages=self.message_history
        )
        reply_content = completion.choices[-1].message.content
        
        if append_to_history:
            self.message_history.append({"role": "assistant", "content": reply_content})
        else:
            self.message_history.pop()

        return reply_content
    
    def clear_history(self):
        self.message_history = []