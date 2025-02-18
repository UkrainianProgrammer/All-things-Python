import multiprocessing
import time

NUMBER_OF_PROCESSES = 5
NUMBER_OF_ITERATIONS = 5
N = 100000000

def sum_all_numbers(n):
    '''
    Sums all numbers from 0 to n

    n: the upper bound of the number to be summed
    return: the sum all numbers from 0 to n
    '''

    total_sum = sum(range(n + 1))
    print('Sum: ' + str(total_sum))

def without_multiprocessing():
    print('Starting without multiprocessing.')
    for i in range(NUMBER_OF_ITERATIONS):
        sum_all_numbers(N)

def with_multiprocessing():
    print('Starting with multiprocessing.')
    jobs = []

    for i in range(NUMBER_OF_PROCESSES):
        p = multiprocessing.Process(target=sum_all_numbers, args=(N,))
        jobs.append(p)
    
    for j in jobs:
        j.start()
    
    for j in jobs:
        j.join()

def main():
    print('Summing all numbers between 0 and ' + str(N) + '\n')

    start_time = time.time()
    without_multiprocessing()
    print('----Without multiprocessing took %s seconds----\n' % (time.time() - start_time))

    start_time = time.time()
    with_multiprocessing()
    print('----With multiprocessing took %s seconds----\n' % (time.time() - start_time))

if __name__ == '__main__':
    main()