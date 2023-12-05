import numpy as np
import pandas as pd
import pickle
from matplotlib import pyplot as plt
import autosmt_utils as au

# SETTINGS
nworkers = 1        # number of cores to use
randseed = 1234     # seed for the random number generator

# read in configuration file in the new format
config = au.read_config('analysis_settings.toml')

# sort trajectories after PAPA and DR pulses
au.sort_PAPA_DR(config)

# get locs per frame for each movie
locs_df = au.getLocsByFrameDF(config,isPAPA=True)

# Plot average number of localizations vs. frame index
au.plot_Nlocs_wholemovie(config,locs_df,closefig=True)

# Plot average number of localizations vs. frame index within each cycle
au.plot_Nlocs_bycycle_colors(config,locs_df,byexperiment=True,closefig=True)

# Do state array analysis of each condition
[SA,posterior_occs,condition_names] = au.analyze_PAPA_DR_stateArray(config,nworkers=nworkers,closefig=True)

# Do state array analysis of each condition, subsampling the same number of trajectories for each
[SA_sameN,posterior_occs_sameN,condition_names_sameN] = au.analyze_PAPA_DR_stateArray_sameN(config,nworkers=nworkers,randseed=randseed,ignoreOther=True,closefig=True)

