# basic_PAPASMT_analysis
Code for performing SASPT analysis on automated PAPA-SMT experiments

# Requirements
Requires the State Array Single-Particle Tracking (SASPT) analysis package, available here: https://saspt.readthedocs.io/en/latest/

# Instructions
*	Copy these files to an analysis folder within the data directory:
- autosmt_utils.py
- callCellPicker.m
- cellpicker.m
- autosmt_papa_saspt.ipynb
- analysis_settings.toml
- sort_picked.py
* In MATLAB, set the options in callCellPicker.m, and run this script to pick cells.
* In a terminal, run sort_picked.py to sort trajectories from selected cells. This requires autosmt_utils.py. Be sure that the variables in the script that specify the output .mat file from MATLAB and the input/output directories are set appropriately.
* Modify the analysis settings in analysis_settings.toml to correspond to your experiment. In cases where you want to pool data from multiple days, it is possible to have multiple conditions with multiple experimental replicates for each condition.
* Run the Juptyer notebook autosmt_papa_saspt.ipynb to run SASPT on the sorted trajectories from selected cells. Alternatively, run the script run_saspt.py from the command line.

To analyze green-to-violet ratios (a normalized measure of PAPA efficiency), use the notebook plot_GV_ratio.ipynb. It expects that you will already have done cell picking and sorting with sort_picked.py, and that you will have an analysis_settings.toml file containing (at least) the PAPA cycle parameters.

# Contact info
If you are interested in performing and analyzing PAPA-SMT experiments, please feel free to contact me! Email me at my GitHub user name at gmail.
