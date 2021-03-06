import collections
import logging

import click

import p1_25
import p26_50
from framework import Problem, AnswerChecker


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
        click.echo('Answer to {}: {}'.format(q_number, raw_answer))

        if is_correct:
            click.echo(click.style('CORRECT', fg='green'))
        else:
            click.echo(click.style('WRONG', fg='red'))


@main.command()
@click.argument('number', type=int)
def run_one(number):
    click.echo('Testing {}...'.format(number))

    question_map = Problem.problem_map
    checker = AnswerChecker()

    if number not in question_map:
        click.echo(click.style('Problem does not have a solution', fg='red'))
        return

    q_func = question_map[number]
    is_correct, raw_answer, hashed_answer = checker.check(str(number), q_func)

    if is_correct:
        click.echo(click.style('CORRECT', fg='green'))
    else:
        click.echo(click.style('WRONG', fg='red'))

    click.echo('Your answer: {}'.format(raw_answer))


if __name__ == "__main__":
    main()
