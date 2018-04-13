import matplotlib.pyplot as plt
import numpy as np

def simple_process():
    cnt = 2
    primes = []
    x = []
    y = []

    while True:
        flag = True
        for i in range(2, cnt):
            if cnt % i == 0:
                flag = False
                break
        if flag is True:
            primes.append(cnt)
        x.append(cnt)
        y.append(len(primes))
        cnt += 1
        plt.plot(x, y)
        plt.title("Prime Steps")
        plt.xlabel("number")
        plt.ylabel("number of primes")
        plt.grid()
        plt.pause(1e-9)
        plt.clf()

def rapid_process():
    cnt = 3
    primes = np.array([2])
    x = np.array([])
    y = np.array([])
    while True:
        flag = True
        for i in range(3, int(np.sqrt(cnt))+2, 2):
            if cnt % i == 0:
                flag = False
                break
        if flag is True:
            primes = np.append(primes, cnt)
        x = np.append(x, cnt)
        y = np.append(y, primes.size)
        prime_theorem = x/np.log(x)
        cnt += 2
        plt.plot(x, y, color='g', label=str(primes[-1]), drawstyle='steps')
        plt.plot(x, prime_theorem, color='k', label='prime theorem', ls='--')
        plt.title("Prime Steps")
        plt.xlabel("number")
        plt.ylabel("number of primes")
        plt.legend(loc='upper left')
        plt.grid()
        plt.pause(1e-15)
        plt.clf()

#simple_process()
rapid_process()





