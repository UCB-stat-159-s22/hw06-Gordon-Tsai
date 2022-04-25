 
import numpy as np
import ligotools.readligo as rl
import ligotools.utils as utils
from scipy.interpolate import interp1d
import matplotlib.mlab as mlab
from os.path import exists
from os import remove

def test_whiten():
	strain_H1 = np.array([1,2,3,4,5,6,6,3,435,436,25])
	time = np.array([1,2,3,3,5,6,6,3,4,6,5,234,3,1,2,2,2,3,5,4,1,2,3,1,2,3])
	dt = 15
	Pxx_H1, freqs = mlab.psd(strain_H1, Fs = 56, NFFT = 134)
	psd_H1 = interp1d(freqs, Pxx_H1)
	strain_H1_whiten = utils.whiten(strain_H1,psd_H1,dt)
	assert sum(strain_H1_whiten) == 7346.7692169625325

def test_write_wavfile():
	data = np.array([0,1,2,3,4,5,5,6,1,23,31,4,2,141,5,5,7])
	fs = 26
	utils.write_wavfile("audio/tempo.wav", fs, data)
	assert exists("audio/tempo.wav")
	remove("audio/tempo.wav")

def test_reqshift():
	data = np.linspace(0,1000,100)
	assert sum(utils.reqshift(data,fshift=204,sample_rate=2048))== -2.2737367544323206e-13

def test_plot_plot_ASD():
	template_fft = np.array([1,2,3,4,5,6])
	datafreq = np.array([1,0,0,4,1,2,3])
	d_eff = 157
	freqs = np.array([1,2,3,4,5,6])
	data_psd = np.array([2,3,1,5,6,7])
	pcolor = 'g'
	det = 'L1'
	eventname = 'GW150914'
	plottype = 'png' 
	fs = 4096
	output = utils.plot_ASD(template_fft,datafreq, d_eff, freqs, data_psd, pcolor, det, fs, eventname, plottype, False)
	assert output[2] == 157