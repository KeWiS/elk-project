class VoltageDivider:
    def voltage_divider(self):
        print("voltage divider")
        Uin = int(input("Please provide input voltage: "))
        Uout = int(input("Please provide output voltage: "))
        resistor_value = int(input("Please provide resistance: "))
        resistor_type = input("Choose resistor to calculate: R1 or R2? ")
        self.__calculate_resistance(Uin, Uout, resistor_value, resistor_type)

    def __calculate_resistance(self, Uin, Uout, R, Rtype):
        match Rtype:
            case "R1":
                R_resulting = (Uin * R)/Uout - R
            case "R2":
                R_resulting = (Uout * R)/((Uout - Uin)*(-1))
            case _:
                print("Invalid data")
        print("The resistance of " + Rtype + " resistor is " + str(R_resulting) + " ohm(s).")