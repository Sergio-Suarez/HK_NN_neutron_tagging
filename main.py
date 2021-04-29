
import os
import numpy as np
import math
import sklearn
import sys
import h5py
import keras
from HK_execution import HK_execution

############################################################################################
#
# 
# Use of a Neural Network for Kamiokande related Neutrino event classification.
#
# Sergio Suarez
#
############################################################################################


inputs_folder = '/home/sergio/NAS_Public/datos_Pablo/20210324_ntag_sim_dist_blind/'
outputs_folder = '/home/sergio/NAS_Public/datos_Pablo/20210324_ntag_sim_dist_blind_results/result_'
model = 'default.h5'


HK_execution(inputs_folder, model, output_folder)
