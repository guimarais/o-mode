import numpy as np

def sim_perf(dens0 = 6e19, Rmid=1.65, R0=2.22, Rant=2.32, m=13, n=4, npts=100):
    """Makes a LFS density profile
    
    Parameters
    -----------
    dens0 : Density at Rmid point
    Rmid : Mid-point of the plasma column (core):
    R0 : Last plasma point
    Rant : Radial location of antennas
    m : Geometric parameter for density profile
    n :  Geometric parameter for density profile
    npts : Number of points for the profile (going from Rmid to Rant)
    
    Returns
    -----------
    r : Profile radius
    dens : Profile density
    """
    #Declare the radii
    r = np.linspace(Rmid, Rant, npts)
    #Declare the density
    dens = np.zeros_like(r)
    #n[rmask] = dens0*( 1.0 - ((r[rmask]-Rmid)/(R0-Rmid))**m)**n
    dens = dens0*( 1.0 - ((r-Rmid)/(R0-Rmid))**m)**n
    rmask = r>R0
    dens[rmask] = 0.0
    return r, dens