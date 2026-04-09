# quiz_app.py

"""
Project: Simple Quiz Application
A console-based quiz app with multiple choice questions.
"""

questions = [
    {
        "question": "What is the capital of France?",
        "options": ["A. Berlin", "B. Madrid", "C. Paris", "D. Rome"],
        "answer": "C"
    },
    {
        "question": "Which programming language is known as the snake language?",
        "options": ["A. Java", "B. Python", "C. C++", "D. Ruby"],
        "answer": "B"
    }
]

def run_quiz():
    score = 0
    for q in questions:
        print(f"\n{q['question']}")
        for opt in q['options']:
            print(opt)
        
        # Simulated answer
        user_answer = q['answer'] 
        print(f"User chose: {user_answer}")
        
        if user_answer == q['answer']:
            score += 1
            print("Correct!")
        else:
            print("Wrong!")
            
    print(f"\nFinal Score: {score}/{len(questions)}")

run_quiz()
