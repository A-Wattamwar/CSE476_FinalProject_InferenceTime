# Reasoning Agent - CSE 476 Final Project

**GitHub Repository:** https://github.com/A-Wattamwar/CSE476_FinalProject_InferenceTime.git

## How the Agent Works

### Three Core Components

1. **Question Classifier** (`answer_parser.py`, `classify_question()` function, lines 4-24)
   - Uses an LLM call to classify questions into types: math, coding, planning, future, general
   - Enables type-specific prompting and answer extraction

2. **Inference Techniques** (4 techniques implemented):
   - **Self-Consistency** (`technique1_self_consistency.py`, `self_consistency()`, lines 5-32): Generates 3 samples with varying temperatures, uses majority voting to select the most common answer
   - **Chain-of-Thought with Verification** (`technique2_cot_verify.py`, `cot_with_verification()`, lines 4-27): Step-by-step reasoning followed by a verification LLM call
   - **Iterative Refinement** (`technique3_refinement.py`, `iterative_refinement()`, lines 4-37): Generate answer, critique it, refine based on feedback
   - **PAL (Program-Aided Language)** (`technique4_pal.py`, `pal_solve()`, lines 4-30): For math problems, generates Python code and executes it locally for accurate computation

3. **Answer Orchestrator** (`agent.py`, `solve()` function, lines 7-47)
   - Routes questions to appropriate techniques based on type
   - math: PAL + Self-Consistency
   - general/coding/planning/future: Self-Consistency + CoT Verification
   - Combines answers using confidence-weighted voting
   - Returns the highest-confidence answer

### Additional Highlights

- Type-specific prompts for each question category
- Type-specific answer extraction (`answer_parser.py`, `extract_answer()` and helper functions)
- PAL technique improves math accuracy through code execution
- Under 20 API calls per question

## Setup and Installation

1. **Clone the repository:**
```bash
git clone https://github.com/A-Wattamwar/CSE476_FinalProject_InferenceTime.git
cd CSE476_FinalProject_InferenceTime
```

## Requirements

- ASU VPN or ASU network connection (required to access the API)

- Python Requests

```bash
pip3 install requests
```

I originally tried installing requests with the code above. 
But that didn't work on my Mac, probably because macOS protects certain system‑managed Python packages. The command that actually worked was:

```bash
pip3 install --break-system-packages requests
```

## How to Run on a New Test Case

**Option 1: Test a single question in Python**
```python
import sys
sys.path.insert(0, "path/to/agent")
from agent import solve

# Math question
print(solve("What is 25 * 4?"))  # 100

# General question
print(solve("What is the capital of France?"))  # paris

# Coding question
print(solve("Write code to add two numbers"))
```

**Option 2: From command line**
```bash
cd agent
python3 -c "from agent import solve; print(solve('Your question here'))"
```

**Option 3: Run on full test dataset**
```bash
cd given/cse476_final_project_submission
python3 generate_answer_template.py
```

This generates `cse_476_final_project_answers.json` for submission.

## Development & Evaluation

### How I Built It

1. Started with the API wrapper (`api.py`), this was pre-given in final_project_tutorial.ipynb file.
2. Built the question classifier to route questions to the right technique
3. Implemented each technique in separate files: Self-Consistency first, then CoT, then Iterative Refinement, then PAL
4. Created answer extractors for different question types (math needs numbers, coding needs code blocks, etc.)
5. Added confidence scores to each technique so I could combine their results
6. Added safety checks in PAL to skip code with loops (was causing hangs)

### How I Tested It

- Used the dev dataset (`cse476_final_project_dev_data.json`) to test
- Ran sample questions from each category and checked outputs, check out test_agent.py
- Fixed common issues like empty answers, answers with too much explanation
- Kept tweaking prompts to get cleaner outputs
- Used 3 samples for self-consistency to balance speed vs accuracy

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
