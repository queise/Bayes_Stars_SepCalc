# Bayes_Stars
Bayesian inference of the posterior probability on stellar mass, age and metallicities [M, t, Z] using [MultiNest](https://ccpforge.cse.rl.ac.uk/gf/project/multinest/).

Please take a look at the following IPython notebook:

### [DataAnalysis_StarDM](DataAnalysis_StarDM.ipynb) ,

it introduces the code and performs pre-calculations, data analysis and visualization of results.

Inside the [code](code/) folder you will find the python scripts to run Multinest using [OpenMPI](http://www.open-mpi.org/) for parallellization and/or [HTCondor](http://research.cs.wisc.edu/htcondor/) queue system to run in a cluster. [allst_main.py](code/allst_main.py) launches Multinest, but to have an overview take a look at the function F_calc_Likelihood4stmd in [allst_func.py](code/allst_func.py).

To calculate the likelihood of a given combination of [M, t, Z] we:

1) run the stellar evolution code CESAM (modified to include the Dark Matter impact), the adiabatic oscillation code ADIPLS and the code to calculate asteroseismic parameters SepCalc. These three codes are written in Fortran and are not provided here, although the executables are needed to run Bayes_Stars.

2) compare the results with observational data (i.e. Dushera.freqs,...). The observational data is needed to run the Bayes_Stars, but it is not provided here.
