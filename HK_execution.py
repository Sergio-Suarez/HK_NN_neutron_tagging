
import os
import numpy as np
import math
import sklearn
import sys
import h5py
import keras
from keras.models import Sequential, load_model
from keras.layers import Dense, Dropout, Activation, Flatten, Conv2D, MaxPooling2D
from keras.layers import Convolution2D, MaxPooling2D
from keras.utils import np_utils

def HK_execution(inputs_folder, model, output_folder):

    for k in os.listdir(inputs_folder):
        

        filename = inputs_folder + k

        datcontent= [i.split() for i in open(filename).readlines()]
        datcontent = datcontent[1:]
        siz = len(datcontent)
        M = np.zeros((siz,2))
        M[:,0] = [datcontent[k][0] for k in range(siz)]
        M[:,1] = [datcontent[k][1] for k in range(siz)]
        M=sorted(M, key=lambda x: x[0])
        N = np.zeros((siz,3))
        m = int(round(M[0][0]))
        N[:,0] = [int(round(M[k][0]))-m for k in range(siz)]
        N[:,1] = [M[k][1] for k in range(siz)]
        dato_temp = np.zeros(31)

        for i in range(siz):
            index = int(N[i,0])
            dato_temp[index]=dato_temp[index]+N[i,1]
        print(dato_temp)
        print(type(dato_temp))
        dato_temp=np.reshape(dato_temp,(1,31))

        



        model_folder = 'models'
            
        model = load_model(model_folder + '/' +model)



        output = model.predict(dato_temp)
        
        
        file_save = outputs_folder + k
        File_object = open(file_save,'w+')
        File_object.writelines(str(output))       
        File_object.close()
HK_execution()

