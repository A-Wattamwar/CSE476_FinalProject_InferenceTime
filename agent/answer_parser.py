import re
from api import call_model_chat_completions

def classify_question(question):
    system = "You are a question classifier. Reply with exactly one word."
    prompt = f"""Classify this question into ONE category:
- math: calculations, numbers, arithmetic, algebra, geometry
- coding: write code, function, program, algorithm
- planning: sequence of actions, steps, moves, logistics
- future: predictions, forecasts, future events
- general: factual questions, reading comprehension, common sense, multiple choice

Question: {question[:500]}

Reply with exactly one word: math, coding, planning, future, or general"""

    result = call_model_chat_completions(prompt, system=system, temperature=0.0)
    
    if result["ok"]:
        text = result["text"].strip().lower()
        for cat in ["math", "coding", "planning", "future", "general"]:
            if cat in text:
                return cat
    return "general"

def extract_answer(text, question_type="general"):
    if not text:
        return ""
    text = text.strip()
    
    boxed = re.search(r"\\boxed\{([^}]+)\}", text)
    if boxed:
        return boxed.group(1).strip()
    
    for pattern in [r"[Ff]inal [Aa]nswer[:\s]+([^\n]+)", r"[Tt]he answer is[:\s]+([^\n]+)"]:
        match = re.search(pattern, text)
        if match:
            return match.group(1).strip()
    
    if question_type == "math":
        nums = re.findall(r'-?\d+\.?\d*', text)
        if nums:
            return nums[-1]
    
    if len(text) < 200:
        return text
    
    return text.split('\n')[0][:200]

def normalize_answer(answer):
    return str(answer).strip().lower()
