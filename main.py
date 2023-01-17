from bridgerectifier.bridge_rectifier import BridgeRectifier
from voltagedivider.voltage_divider import VoltageDivider


def exercise_1():
    voltage_divider = VoltageDivider()
    voltage_divider.voltage_divider()


def jump_to_next_exercise():
    print("Do you want to go to another exercise?\n\"y\" for yes, to exit any other key")
    if (input() != "y"):
        exit()


def exercise_2():
    bridge_rectifier = BridgeRectifier()
    bridge_rectifier.simulate_bridge()


if __name__ == '__main__':
    # exercise_1()
    # jump_to_next_exercise()
    exercise_2()
