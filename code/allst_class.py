import shutil
import os
import time
import subprocess
import math as m
import numpy as np
from allst_func2 import *

class cl_stmod(object):

    def __init__(self, mass, metal, age):
        self.mass  = mass
        self.metal = metal
        self.age   = age
        self.modelname = ('M%.3f-Z%03d-A%04.0f') % (mass, int(self.metal*10000.), age)
        self.eosopal = ('eos_opal_%03d.bin') % (int(round(self.metal,3)*10000.))
        self.Y0 = 0.24 + 3*self.metal
        self.X0 = 1. - self.metal - self.Y0
        self.path2exe = '' # the executables dmp2k.out and SepCalc must be here 
        self.localdir = '/local/tmp/jordi/allst/'
        self.path2out = self.localdir + 'outputs/'
        self.path2inp = self.localdir + 'inputs/'
        self.path2def = '/home/jordi/allst/default_input_files/'
#        self.file_don = self.path2exe + self.modelname + '.don' # not used, it always read in self.path2exe + 'sun.don'
        self.file_red = self.path2inp + self.modelname + '.redistrb.in'
        self.file_adi = self.path2inp + self.modelname + '.adipls.c.in'
        self.file_osc = self.path2out + self.modelname + '.osc'
        self.file_gsm = self.path2out + self.modelname + '.gsm'
        self.file_fre = self.path2out + self.modelname + '.freqs'
	self.file_tot = 'Summary.dat'
	self.file_run = self.path2out + self.modelname + '.run'
	self.OK = True
	self.Chi2 = -np.inf
        self.Like = -np.inf

	if not os.path.exists(self.path2out):
            os.makedirs(self.path2out)
	if not os.path.exists(self.path2inp):
            os.makedirs(self.path2inp)

    def F_run_st_evolution(self):

        # Runs dmp2k code:
        print '--- Running dmp2k.out...'

        with open(self.file_run, 'w') as f:
            f.write('this model is running...\n mass  metal  X0  Y0  age\n %.3e  %.3e  %.3e  %.3e  %.3e \n' % 
                    (self.mass, self.metal, self.X0, self.Y0, self.age))

        subprocess.Popen("./dmp2k.out", stdin=subprocess.PIPE, shell=True).communicate(
                    input='2\n'+'n\n'+self.path2def+'m010.zams\n'+self.modelname+'\n'+
                    self.path2exe+'\n'+str(self.mass)+'\n'+str(self.X0)+'\n'+str(self.Y0)+'\n'+
                    self.eosopal+'\n'+str(self.age)+'\n')[0]
        print '*** DMP run ended on '+time.strftime("%d %b %Y %H:%M:%S",time.localtime())+'.'

	os.remove(self.file_run)

	# Checks if the code ran without errors:
	if not os.path.isfile(self.path2out + self.modelname + '.ok'):
            self.OK = False


    def F_run_oscillations(self):
        # Prepares input file *.redistrb.in:
        shutil.copyfile(self.path2def + 'redistrb.in', self.file_red)
        F_replace_infile(self.file_red, 'MODELNAME', self.path2out + self.modelname)
        
        # Converts .osc.for ascii file to binary .osc:
        subprocess.call("form-amdl.d 2 " + self.file_osc + ".for " + self.file_osc, shell=True)
        print 'conversion .osc done'
        
        # Redistributes the mesh (creates p4 file)
        subprocess.call("redistrb.c.d " + self.file_red, shell=True)
        print 'redistribution done'
    
        # Prepares adipls.c.in file:
        shutil.copyfile(self.path2def + 'adipls.c.in', self.file_adi)
        F_replace_infile(self.file_adi, 'MODELNAME', self.path2out + self.modelname)
        F_replace_infile(self.file_adi, 'DEFINPUTSDIR', self.path2def[:-1])
        
        # Calculates the oscillation frequencies:
        subprocess.call("adipls.c.d " + self.file_adi, shell=True)
        
        # Checks if the code ran without errors:
	if not is_non_zero_file(self.file_gsm):
#        if not os.path.isfile(self.file_gsm):
            self.OK = False
            return

        # Converts .gsm binary to ascii .gsm.for, saves output to .freqs file and cleans file:
        f = open(self.file_fre, 'w') ; ftemp = open(self.file_fre + ".tmp", 'w')
        subprocess.call("form-agsm.d 1 " + self.file_gsm + " " + self.file_gsm + ".for", shell=True, stdout=f)
        subprocess.call("grep -A1000 ' 1     0' " + self.file_fre, shell=True, stdout=ftemp)
        f.close() ; ftemp.close()
        shutil.move(self.file_fre + ".tmp", self.file_fre)

	# Cleans useless files:
        for extension in ['.gsm', '.gsm.for', '.osc', '.p4']:
            try:
                os.remove(self.path2out + self.modelname + extension)
            except OSError:
                pass
        

    def F_calc_seismicparameters(self):
        # Prepares input.dat file:
        shutil.copyfile(self.path2def + 'input.dat', self.path2exe + 'input.dat')
        F_replace_infile(self.path2exe + 'input.dat', 'MODELNAME', self.path2out + self.modelname)
        F_replace_infile(self.path2exe + 'input.dat', 'STARNAME', self.path2def + 'Dushera')
        
        # Runs fortan code SepCalc:
        subprocess.call("./SepCalc", shell=True)
        
        # Reads relevant results:
        with open(self.path2out + self.modelname + '.Chi2') as f:
            self.Chi2, self.Factor = [float(x) for x in f.readline().split()]

    def F_calc_Likelihood(self):
#        self.Like = np.log( self.Factor * m.exp(-self.Chi2/2) )
#	self.Like = -self.Chi2
	self.Like = m.log(self.Factor) - (self.Chi2/2)
	if m.isnan(self.Like):
            self.Like = -np.inf

    def F_printresults(self, Errflag=''):
        with open(self.file_tot, 'a') as f:
            f.write('%.3e  %.3e  %.3e  %.3e  %.3e  %s \n' % (self.mass, self.metal, self.age, self.Chi2, self.Like, Errflag))
