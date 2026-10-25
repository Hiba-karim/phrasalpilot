def check_answer(exercise, user_answer):
    """Return True if the selected option is correct."""
    options = [option.lower() for option in exercise["options"]]
    answer = user_answer.lower()

    # Reject answers that are not among the available options.
    if answer not in options:
        return False

    return exercise["correct_answer"].lower() == answer




def get_feedback(exercise, user_answer):
    """Explain whether the selected answer fits the exercise."""
    answer = user_answer.lower()
    meaning = exercise["option_meanings"].get(answer)


    if check_answer(exercise, user_answer):
        return f'Correct! "{user_answer}" means  {meaning}.'


    # Invalid input should not be treated as a vocabulary mistake.
    if meaning is None :
        return "Please select one of the available options."

    return (
            f'"{answer}" means {meaning}. '
            f'Here, we need to express: {exercise["target_meaning"]}.'
        )

    
def get_hint(exercise, user_answer):
    """Give a contextual hint without revealing the correct answer."""
    answer = user_answer.lower()

    if check_answer(exercise , answer):
        return ("You already got it right!")

    options = [option.lower() for option in exercise['options']]

    if user_answer.lower() not in options :
        return "Please select one of the available options."

    return (
        f'think about the situation'
        f'{exercise["contextual_hint"]}'
    )