import openai


import openai
import json

def build_goal_generation_prompt(user_quality_scores, category_slug):
    # Build a text prompt for OpenAI
    ...

def call_openai_for_goals(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": "You are a career advisor/goal generation assistant."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.2,
        max_tokens=2000
    )
    content = response['choices'][0]['message']['content']
    return json.loads(content)

def generate_user_goals(user_quality_scores, category_slug):
    prompt = build_goal_generation_prompt(user_quality_scores, category_slug)
    return call_openai_for_goals(prompt)
