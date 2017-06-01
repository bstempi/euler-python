"""
This module provides the bits that are used to run the functions that produce the answer.  It also provides bits to
check those answers.
"""
import hashlib
import json
import os


class Problem(object):
    """
    Decorator class that keeps track of which problem numbers map to which solution functions
    """
    problem_map = dict()

    def __init__(self, problem_number):
        self.problem_number = problem_number

    def __call__(self, func):

        # Make sure that element doesn't already exist
        if str(self.problem_number) in self.problem_map:
            raise Exception('Duplicate problem number detected: {}'.format(self.problem_number))

        # Make our entry; the JSON structure that stores the answers keeps the problem numbers as strings.  We will
        # as well to make things easy later.
        self.problem_map[str(self.problem_number)] = func
        return func


class AnswerChecker(object):
    """
    Checks that answers are correct against the list of SHA1 hashed answers
    """

    def __init__(self, answers_file=None):
        if not answers_file:
            answers_file = open(os.path.join(os.path.dirname(__file__),
                                             '../pocket-euler/files/project-euler-sha1-hashed-solutions.json'))
            self.answers = json.load(answers_file)

    def check(self, problem_number, solver_func):
        answer = solver_func()
        m = hashlib.sha1()
        m.update(str(answer).encode('utf-8'))
        hashed_answer = m.hexdigest()

        correct_answer = self.answers[str(problem_number)]
        return correct_answer == hashed_answer, answer, hashed_answer
