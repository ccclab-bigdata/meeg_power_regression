import os.path as op
import glob

path_outputs = op.join('./outputs')  # path to outputs
path_dir = '/storage/local/camcan'  # path to input camcan data

path_data = op.join(path_dir, 'data')
path_maxfilter_info = op.join(path_dir, 'maxfilter')
files_raw = sorted(glob.glob(op.join(path_data,
                   'CC??????/rest/rest_raw.fif')))
camcan_path = '/storage/store/data/camcan'
camcan_meg_path = op.join(camcan_path,
                          'camcan47/cc700/meg/pipeline/release004/')
camcan_meg_raw_path = op.join(camcan_meg_path,
                              'data/aamod_meg_get_fif_00001')
mne_camcan_freesurfer_path = (
    '/storage/store/data/camcan-mne/freesurfer')
derivative_path = ('/storage/inria/agramfor/camcan_derivatives')
