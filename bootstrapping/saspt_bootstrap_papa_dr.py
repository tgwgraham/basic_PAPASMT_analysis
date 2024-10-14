"""
Does state array analysis of  PAPA and DR trajectories from the same bootstrap-resampled cells.

TG 20240427

"""

import os, sys
import numpy as np, pandas as pd
import datetime
from saspt import StateArray, RBME, load_detections
import re

nreps = 100                     # number of bootstrap replicates
filelist = 'filelist.csv'       # csv file containing list of folders in which files are contained. 
                                # It expects each to contain a "PAPA.csv" file and a "DR.csv" file
maxtraj = 30000 

def cell_sampler(index):
    infiles = pd.read_csv(filelist,header=None)
    resampled_df = infiles.apply(lambda x: x.sample(n=len(x),replace=True)).reset_index(drop=True)
   
    # Get the current system time and date
    current_time = datetime.datetime.now()
    # Format the time and date string to include in the output filename
    time_format = current_time.strftime("%Y-%m-%d_%H-%M-%S")  # Example format: 2023-06-15_09-30-15

    # write out list of resampled input files that were used in this analysis
    resampled_df.to_csv(
        f'resampling_output/resampled_input_files/{index}_{time_format}.csv',index=False)

    # analyze DR
    detections = load_detections(*resampled_df[0])
    settings = dict(
        likelihood_type = RBME,
        pixel_size_um = 0.16,
        frame_interval = 0.00748,
        focal_depth = 0.7,
        start_frame = 0,
        progress_bar = True,
        sample_size = maxtraj,
    )
    SA = StateArray.from_detections(detections, **settings)
   
    posterior_occs = SA.posterior_occs
    
    SA.occupations_dataframe.to_csv(f'resampling_output/posterior_occs/DR_{index}_{time_format}.csv', index=False)
    
    # analyze PAPA
    detections = load_detections(*(resampled_df[0].apply(lambda x: re.sub(r'/DR/',r'/PAPA/',x))))
    settings = dict(
        likelihood_type = RBME,
        pixel_size_um = 0.16,
        frame_interval = 0.00748,
        focal_depth = 0.7,
        start_frame = 0,
        progress_bar = True,
        sample_size = maxtraj,
    )
    SA = StateArray.from_detections(detections, **settings)
   
    posterior_occs = SA.posterior_occs
    
    SA.occupations_dataframe.to_csv(f'resampling_output/posterior_occs/PAPA_{index}_{time_format}.csv', index=False)

    
    

if __name__ == '__main__':
    
    os.makedirs('resampling_output',exist_ok=True)
    os.makedirs('resampling_output/posterior_occs',exist_ok=True)
    os.makedirs('resampling_output/resampled_input_files',exist_ok=True)
    
    for j in range(nreps):
        cell_sampler(j)
