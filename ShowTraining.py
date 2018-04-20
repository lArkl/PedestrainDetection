def read_data(filename,index,epochs,loss,seconds):
    with open(filename) as f:
        for line in f:
            if 'images' in line:
                words = line.split()
                idx = int(words[0][:-1])
                if idx> index:
                    seconds.append(float(words[6]))
                    loss.append(float(words[2]))
                    epochs.append(idx)

epochs = []
loss = []
seconds = []
filename = 'output.txt'
read_data(filename,-1,epochs,loss,seconds)
#filename = 'output2.txt'
#read_data(filename,epochs[-1],epochs,loss,seconds)
#filename = 'output3.txt'
#read_data(filename,epochs[-1],epochs,loss,seconds)

import numpy as np
time = np.asarray(seconds).sum()/3600
print("Hours of Training:",time)

import matplotlib.pyplot as plt
#xmin = 0
xmin = 5000
plt.rcParams['figure.figsize'] = (10,6)
plt.plot(epochs[xmin:],loss[xmin:],'b')
plt.xlabel('Epochs')
plt.ylabel('Average Loss')
plt.show()


