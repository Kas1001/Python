"""Interview Exercise: Code to calculate binding energy between objects."""

def binding_energy_calc(distances):
    """Function to calculate the binding energy between objects separated with
        distance, r.
        
        Input parameters:
        distances = list array containing the distance in metres between the objects.
                    
        Output parameters:
        u_r = the binding energy of the two objects, measured in joules.
    """
    
    """Setting two constants, Sigma (metres) and Epsilon (joules)."""
    SIGMA = 3.41e-10
    EPSILON = 1.65e-21

    u_r = 0
    for distance in distances:
        u_r += 4 * EPSILON * ( (SIGMA / distance) ** 12 - (SIGMA / distance) ** 6 )

    return u_r

"""Testing the code with the known case, r = 6.82e-10 m should give u = -1.0e-22 J."""
distances_array = [6.82e-10]
binding_energy = binding_energy_calc(distances_array)
print(f"The binding energy of the test case is {binding_energy:.1e} J.\n")

"""Running the code with the three objects defined in the interview exercise, 
    distances: 5.5e-10, 1.0e-10, 3.41e-10 m."""
distances_array = [5.5e-10, 1.0e-10, 3.41e-10]
binding_energy = binding_energy_calc(distances_array)
print(f"The total binding energy of the three objects is {binding_energy:.1e} J.")