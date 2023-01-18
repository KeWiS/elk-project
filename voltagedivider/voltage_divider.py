class VoltageDivider:
    def voltage_divider(self):
        print("***   Voltage Divider   ***")
        u_in = int(input("Please provide input voltage: "))
        u_out = float(input("Please provide output voltage: "))
        resistor_value = int(input("Please provide resistance: "))
        resistor_type = input("Choose resistor to calculate: R1 or R2? ")
        self.__calculate_resistance(u_in, u_out, resistor_value, resistor_type)

    def __calculate_resistance(self, u_in, u_out, R, r_type):
        match r_type:
            case "R1":
                r_resulting = (u_in * R) / u_out - R
            case "R2":
                r_resulting = (u_out * R) / ((u_out - u_in) * (-1))
            case _:
                print("Invalid data")

        print("\nThe resistance of " + r_type + " resistor is " + str(r_resulting) + " ohm(s).")
