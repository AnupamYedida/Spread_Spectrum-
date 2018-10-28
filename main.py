#!/usr/bin/env python
from scipy.signal import max_len_seq
import sys 
import numpy as np 
import random 
from random import randint
import math 
import matplotlib.pyplot as plt
from matplotlib.pyplot import step, xlim, ylim, show
import scipy


# _Variables Declaration 
vader = 16 


########-----------------TRANSMISSION---------------------########


# _PN Sequence Generation
pn_seq = max_len_seq(int(math.sqrt(vader)))[0].tolist()

for _ in range(0,vader-1):
	if pn_seq[_] == 0:
		pn_seq[_] = -1

print "A Random PN-Sequence is Generated ------->", pn_seq

# _Message Bits 
message = []

for _ in range(vader-1):
	anakin = randint(0,1)
	message.append(anakin)

for _ in range(0,vader-1):
	if message[_] == 0:
		message[_] = -1

print "A Random Message Signal is generated ----->", message



if len(pn_seq) == len(message):
	print "Sequences are EQUAL"
else:
	print "Sequences aren't equal"


# _Spreading of Message with PN-Sequence

spread_seq = [] 
for _ in range(vader-1):	
	spread_seq.append(pn_seq[_]^message[_])

for _ in range(vader-1):
	if spread_seq[_] == -2:
		spread_seq[_] = 1

for _ in range(vader-1):
	if (message[_] == -1 & pn_seq[_] == 1) | (message[_] == 1 & pn_seq[_] == -1):
		spread_seq[_] = -1

	if spread_seq[_] == 0:
		spread_seq[_] = -1


print "The Sequence after Successful Spreading is ---->", spread_seq




########-----------------RECEIVING---------------------########


demod = []
rx_pn_seq = pn_seq 
demod = message

for _ in range(len(spread_seq)):
	if rx_pn_seq[_] & spread_seq[_] == -1:
		demod[_] = 1
	elif rx_pn_seq[_] & spread_seq[_] == 1:
		demod[_] = -1
	


### _Plotting Everything ###

fig = plt.figure()

# _Message Signal 

kylo_ren = np.arange(0, vader-1)
han_solo = np.array((message))
xlim(0, 15)
ylim(-1.5, 1.5)
#plt.figure(0)
demod = message
plt.subplot(3, 1, 1)
ax1 = fig.add_subplot(311)
ax1.title.set_text('Message')
plt.step(kylo_ren, han_solo)

# _PN-Sequence 

c3po  = np.arange(0, vader-1)
r2d2 = np.array((pn_seq))
xlim(0, 15)
ylim(-1.5, 1.5)
#plt.figure(1)
plt.subplot(3, 1, 2)
ax2 = fig.add_subplot(312)
ax2.title.set_text('PN-Sequence')

plt.step(c3po, r2d2)


# _Spread Waveform 

finn = np.arange(0, vader-1)
rey  = np.array((spread_seq))
xlim(0, 15)
ylim(-1.5, 1.5)
#plt.figure(2)
plt.subplot(3, 1, 3)
ax3 = fig.add_subplot(313)
ax3.title.set_text('DSSS')

plt.step(finn, rey)

fig.tight_layout()



fig_1 = plt.figure()

boba = np.arange(0, vader-1)
jabba = np.array((demod))
xlim(0, 15)
ylim(-1.5, 1.5)
#plt.figure(0)
plt.subplot(3, 1, 1)
ax1 = fig.add_subplot(311)
ax1.title.set_text('Message')
plt.step(boba, jabba)






















plt.show()









