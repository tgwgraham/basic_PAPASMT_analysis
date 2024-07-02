# basic_PAPASMT_analysis
Code for performing SASPT analysis on automated PAPA-SMT experiments

This was designed for use with the automated SMT acquisition pipeline developed in the Tjian-Darzacq group, but it could easily be adapted for other data formats.

# Requirements
Requires the State Array Single-Particle Tracking (SASPT) analysis package, available here: https://saspt.readthedocs.io/en/latest/

# Instructions
1.	Copy these files to an analysis folder within the data directory:
- autosmt_utils.py
- callCellPicker.m
- cellpicker.m
- autosmt_papa_saspt.ipynb
- analysis_settings.toml
- sort_picked.py
2. Navigate to this folder in MATLAB, open the script callCellPicker.m, set the options at the top, and run this script to pick cells. See further directions at the bottom of the script.
3. In a terminal, run sort_picked.py to sort trajectories from selected cells. This requires autosmt_utils.py. Be sure that the variables in the script that specify the output .mat file from MATLAB and the input/output directories are set appropriately.
4. Modify the analysis settings in analysis_settings.toml to correspond to your experiment. In cases where you want to pool data from multiple days, it is possible to have multiple conditions with multiple experimental replicates for each condition.
5. Run the Juptyer notebook autosmt_papa_saspt.ipynb to run SASPT on the sorted trajectories from selected cells. Alternatively, run the script run_papa_saspt.py from the command line. At the top of the script, you can set the number of CPUs to use and the random seed to use for subsampling.

To analyze green-to-violet ratios (a normalized measure of PAPA efficiency), use the notebook plot_GV_ratio.ipynb. It expects that you will already have done cell picking and sorting with sort_picked.py, and that you will have an analysis_settings.toml file containing (at least) the PAPA cycle parameters.

# Filtering localization density
The script run_saspt_max_loc_density.py can be used to select only movies in which the density of localizations is below some threshold value. It expects that the target folder will have a CSV file locsperframe/gv_by_cell.csv, with columns containing DR localization counts (vcounts) and ROI areas (area). This CSV file is the output of notebook plot_GV_ratio.ipynb.

# References
For more information about PAPA and automated fast SMT, please see the following publications:

Detecting molecular interactions in live-cell single-molecule imaging with proximity-assisted photoactivation (PAPA).
Graham TGW, Ferrie JJ, Dailey GM, Tjian R, Darzacq X.
Elife. 2022 Aug 17;11:e76870. doi: 10.7554/eLife.76870.
PMID: 35976226 [https://elifesciences.org/articles/76870]

Single-molecule live imaging of subunit interactions and exchange within cellular regulatory complexes
Thomas G.W. Graham, Claire Dugast-Darzacq, Gina M. Dailey, Britney Weng, Xavier Darzacq, Robert Tjian
bioRxiv 2024.06.25.600644; doi: https://doi.org/10.1101/2024.06.25.600644
[https://doi.org/10.1101/2024.06.25.600644]

Surprising Features of Nuclear Receptor Interaction Networks Revealed by Live Cell Single Molecule Imaging.
Dahal L, Graham TG, Dailey GM, Heckert A, Tjian R, Darzacq X.
bioRxiv. 2023 Oct 2:2023.09.16.558083. doi: 10.1101/2023.09.16.558083. Preprint.
PMID: 37745337 [https://www.biorxiv.org/content/10.1101/2023.09.16.558083v2]

Automated live-cell single-molecule tracking in enteroid monolayers reveals transcription factor dynamics probing lineage-determining function
Nike Walther, Sathvik Anantakrishnan, Gina M. Dailey, Robert Tjian, Xavier Darzacq
bioRxiv 2024.04.04.587889; doi: https://doi.org/10.1101/2024.04.04.587889
[https://doi.org/10.1101/2024.04.04.587889]



# Contact info
If you are interested in performing and analyzing PAPA-SMT experiments, please feel free to contact me! You can email me at my GitHub user name at gmail.
