import math
import os

import matplotlib.pyplot as plot


class BridgeRectifier:
    TARGET_RIPPLE_VALUE = 1

    def simulate_bridge(self):
        # Showing scheme image
        self.__show_image()

        # Asking user for input
        self.__load_data_from_user()

        # Calculating capacitor value
        self.capacitor_value = self.__calculate_capacitor_value()
        print("Value of the capacitor (C1) is: " + str(self.capacitor_value))

        # Create Transient Analysis chart
        self.__show_transient_analysis_chart()

    @staticmethod
    def __show_image():
        path = os.getcwd()
        os.startfile(path + "/bridgerectifier/schema.png")

    def __load_data_from_user(self):
        print("\n\nPlease provide following data:")
        self.input_voltage = float(input("Input voltage (V): "))
        self.frequency = float(input("Frequency (Hz): "))
        self.resistance = float(input("Resistance (Ohm): "))

    def __calculate_capacitor_value(self):
        return (self.input_voltage) / (self.TARGET_RIPPLE_VALUE * 2 * self.frequency * self.resistance)

    def __show_transient_analysis_chart(self):
        x_axis = []
        y_ac_axis = []
        y_dc_axis = []
        # Creating chart for AC
        self.lowest_difference_for_graphs = self.input_voltage
        for i in range(0, 100000):
            time = self.__calculate_x_axis_for_ac(i)
            x_axis.insert(i, time)
            voltage_ac = self.__calculate_y_axis_for_ac(time)
            y_ac_axis.insert(i, voltage_ac)

            self.__calculate_y_axis_for_ac_dc_comparision(time, voltage_ac)

        # Creating chart for output DC
        for i in range(0, 100000):
            time = self.__calculate_x_axis_for_ac(i)

            voltage_dc = self.__calculate_y_axis_for_dc(time, self.module_theta_for_lowest_difference)
            if (voltage_dc > self.input_voltage):
                voltage_dc = self.input_voltage
            y_dc_axis.insert(i, voltage_dc)

        self.__set_chart_properties(x_axis, y_ac_axis, y_dc_axis)

        plot.show()

    def __calculate_x_axis_for_ac(self, iteration):
        return iteration * (1 / self.frequency / 25000)

    def __calculate_y_axis_for_ac(self, time):
        return self.input_voltage / 2 * (
            math.cos(2 * self.frequency * math.pi * time - math.pi)) + self.input_voltage / 2

    def __calculate_y_axis_for_ac_dc_comparision(self, time, voltage_ac):
        theta = 2 * self.frequency * math.pi * time

        if (theta < math.pi):
            modulo_theta = math.fmod(theta, math.pi)

            voltage_dc = self.__calculate_y_axi_value(modulo_theta)
            difference = abs(voltage_dc - voltage_ac)

            if (difference < self.lowest_difference_for_graphs):
                self.module_theta_for_lowest_difference = modulo_theta
                self.lowest_difference_for_graphs = difference

    def __calculate_y_axis_for_dc(self, time, theta1):
        theta = 2 * self.frequency * math.pi * time
        modulo_theta = math.fmod(theta, math.pi)

        if (theta < math.pi):
            return self.__calculate_y_axis_for_ac(time)
        elif (modulo_theta < theta1):
            return self.__calculate_y_axi_value(modulo_theta)

        return self.__calculate_sin_y_axi_value(time)

    def __calculate_y_axi_value(self, modulo_theta):
        return self.input_voltage * math.exp(
            (math.pi / 2 - modulo_theta) / (
                    2 * self.frequency * math.pi * self.resistance * self.capacitor_value)) - self.TARGET_RIPPLE_VALUE / 2

    def __calculate_sin_y_axi_value(self, time):
        return self.input_voltage / 2 * (
            abs(math.cos(2 * self.frequency * math.pi * time - math.pi))) + self.input_voltage / 2

    @staticmethod
    def __set_chart_properties(x_axis, y_ac_axis, y_dc_axis):
        plot.title("Transient Analysis")
        plot.ylabel("Voltage")
        plot.xlabel("Time")

        plot.plot(x_axis, y_ac_axis, x_axis, y_dc_axis)
        plot.grid(True, which = 'both')
        plot.axhline(color = 'k')
