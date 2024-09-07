import random
from math import log2
from sys import argv

from scipy.optimize import linprog

def binsearch_left_straight(left_incl, right_incl):
    return (left_incl + right_incl) // 2

def binsearch_right_straight(left_incl, right_incl):
    return (left_incl + right_incl + 1) // 2

def binsearch_right_leaning(left_incl, right_incl):
    """
    Select the rightmost element in the interval that won't increase the worst-case complexity for the binary search.
    """
    search_space_size = right_incl - left_incl + 1
    log_size = int(log2(search_space_size))
    return min(left_incl + 2 ** log_size - 1, right_incl)

def binsearch_left_leaning(left_incl, right_incl):
    """
    Select the leftmost element in the interval that won't increase the worst-case complexity for the binary search.
    """
    search_space_size = right_incl - left_incl + 1
    log_size = int(log2(search_space_size))
    return max(left_incl, right_incl - 2 ** log_size + 1)

def binsearch_outward_leaning(n):
    def f(left_incl, right_incl):
        if left_incl > (n - right_incl):
            return binsearch_right_leaning(left_incl, right_incl)
        else:
            return binsearch_left_leaning(left_incl, right_incl)
    return f

def list_then_binsearch(guesses, binsearch):
    def f(left_incl, right_incl):
        for i in guesses:
            if left_incl <= i <= right_incl:
                return i
        return binsearch(left_incl, right_incl)
    return f

def binsearch_avoiding_list(blacklist, binsearch):
    def f(left_incl, right_incl):
        guess = binsearch(left_incl, right_incl)
        if guess not in blacklist:
            return guess
        rightward = [i for i in range(guess, right_incl+1) if i not in blacklist]
        leftward = [i for i in range(guess, left_incl-1, -1) if i not in blacklist]
        if not rightward and not leftward:
            return guess
        if not rightward:
            return leftward[0]
        return rightward[0]
    return f

def list_then_inward(guesses, n):
    def f(left_incl, right_incl):
        leftbound = 0
        rightbound = n-1
        for i in guesses:
            if left_incl <= i <= right_incl:
                return i
            elif leftbound <= i <= rightbound:
                if left_incl < i:
                    last_hop_leftward = True
                    leftbound = max(i, leftbound)
                else:
                    last_hop_leftward = False
                    rightbound = min(i, rightbound)
        # Otherwise we're doing the linear-search part. Are we traversing leftward or rightward?
        # If our last binary-search hop was leftward, then we should traverse rightward,
        # and vice versa.
        if last_hop_leftward:
            return left_incl
        else:
            return right_incl
    return f

def predict_wins(n: int, guesser) -> list[int]:
    """
    :param n: how many elements do we chose from
    :param guesser: function(lo, hi) -> int: what is your next guess
    :returns array - how many $ you will win if Ballmer chose number i
    """
    attempts = [0] * n
    for ballmer in range(n):
        left_incl = 0
        right_incl = n - 1
        count = 0
        while True:
            count += 1
            guess = guesser(left_incl, right_incl)
            if guess == ballmer:
                break
            elif guess < ballmer:
                left_incl = guess + 1
            else:
                right_incl = guess - 1
        attempts[ballmer] = count

    assert all(attempts)  # all items must be guessable with 1 or more attempts

    wins = [
        6 - a  # $5 for guessing on the 1st` attempts, $4 for the 2nd, etc
        for a in attempts
    ]
    return wins  # wins[i] == how many $ you will win if Ballmer chose number i


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


def guess_low_payouts(payouts, length_of_guesses, high=False):
    """
    :param payouts: Ballmer's payout for choosing x
    Assume Ballmer will stick to the numbers with the lowest payouts,
    so we should binary-search among them first; then among the next-highest payouts,
    and so on. Return the list of guesses we should make.
    """
    n = len(payouts)
    sorted_payouts = sorted(set(payouts))
    if high:
      sorted_payouts = sorted_payouts[::-1]
    guesses = []

    def distribute(guesses, batch):
        if batch:
            m = len(batch) // 2
            guesses.append(batch[m])
            distribute(guesses, batch[:m])
            distribute(guesses, batch[m+1:])

    for k in range(n):
        batch = [i for i in range(n) if (payouts[i] >= sorted_payouts[k] if high else payouts[i] <= sorted_payouts[k])]
        if (len(batch) >= length_of_guesses) or (k == len(sorted_payouts)-1):
            distribute(guesses, batch)
            break

    return guesses



def main(n=100):
    named_strategies = {}
    def add_named_strategy(name, guesser):
        named_strategies.update({ name: predict_wins(n, guesser) })

    for i in range(n):
        guesses = [i]
        add_named_strategy(
            f'Guess %r, then left-leaning binary search.' % guesses,
            list_then_binsearch(guesses, binsearch_left_leaning)
        )
        add_named_strategy(
            f'Guess %r, then right-leaning binary search.' % guesses,
            list_then_binsearch(guesses, binsearch_right_leaning)
        )
        add_named_strategy(
            f'Guess %r, then left-straight binary search.' % guesses,
            list_then_binsearch(guesses, binsearch_left_straight)
        )
        add_named_strategy(
            f'Guess %r, then right-straight binary search.' % guesses,
            list_then_binsearch(guesses, binsearch_right_straight)
        )
        add_named_strategy(
            f'Guess %r, then outward-leaning binary search.' % guesses,
            list_then_binsearch(guesses, binsearch_outward_leaning(n))
        )
        add_named_strategy(
            f'Guess %r, then inward linear search.' % guesses,
            list_then_inward(guesses, n)
        )

    length_of_guesses = 2
    old_state = None
    absolute_count = 0
    while True:
        strategy_names = {}
        strategies = []
        for name, wins in named_strategies.items():
            strategy_names[tuple(wins)] = name
            strategies.append(wins)

        print('Solving with %d strategies...' % (len(strategies),))
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
        lines = []
        for strategy, coeff in zip(strategies, normalized_coeffs):  # using the fact they are the same
            if coeff:
                lines += [f'- With probability {coeff * 100:0.4f}%: {strategy_names[tuple(strategy)]}']
        print('\n'.join(sorted(lines)))

        useless_strategies = [s for s, c in zip(strategies, normalized_coeffs) if not c]
        named_strategies = {
            name: wins for name, wins in named_strategies.items() if wins not in useless_strategies
        }
        print('PRUNED %d USELESS STRATEGIES' % len(useless_strategies))

        print('## Average wins for each number')
        for i, (mean_win, stdev_win) in enumerate(zip(mixed_strategy, mixed_strategy_stdev)):
            print(f'{i}: ${mean_win:0.4f} (stdev ${stdev_win**0.5:0.4f})', end=('\n' if (i % 10 == 9) else ' '))

        print(f'Avg win if Ballmer chooses randomly: ${sum(mixed_strategy) / len(mixed_strategy)}')
        print(f'Win if Ballmer chooses adversarially: ${min(mixed_strategy)}')

        state = (-min(mixed_strategy), len(strategies), sum(mixed_strategy))
        if old_state is None or (state < old_state):
            old_state = state
            absolute_count = 0
        else:
            absolute_count += 1
            if absolute_count >= 100:
                length_of_guesses += 1
                if length_of_guesses >= 10:
                    length_of_guesses -= 8

        if max(mixed_strategy) < min(mixed_strategy) + 0.00001:
            print('YOU CAN STOP NOW')

        # input()

        for i in range(10):
            high = random.choice([True, False])
            whitelist = guess_low_payouts(mixed_strategy, int(length_of_guesses), high=False)[:int(length_of_guesses)]
            blacklist = guess_low_payouts(mixed_strategy, int(length_of_guesses), high=True)[:int(length_of_guesses)]
            add_named_strategy(
                f'Guess %r, then inward linear search.' % (whitelist,),
                list_then_inward(whitelist, n)
            )
            add_named_strategy(
                f'Guess %r, then outward-leaning binary search avoiding %r.' % (whitelist, blacklist),
                list_then_binsearch(whitelist, binsearch_avoiding_list(blacklist, binsearch_outward_leaning(n)))
            )
            add_named_strategy(
                f'Guess %r, then left-leaning binary search avoiding %r.' % (whitelist, blacklist),
                list_then_binsearch(whitelist, binsearch_avoiding_list(blacklist, binsearch_left_leaning))
            )
            add_named_strategy(
                f'Guess %r, then right-leaning binary search avoiding %r.' % (whitelist, blacklist),
                list_then_binsearch(whitelist, binsearch_avoiding_list(blacklist, binsearch_right_leaning))
            )
            add_named_strategy(
                f'Guess %r, then left-straight binary search avoiding %r.' % (whitelist, blacklist),
                list_then_binsearch(whitelist, binsearch_avoiding_list(blacklist, binsearch_left_straight))
            )
            add_named_strategy(
                f'Guess %r, then right-straight binary search avoiding %r.' % (whitelist, blacklist),
                list_then_binsearch(whitelist, binsearch_avoiding_list(blacklist, binsearch_right_straight))
            )

if __name__ == '__main__':
    main(int(argv[1]))
