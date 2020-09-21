import random


def main():
    show_header()
    player = "You"
    ai = "Computer"
    play_game(player, ai)


def show_header():
    print("--------------------------")
    print("- Rock Paper Scissors v1 -")
    print("--------------------------")


def play_game(player_1, player_2):
    rounds = 3
    wins_p1 = 0
    win_sp2 = 0
    rolls = ['rock', 'paper', 'scissors']
    overall_winner = None

    while wins_p1 < rounds and win_sp2 < rounds:

        roll1 = get_roll(player_1, rolls)
        roll2 = random.choice(rolls)

        if not roll1:
            print("Can't play that, exiting ...")
            return

        print(f"{player_1} rolls {roll1}")
        print(f"{player_2} rolls {roll2}")

        winner = check_for_winning_throw(player_1, player_2, roll1, roll2)

        if winner is None:
            print("This round was a tie!")
        else:
            print(f"{winner} takes the round!")
            if winner == player_1:
                wins_p1 += 1
            elif winner == player_2:
                win_sp2 += 1

        print(f"Score is {player_1}: {wins_p1} and {player_2}: {win_sp2}.")
        print()

    if wins_p1 >= rounds:
        overall_winner = player_1
    else:
        overall_winner = player_2

    print(f"{overall_winner} wins the game!")


def check_for_winning_throw(player_1, player_2, roll1, roll2):
    winner = None
    if roll1 == roll2:
        print("The play was tied!")
    elif roll1 == "rock":
        if roll2 == "paper":
            winner = player_2
        elif roll2 == "scissors":
            winner = player_1
    elif roll1 == "paper":
        if roll2 == "scissors":
            winner = player_2
        elif roll2 == "rock":
            winner = player_1
    elif roll1 == "scissors":
        if roll2 == "rock":
            winner = player_2
        elif roll2 == "paper":
            winner = player_1
    return winner


def get_roll(player_name, rolls):
    print("Available rolls:")
    for index, r in enumerate(rolls, start=1):
        print(f"{index}. {r}")

    selected_index = int(input(f"{player_name}, what is your roll? ")) - 1
    if selected_index < 0 or selected_index >= len(rolls):
        print(f"Sorry {player_name}, {selected_index + 1} is out of bounds!")
        return None

    return rolls[selected_index]


if __name__ == '__main__':
    main()
