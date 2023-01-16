import os
import numpy as np
import matplotlib.pyplot as plot


class BridgeRectifier:
    TARGET_RIPPLE_VALUE = 1

    def simulate_bridge(self):
        # Showing scheme image
        self.__show_image()

        # Asking user for input
        self.__load_data_from_user()

        # Calculating capacitor value
        capacitor_value = self.__calculate_capacitor_value()
        print("Value of the capacitor (C1) is: " + str(capacitor_value))

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
        plot.title("Transient Analysis")
        plot.ylabel("Voltage")
        plot.xlabel("Time")

        x_axis = self.__create_chart_x_axis()
        y_axis = self.__create_chart_y_axis(x_axis)

        plot.plot(x_axis, y_axis)
        plot.grid(True, which = 'both')
        plot.axhline(y = self.input_voltage, color = 'k')
        plot.show()

    def __create_chart_x_axis(self):
        return np.arange(0, self.__calculate_arange_end_value(), self.__calculate_arange_step())

    def __calculate_arange_end_value(self):
        return 1 / self.frequency * 3

    def __calculate_arange_step(self):
        return 1 / self.frequency / 10

    def __create_chart_y_axis(self, x_axis):
        return np.sin(x_axis)
