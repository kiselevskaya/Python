

from game_logic import *

logs = []


def simulate(muppet):
    while True:
        time.sleep(2)
        muppet.animate()
        logs.append(['Time since start: {}. Muppet position: {}'.format(time.time()-start_time, muppet)])
        print(logs[-1])


def main():
    simulate(muppet)


if __name__ == '__main__':
    main()
