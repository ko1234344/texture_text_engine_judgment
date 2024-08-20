#try using chatgpt 4
import openai

openai.api_key = "api-key"

def texture_text_engine_judgment(prompt):
    response = openai.ChatCompletion.create(
    model="gpt-4o-mini",
    messages=[
      {"role": "system", "content": "answer with only yes, no. Try answers with two"},
      {"role": "user", "content": prompt},
    ]
)
    if "yes" in response['choices'][0]['message']['content'] or "Yes" in response['choices'][0]['message']['content']:
        return True
    elif "no" in response['choices'][0]['message']['content'] or "No" in response['choices'][0]['message']['content'] :
        return False
    else:
        return "Error"