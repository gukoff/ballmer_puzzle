from math import log2
from sys import argv

from scipy.optimize import linprog


def choose_straight_middle_left(left_incl, right_incl, n):
    """
    Select the middle element in the interval. In case of a tie, choose the left one.
    """
    return (left_incl + right_incl) // 2


def choose_straight_middle_right(left_incl, right_incl, n):
    """
    Select the middle element in the interval. In case of a tie, choose the right one.
    """
    return (left_incl + right_incl + 1) // 2


def choose_right_leaning(left_incl, right_incl, n):
    """
    Select the rightmost element in the interval that won't increase the worst-case complexity for the binary search.
    """
    search_space_size = right_incl - left_incl + 1
    log_size = int(log2(search_space_size))
    return min(left_incl + 2 ** log_size - 1, right_incl)


def choose_left_leaning(left_incl, right_incl, n):
    """
    Select the leftmost element in the interval that won't increase the worst-case complexity for the binary search.
    """
    search_space_size = right_incl - left_incl + 1
    log_size = int(log2(search_space_size))
    return max(left_incl, right_incl - 2 ** log_size + 1)


def choose_outward_leaning(left_incl, right_incl, n):
    if left_incl > (n - right_incl):
        return choose_right_leaning(left_incl, right_incl, n)
    else:
        return choose_left_leaning(left_incl, right_incl, n)


def predict_wins_binsearch(n: int, first_guess: int, choose_middle_func) -> list[int]:
    """
    :param n: how many elements do we chose from
    :param first_guess: what is the first guess
    :param choose_middle_func: how the binary search should select its next guess
    :returns array - how many $ you will win if Ballmer chose number i
    """
    attempts = [0] * n  # attempts[i] == how many attempts to guess the number i with this strategy

    def fill_attempts(left_incl, right_incl, cur_attempt):
        if left_incl > right_incl:
            return
        middle = choose_middle_func(left_incl, right_incl, n)
        attempts[middle] = cur_attempt
        if left_incl == right_incl:
            return
        fill_attempts(left_incl, middle - 1, cur_attempt + 1)
        fill_attempts(middle + 1, right_incl, cur_attempt + 1)

    attempts[first_guess] = 1
    fill_attempts(0, first_guess - 1, cur_attempt=2)
    fill_attempts(first_guess + 1, n - 1, cur_attempt=2)

    assert all(attempts)  # all items must be guessable with 1 or more attempts

    wins = [
        6 - a  # $5 for guessing on the 1st` attempts, $4 for the 2nd, etc
        for a in attempts
    ]
    return wins  # wins[i] == how many $ you will win if Ballmer chose number i


def prepare_strategies(n):
    named_strategies = {}
    named_strategies.update({
        f'Binary search, first guess {x}. On each step, guess the middle element in the interval. In case of tie, guess the left one.':
            predict_wins_binsearch(n, x, choose_straight_middle_left) for x in range(n)
    })
    named_strategies.update({
        f'Binary search, first guess {x}. On each step, guess the middle element in the interval. In case of tie, guess the right one.':
            predict_wins_binsearch(n, x, choose_straight_middle_right) for x in range(n)
    })
    named_strategies.update({
        f'Binary search, first guess is {x}. On each step, guess the rightmost element in the interval that won\'t increase the worst-case complexity.':
            predict_wins_binsearch(n, x, choose_right_leaning) for x in range(n)
    })
    named_strategies.update({
        f'Binary search, first guess is {x}. On each step, guess the leftmost element in the interval that won\'t increase the worst-case complexity.':
            predict_wins_binsearch(n, x, choose_left_leaning) for x in range(n)
    })
    named_strategies.update({
        f'Binary search, first guess is {x}. On each step, guess the endmost element in the interval that won\'t increase the worst-case complexity.':
            predict_wins_binsearch(n, x, choose_outward_leaning) for x in range(n)
    })

    strategy_names = {}
    strategies = []
    for name, wins in named_strategies.items():
        strategy_names[tuple(wins)] = name
        strategies.append(wins)

    return strategies, strategy_names


def solve(strategies: list[list[float]]):
    """
    Find a linear combination of the strategies so that:
    - all coefficients are non-negative (and correspond to the probability to choose this strategy)
    - all values of the linear combination are positive (i.e. every number wins)
    """
    # Based on the code snippet from https://docs.scipy.org/doc/scipy/reference/generated/scipy.optimize.linprog.html#scipy.optimize.linprog
    strat_len = len(strategies[0])
    c = [1] * len(strategies)  # these values are not essential for this solution, we aren't "minimizing" anything per se
    A = [
        [-strat[idx] for strat in strategies]
        for idx in range(strat_len)
    ]  # transpose and negate
    b = [-1] * strat_len  # also negate. We do it in order to ensure the linear_sum > 0 inequalities rather than <0
    bounds = [[0, None] for _ in range(len(strategies))]
    return linprog(c, A_ub=A, b_ub=b, bounds=bounds, method='highs')


def main(n=100):
    strategies, strategy_names = prepare_strategies(n)

    res = solve(strategies)

    assert res.x is not None, "could not solve"

    normalized_coeffs = res.x / sum(res.x)

    mixed_strategy = [
        float(sum(normalized_coeffs[idx] * s[win_idx] for idx, s in enumerate(strategies)))
        for win_idx in range(len(strategies[0]))
    ]

    mixed_strategy_stdev = [
        float(
            sum(normalized_coeffs[idx] * (s[win_idx] - mixed_strategy[win_idx]) ** 2 for idx, s in enumerate(strategies))
        ) ** 0.5
        for win_idx in range(len(strategies[0]))
    ]

    print('## Winning strategy')
    for strategy, coeff in zip(strategies, normalized_coeffs):  # using the fact they are the same
        if coeff:
            print(f'- With probability {coeff * 100:0.4f}%: {strategy_names[tuple(strategy)]}')

    print('## Average wins for each number')
    for i, (mean_win, stdev_win) in enumerate(zip(mixed_strategy, mixed_strategy_stdev)):
        print(f'{i}: ${mean_win:0.4f} (stdev ${stdev_win**0.5:0.4f})')

    print(f'Avg win if Ballmer chooses randomly: ${sum(mixed_strategy) / len(mixed_strategy)}')
    print(f'Win if Ballmer chooses adversarially: ${min(mixed_strategy)}')


if __name__ == '__main__':
    main(int(argv[1]))
