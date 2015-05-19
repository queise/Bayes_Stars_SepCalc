# Bayes_Stars
Bayesian inference of the posterior probability on stellar mass, age and metallicity using [MultiNest](https://ccpforge.cse.rl.ac.uk/gf/project/multinest/).

Look at the IPython notebook here:
http://nbviewer.ipython.org/github/queise/Bayes_Stars/blob/master/DataAnalysis_StarDM.ipynb

Inside the /code folder you will find the python scripts to run Multinest using [OpenMPI](http://www.open-mpi.org/) for parallellization and/or [HTCondor](http://research.cs.wisc.edu/htcondor/) queue system to run in a cluster. [code/allst_main.py] launches Multinest, but to have an overview better take a look at the function F_calc_Likelihood4stmd in [code/allst_func.py].

The Likelihood is calculated running the stellar evolution code CESAM (modified to include the Dark Matter impact), the adiabatic oscillation code ADIPLS and the code to calculate asteroseismic parameters SepCalc. These three codes are written in Fortran and are not provided here, although the executables are needed to run Bayes_Stars.
