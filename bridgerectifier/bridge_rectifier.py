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
        # V cos(2 pi f t)
        x = []
        y = []
        for i in range(0, 400):
            time = i * (1 / self.frequency / 100)
            x.insert(i, time)
            y.insert(i,
                     self.input_voltage / 2 * (math.cos(2 * self.frequency * math.pi * time - math.pi)) + self.input_voltage / 2)

        print(x)
        print(y)

        plot.title("Transient Analysis")
        plot.ylabel("Voltage")
        plot.xlabel("Time")

        plot.plot(x, y)
        plot.grid(True, which = 'both')
        plot.axhline(color = 'k')
        plot.show()
