from random import choice
import response_db as rd


def thats_correct(name):
    return choice(rd.thats_correct).replace("<name>", name).replace("<fname>", name.split()[0])


def render_house_scores(house_scores):
    output = ""
    for i in house_scores:
        if not house_scores[i] == 0:
            output += rd.houses[i] + ": " + str(house_scores[i])
            output += "\n"

    return output


def render_individual_scores(individual_scores):
    output = ""
    for i in individual_scores:
        output += i + ": " + str(individual_scores[i])
        output += "\n"

    return output


def get_winner(house_scores):
    winner = "NULL"
    top = 0
    for i in house_scores:
        if house_scores[i] > top:
            winner = rd.houses[i]
            top = house_scores[i]

    return winner


def render_result(house_scores, individual_scores):
    output = ""
    output += choice(rd.end)
    output += "\n"
    output += choice(rd.wins).replace("<winner>", get_winner(house_scores))
    output += "\n"
    output += render_house_scores(house_scores)
    output += "\n"
    output += choice(rd.individual)
    output += "\n"
    output += render_individual_scores(individual_scores)
    return output
