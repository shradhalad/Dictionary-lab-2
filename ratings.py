"""Restaurant rating lister."""


def rest_ratings(file_name):

    file = open(file_name)
    rest_scores = {}

    for line in file:
        name, score = line.rstrip().split(":")
        rest_scores[name] = score

    file.close()
    return rest_scores

def print_ratings(rest_scores):

    for name, score in sorted(rest_scores.items()):
        print(f"{name} is rated at {score}.")

def add_rest(rest_scores):
     restaurant = input("Restaurant name: ")
     while True:
        score = input("Restaurant score: ")
        try:
            score = int(score)
            if score > 5 or score < 1:
                print("Invalid input: please enter a number between 1 and 5")
            else:
                break
        except ValueError:
            print("Invalid input: please enter a number between 1 and 5")

     rest_scores[restaurant] = score


def update_rest(rest_scores):
     while True:
        restaurant = input("Restaurant name: ")
        if rest_scores.get(restaurant) is None:
            print("Invalid input, please select from existing list of restaurants")
        else:
            break

     while True:
        score = input("Restaurant score: ")
        try:
            score = int(score)
            if score > 5 or score < 1:
                print("Invalid input: please enter a number between 1 and 5")
            else:
                break
        except ValueError:
            print("Invalid input: please enter a number between 1 and 5")

     rest_scores[restaurant] = score


rest_scores = rest_ratings("scores.txt")
print_ratings(rest_scores)
# add_rest(rest_scores)
update_rest(rest_scores)
print_ratings(rest_scores)
