from concurrent.futures import ProcessPoolExecutor
from multiprocessing import Pool, cpu_count
from time import time


def factorize(*numbers):
    output_list = []
    for number in numbers:
        answer_list = []
        for i in range(1, number + 1):
            if number % i == 0:
                answer_list.append(i)
        output_list.append(answer_list)
    return output_list


if __name__ == '__main__':
    timer = time()
    a, b, c, d, e = factorize(128, 255, 99999, 10651060, 983456824)

    assert a == [1, 2, 4, 8, 16, 32, 64, 128]
    assert b == [1, 3, 5, 15, 17, 51, 85, 255]
    assert c == [1, 3, 9, 41, 123, 271, 369, 813, 2439, 11111, 33333, 99999]
    assert d == [1, 2, 4, 5, 7, 10, 14, 20, 28, 35, 70, 140, 76079, 152158, 304316, 380395, 532553, 760790, 1065106,
                 1521580, 2130212, 2662765, 5325530, 10651060]
    assert e == [1, 2, 4, 7, 8, 14, 28, 56, 131, 262, 524, 917, 1048, 1834, 3668, 7336, 134059, 268118, 536236, 938413,
                 1072472, 1876826, 3753652, 7507304, 17561729, 35123458, 70246916, 122932103, 140493832, 245864206,
                 491728412, 983456824]

    print(f'Done by 1 processes: {round(time() - timer, 4)}')

    timer = time()
    with Pool(cpu_count()) as pool:
            pool.map_async(factorize,  [128, 255, 99999, 10651060, 983456824])
    print(f'Done by map async multiprocessing: {round(time() - timer, 4)}')

    timer = time()
    with Pool(cpu_count()) as pool:
            pool.map(factorize,  [128, 255, 99999, 10651060, 983456824])
    print(f'Done by map multiprocessing: {round(time() - timer, 4)}')

    timer = time()
    with ProcessPoolExecutor(cpu_count()) as executor:
        executor.map(factorize, [128, 255, 99999, 10651060, 983456824])
    print(f'Done by executor multiprocessing: {round(time() - timer, 4)}')

