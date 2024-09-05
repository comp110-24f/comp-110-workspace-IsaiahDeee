"""My first exercise in COMP110!"""

__author__ = "730583303"


def main_planner(guests: int) -> None:
    """strings functions together to create a total cost and prints"""
    print("A Cozy Tea Party For " + str(guests) + " People!")
    print("Tea Bags: " + str(tea_bags(people=guests)))
    print("Treats: " + str(treats(people=guests)))
    # remember to define cost parameters, and define nested parameters within.
    # I only have to call the cost function, then define all parameters nested.
    print(
        "Cost: $"
        + str(
            cost(tea_count=tea_bags(people=guests), treat_count=treats(people=guests))
        )
    )


def tea_bags(people: int) -> int:
    """calculates number of tea bags"""
    return people * 2


def treats(people: int) -> int:
    """calculates number of treats"""
    # change float into int, make sure to call tea_bags and define people parameter
    return int(tea_bags(people=people) * 1.5)


def cost(tea_count: int, treat_count: int) -> float:
    """calculates cost of treats and tea"""
    # multiply number of tea bags and treats by corresponding prices and sum together
    return tea_count * 0.5 + treat_count * 0.75


if __name__ == "__main__":
    main_planner(guests=int(input("How many guests are attending your tea party? ")))
