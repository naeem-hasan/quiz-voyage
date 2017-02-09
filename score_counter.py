house_scores = {"s": 0, "g": 0, "h": 0, "r": 0}
individual_scores = {}


def process_scores(house, person, point):
    global house_scores, individual_scores
    house_scores[house] += point
    if person in individual_scores:
        individual_scores[person] += point
    else:
        individual_scores[person] = point
