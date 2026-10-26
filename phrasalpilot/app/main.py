from data.exercises import EXERCISES
from app.learning import  check_answer, get_feedback , get_hint

exercise = EXERCISES[0]

def run_exercise(exercise):
    print(exercise["sentence"])
    for idx , value in enumerate(exercise['options']):
        print(f'{idx+1}. {value}')

    choice = int(input("Choose an option (1-4):"))
    retrieved_choice = exercise['options'][choice-1]

    while "Correct!" not in get_feedback(exercise, retrieved_choice):
        print(get_feedback(exercise, retrieved_choice))
        choice = int(input("Choose an option (1-4):"))
        retrieved_choice = exercise['options'][choice-1]

    print(get_feedback(exercise, retrieved_choice))
if __name__ == "__main__":
    run_exercise(exercise)