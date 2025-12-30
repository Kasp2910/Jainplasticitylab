"""
NMDA Pathway Module
Handles NMDA receptor dynamics
"""

import numpy as np
from Params import params


def compute_voltage_attenuation(syn_distances, v_soma):
    """
    Calculates distance based attenuation for each particular synapse
    
    Args:
        syn_distances: synapse distances from soma 
        v_soma: Somatic voltage 
        
    Returns:
        v_spine: spine voltages at each synapse
    """
    attenuation = np.exp(-syn_distances / params["lambda_d"]) * 4
    v_spine = params["v_rest"] + (v_soma - params["v_rest"]) * attenuation
    
    return v_spine


def compute_nmda_voltage_dependence(v_spine):
    """
    Calcutate NMDA activity
    """

    nmda_v = 1.0 / (1.0 + params["mg_block"] * np.exp(-0.062 * v_spine))
    
    return nmda_v


def get_somatic_voltage(post_spike):
    """
    Calculates somatic voltage based on postsynaptic spike
    """
    v_soma = params["v_rest"] + post_spike * (params["v_peak"] - params["v_rest"])
    
    return v_soma