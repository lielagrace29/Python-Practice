######################################################
# Name:       Liela Pressley
# Class:      CIS-1400
# Assignment: Practice_06
# File:       Practice_06.py
# Purpose:   Calcualte Kinetic Energy using Functions
#######################################################


# Main procedure
def main():

    # input mass in kilograms:
    mass = float(input('Enter the mass of the object in kilograms: '))

    print()  # Blank line

    #input velocity in meters:

    velocity = float(input('Enter the velocity o fthe object in meters per second: '))

    print() #blank line

    # Display results
    kinetic_energy = calculate_kinetic_energy(mass, velocity)
    print('Joules: ', kinetic_energy)


# Finds initials inside of a name
def calculate_kinetic_energy(calc_mass, calc_velocity):
    velocity_sqrd = calc_velocity*calc_velocity #squared the velocity

    Total_KE = 0.5 * calc_mass * velocity_sqrd #calculate kinetic energy

    return Total_KE  # Return total kinetic energy


# Call the main procedure
main()
