# Reasoning Agent - CSE 476 Final Project

## How the Agent Works

### Three Core Components

1. **Question Classifier** (`answer_parser.py`, `classify_question()` function, lines 4-24)
   - Uses an LLM call to classify questions into types: math, coding, planning, future, general
   - Enables type-specific prompting and answer extraction

2. **Inference Techniques** (4 techniques implemented):
   - **Self-Consistency** (`technique1_self_consistency.py`, `self_consistency()`, lines 5-32): Generates 3 samples with varying temperatures, uses majority voting to select the most common answer
   - **Chain-of-Thought with Verification** (`technique2_cot_verify.py`, `cot_with_verification()`, lines 4-27): Step-by-step reasoning followed by a verification LLM call
   - **Iterative Refinement** (`technique3_refinement.py`, `iterative_refinement()`, lines 4-37): Generate answer, critique it, refine based on feedback
   - **PAL (Program-Aided Language)** (`technique4_pal.py`, `pal_solve()`, lines 4-24): For math problems, generates Python code and executes it locally for accurate computation

3. **Answer Orchestrator** (`agent.py`, `solve()` function, lines 4-40)
   - Runs all techniques and collects results
   - Combines answers using confidence-weighted voting
   - Returns the highest-confidence answer

### Additional Highlights

- Type-specific prompts for each question category
- Type-specific answer extraction (`answer_parser.py`, `extract_answer()` and helper functions)
- PAL technique improves math accuracy through code execution
- Under 20 API calls per question

## Development & Evaluation

- Developed and evaluated using the provided dev data (`cse476_final_project_dev_data.json`)
- Tested with a script that samples random questions from each domain
- Iteratively improved answer parsing based on output format analysis

## How to Run on a New Test Case

```python
import sys
sys.path.insert(0, "path/to/agent")
from agent import solve

question = "Your question here"
answer = solve(question)
print(answer)
```

## Generate Submission File

```bash
cd given/cse476_final_project_submission
python3 generate_answer_template.py
```

This generates `cse_476_final_project_answers.json` for submission.

## Requirements

- ASU VPN or ASU network connection (required to access the API)

- Python Requests

```bash
pip3 install requests
```

I originally tried installing requests with the code above. 
But that didn’t work on my Mac, probably because macOS protects certain system‑managed Python packages. The command that actually worked was:

```bash
pip3 install --break-system-packages requests
```

## Project Structure

```
agent.py                        # Main orchestrator - solve() function
answer_parser.py                # Question classifier + answer extraction
api.py                          # API wrapper for LLM calls
technique1_self_consistency.py  # Self-consistency with majority voting
technique2_cot_verify.py        # Chain-of-thought with verification
technique3_refinement.py        # Iterative refinement
technique4_pal.py               # Program-aided language for math
README.md                       # This file
```

## Author

**Ayush Sachin Wattamwar**

This project was developed as a final project for a course at Arizona State University. 

CSE476 - Introduction to Natural Language Processing.