"""
Dendritic Calcium Module
Handles calcium dynamics in the dendrite
"""

import numpy as np
from Params import params


def update_ca_dend(ca_dend_current, ca_release, dt, noise):
    """
    Update dendritic calcium concentration
    
    Args:
        ca_dend_current: Current dendritic Ca concentration
        ca_release: Ca release from stores
        dt: Time step
        noise: Noise variable
        
    Returns:
        dca_dend: Change in dendritic Ca concentration
    """
    dca_dend = (
        -ca_dend_current / params["tau_ca_dend"] + ca_release
    ) * dt
    
    dca_dend += noise * np.sqrt(dt)
    
    return dca_dend


def initialize_ca_dend():
    """
    Initialize dendritic calcium concentration
    
    This function currently initialises ca_dend to 0.
    """
    return 0.0
