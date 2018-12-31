# エキスパートPythonプログラミング 改訂2版 13章
# マルチプロセスその２
# multiprocessing の使い方

from multiprocessing import Process
import os


def work(identifier):
    print(f'私はプロセス {identifier}, pid: {os.getpid()} です')


def main():
    processes = [Process(target=work, args=(number,)) for number in range(5)]

    for p in processes:
        p.start()

    while processes:
        processes.pop().join()


if __name__ == "__main__":
    main()
