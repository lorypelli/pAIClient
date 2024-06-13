from utils.client import gpt


def openai_response(model: str, messages: list):
    try:
        res = gpt.chat.completions.create(
            temperature=0.0, model=model, messages=messages, stream=True
        )
        for c in res:
            if c.choices[0].delta.content:
                yield c.choices[0].delta.content
    except:
        raise Exception("There was an error")
