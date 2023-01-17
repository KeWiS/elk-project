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
        return (self.input_voltage * self.TARGET_RIPPLE_VALUE) / (2 * self.frequency * self.resistance)

    def __show_transient_analysis_chart(self):
        # V cos(2 pi f t)
        x_axis = []
        y_ac_axis = []
        y_dc_axis = []
        for i in range(0, 400):
            # Creating chart for AC
            time = self.__calculate_x_axis_for_ac(i)
            x_axis.insert(i, time)
            voltage_ac = self.__calculate_y_axis_for_ac(time)
            y_ac_axis.insert(i, voltage_ac)

            # Creating chart for output DC
            voltage_dc = self.__calculate_y_axis_for_dc(time, voltage_ac)
            y_dc_axis.insert(i, voltage_dc)

        self.__set_chart_properties(x_axis, y_ac_axis, y_dc_axis)

        plot.show()

    def __calculate_x_axis_for_ac(self, iteration):
        return iteration * (1 / self.frequency / 100)

    def __calculate_y_axis_for_ac(self, time):
        return self.input_voltage / 2 * (
            math.cos(2 * self.frequency * math.pi * time - math.pi)) + self.input_voltage / 2

    def __calculate_y_axis_for_dc(self, time, voltage_ac):
        theta = 2 * self.frequency * math.pi * time
        conditional_theta = math.fmod(theta, 2 * math.pi)

        if (0 <= conditional_theta < math.pi / 2):
            return self.__calculate_middle_y_axi_value(theta)

        return self.__calculate_extreme_y_axi_value(theta)
        # if ((0 <= conditional_theta < self.input_voltage - self.TARGET_RIPPLE_VALUE) or (
        #         math.pi / 2 <= conditional_theta < math.pi * 2)):
        #     return self.__calculate_extreme_y_axi_value(theta)
        # elif (self.input_voltage - self.TARGET_RIPPLE_VALUE <= conditional_theta < math.pi / 2):
        #     return self.__calculate_middle_y_axi_value(theta)

    def __calculate_extreme_y_axi_value(self, theta):
        return self.input_voltage * math.exp(
            ((math.pi / 2) - theta) / (2 * self.frequency * math.pi * self.resistance * self.capacitor_value))

    def __calculate_middle_y_axi_value(self, theta):
        return self.input_voltage * math.sin(theta)

    @staticmethod
    def __set_chart_properties(x_axis, y_ac_axis, y_dc_axis):
        plot.title("Transient Analysis")
        plot.ylabel("Voltage")
        plot.xlabel("Time")

        # plot.plot(x_axis, y_dc_axis)
        plot.plot(x_axis, y_ac_axis, x_axis, y_dc_axis)
        plot.grid(True, which = 'both')
        plot.axhline(color = 'k')
