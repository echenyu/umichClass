from time import time

def group(seq):
    """Divide a sequence of at least 12 elements into groups of 4
    or 5. Groups of 5 will be at the end. Returns a tuple of
    sequences, each corresponding to a group, with type matching
    that of the input sequence.

    >>> group(range(14))
    (range(0, 4), range(4, 9), range(9, 14))
    >>> group(tuple(range(17)))
    ((0, 1, 2, 3), (4, 5, 6, 7), (8, 9, 10, 11), (12, 13, 14, 15, 16))
    """

    res = list()
    # We can determine the number of four sets we need, and then recursively call 
    # with this count to save us the trouble of creating many base cases
    number_of_four_sets = (len(seq) // 4) - (len(seq) % 4)

    group_helper(seq, res, number_of_four_sets)
    return tuple(res)

def group_helper(seq, res, count):
    if(len(seq) == 0):
        return
    if(count > 0):
        res.append(seq[0:4])
        group_helper(seq[4:], res, count-1)
    else:
        res.append(seq[0:5])
        group_helper(seq[5:], res, count)

def make_accumulator():
    """Return an accumulator function that takes a single numeric
    argument and accumulates that argument into total, then
    returns total.

    >>> acc = make_accumulator()
    >>> acc(15)
    15
    >>> acc(10)
    25
    >>> acc2 = make_accumulator()
    >>> acc2(7)
    7
    >>> acc3 = acc2
    >>> acc3(6)
    13
    >>> acc2(5)
    18
    >>> acc(4)
    29
    """
    # replace with your solution
    current_val = 0
    def accumulate(value):
        nonlocal current_val
        current_val += value
        return current_val
    return accumulate

def memoize(fn):
    """Return a function that computes the same result as fn, but
    if a given set of arguments has already been seen before,
    returns the previously computed result instead of repeating
    the computation. Assumes fn is a pure function (i.e. has no
    side affects), and that all arguments to fn are hashable.

    >>> @memoize
    ... def sum_to_n(n):
    ...     return 1 if n == 1 else n + sum_to_n(n - 1)
    >>> try:
    ...     sum_to_n(300)
    ...     sum_to_n(600)
    ...     sum_to_n(900)
    ...     sum_to_n(1200)
    ... except RecursionError:
    ...     print('recursion limit exceeded')
    45150
    180300
    405450
    720600
    >>> @memoize
    ... def sum_k_to_n(k, n):
    ...     return k if n == k else n + sum_k_to_n(k, n - 1)
    >>> try:
    ...     sum_k_to_n(2, 300)
    ...     sum_k_to_n(2, 600)
    ...     sum_k_to_n(2, 900)
    ...     sum_k_to_n(2, 1200)
    ... except RecursionError:
    ...     print('recursion limit exceeded')
    45149
    180299
    405449
    720599
    """
    # replace with your solution
    memorized = {}
    def memoize_helper(*args):
        if args not in memorized:
            memorized[args] = fn(*args)
        return memorized[args]
    return memoize_helper

class Timer:
    """A timer class that can be used as a context manager with
    the 'with' statement. The constructor must be passed a
    function or callable to be used to determine the current
    time. Initializes the total time to 0. For each entry and
    exit pair, adds the time between the two calls to the total
    time, using the timer function or callable to read the
    current time.

    >>> class Counter:
    ...     def __init__(self):
    ...         self.count = 0
    ...     def __call__(self):
    ...         self.count += 1
    ...         return self.count - 1
    >>> t = Timer(Counter())
    >>> t.total()
    0
    >>> with t:
    ...    t.total()
    0
    >>> t.total()
    1
    >>> with t:
    ...    t.total()
    1
    >>> t.total()
    2
    >>> t2 = Timer(Counter())
    >>> with t2:
    ...    t2.total()
    0
    >>> t2.total()
    1
    >>> t.total()
    2
    """
    def __init__(self, time_fn):
        # replace with your solution
        self.time_fn = time_fn
        self.count = 0
    def __enter__(self):
        self.enter_time = self.time_fn()
    def __exit__(self, *args):
        self.exit_time = self.time_fn();
        self.count = self.count + (self.exit_time - self.enter_time)
    def total(self):
    # replace with your solution
    # add any other members you need
        return self.count