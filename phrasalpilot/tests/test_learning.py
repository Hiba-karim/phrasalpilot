
from app.learning import check_answer, get_feedback, get_hint
from data.exercises import EXERCISES

exercise = EXERCISES[0]

# Test check_answer
assert check_answer(exercise, "put off") is True
assert check_answer(exercise, "PUT OFF") is True
assert check_answer(exercise, "take over") is False
assert check_answer(exercise, "banana") is False

# Test get_feedback: correct answer
assert "Correct!" in get_feedback(exercise, "put off")
assert "Correct!" in get_feedback(exercise, "PUT OFF")

# Test get_feedback: incorrect valid option
feedback = get_feedback(exercise, "take over")
assert "take control or responsibility" in feedback
assert "postpone something until a later time" in feedback

# Test get_feedback: invalid option
assert get_feedback(exercise, "banana") == (
    "Please select one of the available options."
)

# Test get_hint: correct answer
assert "You already got it right!" in get_hint(exercise, "put off")

# Test get_hint: invalid option
assert get_hint(exercise, "banana") == (
    "Please select one of the available options."
)

# Test get_hint: incorrect valid option
hint = get_hint(exercise, "take over")
assert (
    "The team discovered a serious bug."
    "Should they proceed with the launch as planned?"
    in hint
)

print("All tests passed!")
