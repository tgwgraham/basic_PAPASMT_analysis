from glob import glob

suffix = 'DR'
input_files = []

basefname = '/mnt/g/SPT_analysis/20230613_BSCE11_and_control_PAPA/analysis20230613/sortedTrajectories/BSCE11/exp1/'
input_files.extend(glob(f'{basefname}{suffix}/*.csv'))

basefname = '/mnt/g/SPT_analysis/20230621_BSCE11_and_control_PAPA/run2/analysis20230823/sortedTrajectories/BSCE11/exp1/'
input_files.extend(glob(f'{basefname}{suffix}/*.csv'))

basefname = '/mnt/g/SPT_analysis/20230621_BSCE11_and_control_PAPA/run3/analysis20230823/sortedTrajectories/BSCE11/exp1/'
input_files.extend(glob(f'{basefname}{suffix}/*.csv'))


with open('filelist.csv','w') as fh:
    [fh.write(x + '\n') for x in input_files]