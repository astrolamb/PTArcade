from enterprise.signals.parameter import function
import enterprise.signals.parameter as parameter
import scipy.constants as scon
import numpy as np
import src.models_utils as aux

name = 'uldm_earth_mod' # name of the model

mod_sel = True # set to True if you want to compare the model to the SMBHB signal

smbhb = True # set to True if you want to overlay the new-physics signal to the SMBHB signal
corr = True # set to True if you want to include spatial correlations in the analysis 

parameters ={
    "log10_A_dm" : parameter.Uniform(-9, -4)('log10_A_dm'),
    "log10_f_dm" : parameter.Uniform(-9, -7)('log10_mass_dm'),
    "gamma" : parameter.Uniform(0, 2 * np.pi)('gamma_e')
}

group = ['log10_A_dm', 'log10_mass_dm']

@function
def signal(toas, log10_A_dm, log10_f_dm, gamma):
    """
    Function that calculates the pulsar term signal generated by
    ultralight dark matter 
    :param toas: Time-of-arrival measurements [s]
    :param log10_A: log10 of GW strain
    :param log10_f: log10 of GW frequency
    :param phase_p: The Pulsar-term phase of the GW
    :return: the waveform as induced timing residuals (seconds)
    """
    
    A = 10**log10_A_dm
    f= 10**log10_f_dm

    # return timing residual in seconds
    return A *  np.sin(2 * np.pi * f * toas + gamma)
