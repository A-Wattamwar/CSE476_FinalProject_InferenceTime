from answer_parser import classify_question, normalize_answer
from technique1_self_consistency import self_consistency
from technique2_cot_verify import cot_with_verification
from technique3_refinement import iterative_refinement
from technique4_pal import pal_solve

def solve(problem):
    q_type = classify_question(problem)
    results = []
    
    if q_type == "math":
        r0 = pal_solve(problem)
        if r0["answer"]:
            results.append(r0)
        r1 = self_consistency(problem, q_type)
        if r1["answer"]:
            results.append(r1)
    
    elif q_type == "general":
        r1 = self_consistency(problem, q_type)
        if r1["answer"]:
            results.append(r1)
        r2 = cot_with_verification(problem, q_type)
        if r2["answer"]:
            results.append(r2)
    
    else:
        r1 = self_consistency(problem, q_type)
        if r1["answer"]:
            results.append(r1)
        r2 = cot_with_verification(problem, q_type)
        if r2["answer"]:
            results.append(r2)
    
    if not results:
        return ""
    
    if q_type in ["coding", "planning"]:
        best_result = max(results, key=lambda x: x["confidence"])
        return best_result["answer"]
    
    weights = {}
    for r in results:
        ans = normalize_answer(r["answer"]) if q_type != "future" else r["answer"]
        conf = r["confidence"]
        weights[ans] = weights.get(ans, 0) + conf
    
    return max(weights, key=weights.get)