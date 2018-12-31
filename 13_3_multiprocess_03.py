# エキスパートPythonプログラミング 改訂2版 13章
# マルチプロセスその３
# multiprocessing で Pipe を使ったプロセス間通信(Queue もあるが略)

from multiprocessing import Process, Pipe


class CustomClass:
    pass


def work(connection):
    while True:
        item = connection.recv()
        if item:
            print(f'子： 受信： {item}')
        return


def main():
    # 双方向チャネル作成
    parent_conn, child_conn = Pipe()

    child = Process(target=work, args=(child_conn,))

    items = (42, 'some string', {'one': 1}, CustomClass(), None)
    for item in items:
        print(f'PRINT: send: {item}')
        # parent_conn で send して、child_conn で recv する
        parent_conn.send(item)

    child.start()

    child.join()


if __name__ == "__main__":
    main()
