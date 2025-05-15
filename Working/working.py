from multiprocessing import Process, Pipe
from time import sleep

class person():

    def __init__(self, name):
        self.name = name

    @property
    def getName(self):
        return self.name


def worker(conn):
    print('Worker - started now sleeping for 1 second')
    sleep(1)

    print('Worker-sending data via Pipe')
    p_obj = person('Plamen')
    conn.send(p_obj)
    print('Worker-closing worker end of connection')
    conn.close()


def main():
    print('Main - Starting, creating the Pipe')
    main_connection, worker_connection = Pipe()

    print('Main - Setting up the process')
    p = Process(target=worker, args=[worker_connection])

    print('Main - Starting the process')
    p.start()

    print('Main - Wait for a response from the child process')
    obj = main_connection.recv()
    print(f'Class name {obj} with attribute {obj.getName}')

    print('Main-closing parent process end of connection')
    main_connection.close()

    print('Main-Done')


if __name__ == '__main__':
    main()
