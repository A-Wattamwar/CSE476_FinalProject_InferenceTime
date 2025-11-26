from collections import Counter
from api import call_model_chat_completions
from answer_parser import extract_answer, normalize_answer

def self_consistency(problem, q_type="general", num_samples=3):
    system = "Give only the final answer. No explanation."
    
    answers = []
    for i in range(num_samples):
        temp = 0.0 if i == 0 else 0.3
        result = call_model_chat_completions(problem, system=system, temperature=temp)
        if result["ok"] and result["text"]:
            answer = extract_answer(result["text"], q_type)
            if answer:
                answers.append(answer)
    
    if not answers:
        return {"answer": "", "confidence": 0.0}
    
    counts = Counter([normalize_answer(a) for a in answers])
    best, count = counts.most_common(1)[0]
    
    for a in answers:
        if normalize_answer(a) == best:
            return {"answer": a, "confidence": count / len(answers)}
    
    return {"answer": answers[0], "confidence": 0.5}