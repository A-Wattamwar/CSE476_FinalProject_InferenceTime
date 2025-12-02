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