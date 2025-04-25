"""
Background:
    Write a program that requires an argument for the name of a text file containing
    multiple sets of commands as an input, and for each set of commands writes to standard output
    both the path that the elevator will take and the total distance in floors that
    the elevator must travel. In addition, your program must accept an argument to specify
    which mode the elevator will operate in throughout the application lifecycle.
    The mode argument should follow the filename argument

Details:
    The Elevator Problem is instanciated by passing Strategy mode, then reads the line commands
    from feed data  and to create a list of Command objects.
    For each path creation is used a strategy mode logic
    The prototype demo of Elevator build and then show by printing the path and distance

Environment setup:
    Python 2
    conda install or pip install - needed packages
"""

import numpy as np
from abc import ABCMeta, abstractmethod
from itertools import groupby, chain
from io import BytesIO
from os import path
from operator import itemgetter
from sortedcontainers import SortedSet
from tempfile import NamedTemporaryFile


class StrategyModeBase:
    """ This abstract class provides skeletal implementation for mode strategies"""
    __metaclass__ = ABCMeta

    def __new__(cls, *args, **kwargs):
        return super(StrategyModeBase, cls).__new__(cls, *args, **kwargs)

    def __init__(self, *args, **kwargs):
        super(StrategyModeBase, self).__init__(*args, **kwargs)

    @abstractmethod
    def build_strategy_mode(self, command):
        return NotImplemented

    @staticmethod
    def show_strategy_mod(floorpath):
        route = " ".join(map(str, floorpath))
        distance = np.sum(np.abs(np.diff(floorpath)))
        return "%s (%i)" % (route, ------------------------------------------------------------------ distance)


class StrategyModeA(StrategyModeBase):
    """
    An instance of this class is used to create a path collection. Once the system receives commands tells
    the elevator to travel according the path and sums the differences between floors to obtain total distance
    """

    def __init__(self, *args, **kwargs):
        super(StrategyModeA, self).__init__(*args, **kwargs)

    def build_strategy_mode(self, cmdobj):
        floorpath = [cmdobj.initialfloor]
        floorpath.extend(np.ravel(cmdobj.paths))
        return StrategyModeA.show_strategy_mod(floorpath)


class StrategyModeB(StrategyModeBase):
    """
    This class is used to create paths list which system accept and tells the elevator which direction to travel (up or down)
    if it is in the same direction we sort  the floors depending on direction also we calculate and sum
    the differences between floors to obtain total distance
    """

    def __init__(self, *args, **kwargs):
        super(StrategyModeB, self).__init__(*args, **kwargs)

    def build_strategy_mode(self, cmdobj):
        floors = [[cmdobj.initialfloor, cmdobj.paths[0][0]]]
        floors.extend(cmdobj.paths)
        directions = [np.sign(np.diff(i))[0] for i in floors]
        yy = [(a, b) for a, b in zip(directions, floors)]
        fullroute = []
        for key, items in groupby(yy, itemgetter(0)):
            route = [subitem[1] for subitem in items]
            fullroute.append(list(SortedSet(np.ravel(route), key=lambda i: key * i)))
        flatroute = [i for i in chain.from_iterable(fullroute)]
        floorpath = [x[0] for x in groupby(flatroute)]
        return StrategyModeB.show_strategy_mod(floorpath)


class Command(object):
    """ This class creates the path list which the elevator travels"""

    def __init__(self, strcommand):
        self.strcommand = strcommand
        self.paths = []
        self.initialfloor = 0
        self.__get_command()

    def __get_command(self):
        ini, rest = self.strcommand.split(':')
        self.initialfloor = int(ini)
        self.paths = [map(int, i.split('-')) for i in rest.split(',')]


class ElevatorSystem(object):
    """ This class loads the commands from the feed data and show the output strategy mode"""

    def __init__(self, strategy):
        self.mode = strategy
        self.commands = []

    def load_data(self, file):
        with open(file, mode='r') as fh:
            self.commands = [Command(line) for line in fh.readlines()]

    def show_mode_output(self):
        print("\n".join([self.mode.build_strategy_mode(commandline) for commandline in self.commands]))


def get_input_data():
    """ Load the feed commands in case the input data file is not present"""
    input_data = b"""\
    10:8-1
    9:1-5,1-6,1-5
    2:4-1,4-2,6-8
    3:7-9,3-7,5-8,7-11,11-1
    7:11-6,10-5,6-8,7-4,12-7,8-9
    6:1-8,6-8
    """

    with BytesIO(input_data) as fh:
        with NamedTemporaryFile(delete=False) as tmp_f:
            for line in fh.readlines():
                tmp_f.write(line.strip(' \t'))
    return tmp_f.name


def generate_output(mode, strategy, data):
    """ Generate  the mode output in the console"""
    print("\n")
    print("\n\t\t Mode " + mode + " \t\n")
    print("================================")
    elevator = ElevatorSystem(strategy)
    elevator.load_data(data)
    elevator.show_mode_output()


def run():
    """ Entry point of the elevator system"""
    data = 'input_file.txt' if not path.isfile('input_file.txt') else get_input_data()
    modes = {"A": StrategyModeA(),
             "B": StrategyModeB()}
    [generate_output(mode, strategy, data) for mode, strategy in modes.items()]


if __name__ == '__main__':
    print("================================")
    print("===   BAML Elevator Problem  ===")
    print("================================")
    run()
