#!/usr/bin/python
import sys
from scipy.integrate import quad
from allst_func import *

def main():
#    mass = 1.1021723        # Ms [0.6 - 1.9]
#    metal = 0.0125577777   # [0.0095 - 0.0334]
#    age = 10.384296332            # Myr [0 - ageUniv]
    cube = [ 0.5, 0.2, 0.1 ]
    ndim = len(cube)
    nparams = len(cube)

    # transforms normlized cube to real units inputs with prior distribution:
    F_allpriors( cube, ndim, nparams ) 

#    cube = [ 1.002e+00, 1.284e-02, 1.398e+01 ]
    cube = [ 1.003e+00, 2.407e-02, 3.330e+01 ]
    # calculates likelyhood:
    print F_calc_Likelihood4stmd( cube, ndim, nparams )


if __name__ == "__main__":
    main()
