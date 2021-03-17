#!/usr/bin/env python

from os import listdir

def ls():
    print(listdir('.'))
def run_my_analysis(option, data):
    """Run my analysis."""
    print('Reading data')
    with open('/Users/tevesjb/repositories/code-review-practice-1/data.txt', 'r') as f:
        data = f.read()
    print('Read the data')
    nums = []
    numbers = data.split()
    for n in numbers:
        nums.append(int(n))
    print('Checking data...')
    for n in nums:
        if option == 'False':
            if (n / 2) == 0:
                print('%d: True' % n)
            else:
                print('%d: False' % n)
        else:
            # Checking to see if even
            if (n/2) == 0:
                print('%d: False' % n)
            else:
                print('%d: True'%n)
    print('Finished aanalysing data!')




def main():
    run_my_analysis('True', '/Users/tevesjb/repositories/code-review-practice-1')
if __name__ == '__main__':
    main()
