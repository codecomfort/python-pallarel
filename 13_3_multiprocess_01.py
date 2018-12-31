# エキスパートPythonプログラミング 改訂2版 13章
# マルチプロセスその１
# 生の fork を使う方法
# → コードが入り交じるし、Win では使えないし、プロセス間通信も難しい

import os

pid_list = []


def main():
    pid = os.getpid()
    pid_list.append(pid)
    # 子プロセス側では 0 が返り、親プロセス側では子プロセスの id が返る
    child_pid = os.fork()

    # ここでプロセスが別れ、以降のコードではメモリコンテキストが共有されない
    # → 例えば、子側では pid_list に append しているが、親側ではそれ認識できない

    if child_pid == 0:
        # 子プロセス側で実行されるコード
        c_pid = os.getpid()
        pid_list.append(c_pid)
        print()
        print(f'[子プロセス]: 私は子プロセスです pid: {c_pid}')
        print(f'[子プロセス]: 認識している pid：{pid_list}')
    else:
        # 親プロセス側で実行されるコード
        print()
        print(f'[親プロセス]: 私は親プロセスです pid: {pid}')
        print(f'[親プロセス]: 子プロセスpid：{child_pid}')
        print(f'[親プロセス]: 認識している pid: {pid_list}')


if __name__ == "__main__":
    main()
