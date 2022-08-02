import os
import numpy as np
import enterprise.signals.parameter as parameter
import src.models_utils as aux

name = 'string_stable' # name of the model 

mod_sel = True # set to True if you want to compare the model to the SMBHB signal

smbhb = True # set to True if you want to overlay the new-physics signal to the SMBHB signal
corr = False # set to True if you want to include spatial correlations in the analysis 

parameters = {
    'log10_mu' : parameter.Uniform(-14, -3)('log10_mu'),
    }

group = []   

cwd = os.getcwd()
log_spectrum = aux.spec_importer(cwd +'/inputs/models/models_data/stable.dat')

@aux.omega2cross
def spectrum(f, log10_mu, log10_k):
    return 10**log_spectrum(np.log10(f), log10_mu=log10_mu, log10_k=log10_k)