#!/usr/bin/python
from scipy.integrate import quad
from allst_func import *
import pymultinest
import os

""" Requirements:
        - dmp2k version >= Nov14, adipls 2012, SepCalc v2.2.6
        - 4 folders are needed:
            run/     : a copy of the sample directory provided, with:
		       allst_main.py, allst_class.py, allst_func.py, allst_func2.py,
		       SepCalc, dmp2k.out, sun.don
		       and, if running in cluster: condor.sub  openmpiscript
            inputs/  : initially empty, put it in /local if running in cluster
            outputs/ : initially empty, put it in /local if running in cluster
            default_input_files/
                     : m010.zams, adipls.c.in, agsm.l5bi.d.15.p2, redistrb.in,
                       Dushera.freqs, Dushera.mean-Err-r02.r010, Dushera.mean-Err-Ls.ss0,
                       Dushera.sl-Err-r02.r010.Lsr010, input.dat
        - the path of the 3 last folders should be specified in allst_class.py

    TODO:
        - different initial m010.zams for different masses (not necessary for m<2Ms)
        - test whether dmcapture can be used instead of darksusy """

def main():
    run_name = 'NoDM'

    cube = [ 0.9, 0.5, 0.1 ] # initial values not used
    ndim = len(cube)
    nparams = len(cube)

#    os.chdir('/home/jordi/allst/sample')   

    pymultinest.run(F_calc_Likelihood4stmd, F_allpriors, nparams,importance_nested_sampling = False,
	            resume = False, verbose = True, n_live_points=32, outputfiles_basename=run_name+"_",
                    sampling_efficiency=0.02,const_efficiency_mode=True,init_MPI=False)

if __name__ == "__main__":
    main()
