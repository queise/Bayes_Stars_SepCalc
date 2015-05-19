import numpy as np
from scipy.integrate import quad
from allst_class import *

def F_calc_Likelihood4stmd(cube, ndim, nparams):
    mass  = cube[0] 
    metal = cube[1]
    age   = cube[2]    

    # Initializes stellar model with given inputs:
    stmod = cl_stmod(mass, metal, age)

    # Prepares and runs DMP2k code for stellar evolution:
    stmod.F_run_st_evolution()
    if not stmod.OK: 
        stmod.F_printresults(Errflag='DMP-Err')
        return -np.inf

    # Prepares and runs ADIPLS code for stellar oscillations:
    stmod.F_run_oscillations()
    if not stmod.OK:
        stmod.F_printresults(Errflag='OSC-Err')
        return -np.inf

    # Prepares and runs SepCalc small code that calculates seismic parameters and Chi2:
    stmod.F_calc_seismicparameters()

    # Calculates likelihood:
    stmod.F_calc_Likelihood()

    # Prints results in summary file:
    stmod.F_printresults()

    return stmod.Like

def F_allpriors(cube, ndim, nparams):
    """ transforms normlized cube:
		cube[0] : mass
		cube[1] : metallicity
		cube[2] : final age
        to real units inputs with prior distribution """
    #cube[0] = 1.0 + (cube[0] + (m.pow((1.6-1.0), 1/2.35) - 1.))**2.35 	# max would be [0.6, 1.6] for m010.zams
    cube[0] = 0.7 + m.pow(cube[0]/1.04585450769,2.35) 	# min + m.pow(cube[0]/((max-min)^(-1/2.35)),2.35)      max would be [0.6, 1.6] for m010.zams
    cube[1] = 0.0005 + cube[1]*(0.0400-0.0005)	     	# min + cube[1]*(max-min)    max range allowed by opa tables would be: [0.0005, 0.0404]
    cube[2] = 0.0 + cube[2]*13800.			# min + cube[2]*(max-min)    max would be [0, 13800.]

# intervals February 2015:
# cube[0]       [0.7, 1.6]
# cube[1]       [0.0005, 0.0400]
# cube[2]       [0.0, 13800.]

# intervals January 2015:
# cube[0]	[1.0, 1.6]
# cube[1]	[0.0095, 0.0334]
# cube[2]	[0.0, 8000.]

def F_imf_with_range(mass):
    if mass <= 0.6 or mass >= 1.9:
        val = 0.
    else:
        val = m.pow(mass,-2.35)
    return val

def F_calc_prior_mass(mass):
    prior = F_imf_with_range(mass) / quad(F_imf_with_range, 0., 3.)[0]
    return prior

def F_calc_prior_age(age):
    if age >= 13800.:
        prior = 0.
    else:
        prior = 1/13800.
    return prior

def F_calc_prior_metal(metal):
    if metal < 0.0095 or metal > 0.0334:
        prior = 0.
    else:
        prior = 1. / (0.0334-0.0095)
    return prior

