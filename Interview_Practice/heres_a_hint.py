import copy 

question_template = {
    "title": "default title",
    "question": "default question",
    "answer": "default answer",
    "hints": []
}

def make_new_question(title, question, answer, hints=None):
    #copy.deepcopy will make sure we're not just copying the list reference
    #but actually getting a new list object for hints.
    new_q = copy.deepcopy(question_template)

    # always require title, question, answer
    new_q["title"] = title
    new_q["question"] = question
    new_q["answer"] = answer

    # sometimes there aren't hints, that's fine. Otherwise, add them:
    if hints is not None:
        new_q["hints"].extend(hints)

    return new_q

if __name__ == "__main__":
    question_1 = make_new_question("title1", "question1", "answer1", ["q1 hint1", "q1 hint2"])
    question_2 = make_new_question("title2", "question2", "answer2")
    question_3 = make_new_question("title3", "question3", "answer3", ["q3 hint1"])

    print(question_1)
    print(question_2)
    print(question_3)