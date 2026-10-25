# PhrasalPilot 

**Learn workplace English, one phrasal verb at a time.**

PhrasalPilot is a Python project designed to help English learners master phrasal verbs used in professional contexts. It provides multiple-choice exercises, feedback on incorrect answers, and contextual hints to encourage learners to reason about meaning rather than simply memorize definitions.

## Current Features

- **Multiple-choice exercises:** Select an answer from predefined options.
- **Answer validation:** Check whether the selected option is correct.
- **Explanatory feedback:** Understand the meaning of a selected phrasal verb and why it may not fit the intended meaning.
- **Contextual hints:** Receive a hint to help reason through an incorrect answer.
- **Input validation:** Handle invalid answers gracefully.
- **Automated tests:** Verify the learning logic and its behavior for different inputs.

## Project Structure

```text
phrasalpilot/
├── app/
│   └── learning.py       # Answer checking, feedback, and hints
├── data/
│   └── exercises.py     # Exercise content and vocabulary data
├── tests/
│   └── test_learning.py # Tests for the learning logic
├── .env.example         # Example environment configuration
├── .gitignore
└── Readme.md
```

## Getting Started

### Prerequisites

- Python 3.12 or a compatible Python version
- Git

### Installation

Clone the repository:

```bash
git clone https://github.com/Hiba-karim/phrasalpilot.git
cd phrasalpilot
```

Create and activate a virtual environment:

```bash
python -m venv .venv
```

On Windows (Git Bash):

```bash
source .venv/Scripts/activate
```

On macOS or Linux:

```bash
source .venv/bin/activate
```

### Run the Tests

From the project root:

```bash
python -m tests.test_learning
```

A successful run prints `All tests passed!`.

## Example Exercise

**Target meaning:** Postpone something until a later time.

> We need to ___ the launch until Monday.

Choose from:

- put off
- take over
- bring out
- put up

If the learner chooses an incorrect option, PhrasalPilot explains its meaning and offers a contextual hint to encourage another attempt.

## Roadmap

- [ ] Expand the exercise dataset with workplace English vocabulary.
- [ ] Build an interactive user interface.
- [ ] Add retries and progress tracking.
- [ ] Implement spaced repetition (bringing a phrasal verb back for practice after some time has passed, instead of practising it only once) to support long-term retention.
- [ ] Explore AI-generated explanations and adaptive hints.
- [ ] Evaluate learning effectiveness using measurable metrics.

## Project Goal

The long-term goal is to explore whether personalized feedback and adaptive practice can improve vocabulary learning and retention.

PhrasalPilot is an evolving learning project focused on Python development, educational technology, and evidence-based personalization.
