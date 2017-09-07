from scipy.constants import codata
import numpy as np

def n2f(n):
    """Converts a density in m^-3 to the corresponding O-mode frequency in Hz
    
    Parameters
    -----------
    n : The input density in m^-3
    
    Returns
    -----------
    The corresponding frequency in Hertz
    
    """
    k = 4.0 * np.pi**2 * codata.value('electron mass') * codata.value('electric constant') / codata.value('elementary charge')**2
    return np.sqrt(n/k)


def f2n(f):
    """Converts a frequency in Hertz to the corresponding O-mode density in m^-3
    
    Parameters
    -----------
    f : The input frequency in Hertz
    
    Returns
    -----------
    The corresponding density in m^-3
    
    """
    k = 4.0 * np.pi**2 * codata.value('electron mass') * codata.value('electric constant') / codata.value('elementary charge')**2
    return k * f**2