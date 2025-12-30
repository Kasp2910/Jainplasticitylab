"""
PP1 (Phosphatase) Module
Handles possible synaptic tag dynamics through PP1 inhibition by Kinase

Very Early Development model
"""

import numpy as np
from Params import params


def update_pp1(pp1_current, ca_spine, is_active, dt, noise):
    """
    Update PP1 dynamics
    
    Args:
        pp1_current: Current PP1 level 
        ca_spine: Spine calcium concentration 
        is_active: State of synapse(whether it is active or not)
        dt: Time step
        noise: Noise 
    """
    n_syn = len(pp1_current)
    
    # Recovery to baseline (all synapses)
    dpp1 = (params["pp1_baseline"] - pp1_current) / params["tau_pp1"] * dt
    
    # Inhibition by Kinase (active synapses)
    dpp1[is_active] -= params["alpha_pp1"] * ca_spine[is_active] * dt
    
    # Add noise
    dpp1 += noise * np.sqrt(dt)
    
    return dpp1


def initialize_pp1(n_syn):
    """
    Currently the module initialises pp1 levels to the parameter of baseline PP1
    """
    return np.ones(n_syn) * params["pp1_baseline"]