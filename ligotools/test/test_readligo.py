import numpy as np
import ligotools.readligo as rl 


def test_read_hdf5():
	assert rl.read_hdf5('data/H-H1_LOSC_4_V2-1126259446-32.hdf5', readstrain=True)[1] == 1126259446

def test_loadfile():
	assert len(rl.loaddata('data/H-H1_LOSC_4_V2-1126259446-32.hdf5','H1')[1]) == 131072

def test_FileList_searchdir():
	assert np.array_equal( rl.FileList().searchdir('data/'), ['data/GW150914_4_template.hdf5','data/H-H1_LOSC_4_V2-1126259446-32.hdf5','data/L-L1_LOSC_4_V2-1126259446-32.hdf5'])

def test_dq_channel_to_seglist():
	c = np.array([ 5, 3, 1, 4, 1, 1, 1, 1, 7, 1, 5, 6, 3, 4, 1, 2, 1, 1, 3, 5, 7, 1, 2, 1, 1, 1, 1, 0, 2, 3, 4, 1])
	assert np.array_equal(rl.dq_channel_to_seglist(c),[slice(0, 110592, None), slice(114688, 131072, None)])

