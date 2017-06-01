import collections
import logging

import click

from euler import p1_25
from euler.framework import Problem, AnswerChecker


@click.group()
def main():
    """
    Entry into the click interface
    :return: 
    """


@main.command()
def run_all():
    # Get the questions and sort them
    question_map = Problem.problem_map
    question_map = collections.OrderedDict(sorted(question_map.items()))

    checker = AnswerChecker()

    for q_number, q_func in question_map.items():
        click.echo('Testing {}...'.format(q_number))

        is_correct, raw_answer, hashed_answer = checker.check(q_number, q_func)

        if is_correct:
            click.echo('CORRECT')
        else:
            click.echo('WRONG')


@main.command()
@click.argument('number', type=int)
def run_one(number):
    click.echo('Testing {}...'.format(number))

    question_map = Problem.problem_map
    checker = AnswerChecker()

    q_func = question_map[str(number)]
    is_correct, raw_answer, hashed_answer = checker.check(str(number), q_func)

    if is_correct:
        click.echo('CORRECT')
    else:
        click.echo('WRONG')

    click.echo('Your answer: {}'.format(raw_answer))

if __name__ == "__main__":
    main()
