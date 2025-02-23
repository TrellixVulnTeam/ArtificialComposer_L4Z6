import shelve
from keras.optimizers import RMSprop
from neupy.datasets import make_reber
from keras.models import Sequential, load_model
from keras.layers import Dense, Dropout, Activation, TimeDistributed
from keras.layers import LSTM
from keras.utils import np_utils, plot_model
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np

if 'model' not in vars():
	model = load_model('embedCerg_model.h5')
else:
	model.reset_states()

char_indices = {'B': 0, 'E': 1, 'P': 2, 'S': 3, 'T': 4, 'V': 5, 'X': 6}
indices_char = dict((i, c) for i, c in enumerate(char_indices))



input_shape = (model.get_layer(index=0)).input_shape

xPredictBatch = -1*np.ones(input_shape)

xPredictBatch[0,0] = np.array([ 1.,  0.,  0.,  0.,  0.,  0.,  0.]) #give it a B :-) 

for i in  range(49):# range(len(xPredictBatch[0])):
	P = model.predict(xPredictBatch, batch_size = input_shape[0])
	choice = np.argmax(P[0,i])

	xPredictBatch[0,i+1] = np.zeros(7)
	xPredictBatch[0,i+1,choice] = 1
	model.reset_states()

P = P.transpose(0,2,1)

imgplot = plt.imshow(P[0])
plt.yticks(np.arange(P[0].shape[0]), list(indices_char.values()))
plt.xticks(np.arange(P[0].shape[1]), [indices_char[np.argmax(i)] for i in xPredictBatch[0]])
plt.title('Generated Reber Word sampled with argmax')
#plt.colorbar()
plt.show()