import matplotlib.pyplot as plt

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

simple_process()
