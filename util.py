#!/usr/bin/env python

import argparse


def is_even(n: int) -> bool:
    """Indicates whether an integer is even.

    Parameters
    ----------
    n: int
        The integer to check for evenness

    Returns
    -------
    Whether the integer is even
    """
    return (n % 2) == 0

def print_evens_odds(data: str) -> None:
    """Prints whether each number in data is even or odd

    Parameters
    ----------
    data: str
        The filename for the data to be read. The file should have
        space-delimited integers.

    Returns
    -------
    None

    Notes
    -----
    This is confusing; consider rewriting

    See Also
    --------
    Nothing
    """
    print('Reading data')
    with open(data, 'r') as f:
        contents = f.read()
    print('Read the data')
    entries = contents.split()
    print('Checking data...')
    for entry in entries:
        n = int(entry)
        if is_even(n):
            print('%d: even' % n)
        else:
            print('%d: odd' % n)
    print('Finished analysing data!')


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--input', help='Path to data')
    args = parser.parse_args()
    print_evens_odds(args.input)


if __name__ == '__main__':
    main()
