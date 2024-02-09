from load_data import * #import all the data variables from load_data
import numpy as np
import matplotlib.pyplot as plt
from PyEMD import EMD


t1=np.linspace(0,168,168)
t2=np.linspace(0,161,161)
t3=np.linspace(0,72,72)
t4=np.linspace(0,72,72)
t5=np.linspace(0,73,73)
t6=np.linspace(0,72,72)


x=soh_data_battery5.values[:]
print('Shape of battery_data_5\t',soh_data_battery5.shape)

x1=soh_data_battery6.values[:]
print('Shape of battery_data_6\t',soh_data_battery6.shape)

x2=soh_data_battery45.values[:]
print('Shape of battery_data_45\t',soh_data_battery45.shape)

x3=soh_data_battery46.values[:]
print('Shape of battery_data_46\t',soh_data_battery46.shape)

x4=soh_data_battery47.values[:]
print('Shape of battery_data_47\t',soh_data_battery47.shape)

x5=soh_data_battery48.values[:]
print('Shape of battery_data_48\t',soh_data_battery48.shape)


emd = EMD()
imfs_5 = emd(x)
imfs_6 = emd(x1)
imfs_7 = emd(x2)
imfs_8 = emd(x3)
imfs_9 = emd(x4)
imfs_10 = emd(x5)

# Battery 5
plt.figure(figsize=(10,8))
plt.subplot(len(imfs_5)+1,1,1)
plt.plot(t1, soh_data_battery5, 'r')
plt.title('Battery 5 Original Signal')
for i, imf in enumerate(imfs_5):
    plt.subplot(len(imfs_5)+1,1,i+2)
    plt.plot(t1, imf, 'g')
    plt.title(f'IMF {i+1}')
plt.tight_layout()

# Battery 6
plt.figure(figsize=(10,8))
plt.subplot(len(imfs_6)+1,1,1)
plt.plot(t2, soh_data_battery6, 'r')
plt.title('Battery 6 Original Signal')
for i, imf in enumerate(imfs_6):
    plt.subplot(len(imfs_6)+1,1,i+2)
    plt.plot(t2, imf, 'g')
    plt.title(f'IMF {i+1}')
plt.tight_layout()

# Battery 45
plt.figure(figsize=(10,8))
plt.subplot(len(imfs_7)+1,1,1)
plt.plot(t3, soh_data_battery45, 'r')
plt.title('Battery 45 Original Signal')
for i, imf in enumerate(imfs_7):
    plt.subplot(len(imfs_7)+1,1,i+2)
    plt.plot(t3, imf, 'g')
    plt.title(f'IMF {i+1}')
plt.tight_layout()

# Battery 46
plt.figure(figsize=(10,8))
plt.subplot(len(imfs_8)+1,1,1)
plt.plot(t4, soh_data_battery46, 'r')
plt.title('Battery 46 Original Signal')
for i, imf in enumerate(imfs_8):
    plt.subplot(len(imfs_8)+1,1,i+2)
    plt.plot(t4, imf, 'g')
    plt.title(f'IMF {i+1}')
plt.tight_layout()

# Battery 47
plt.figure(figsize=(10,8))
plt.subplot(len(imfs_9)+1,1,1)
plt.plot(t5, soh_data_battery47, 'r')
plt.title('Battery 47 Original Signal')
for i, imf in enumerate(imfs_9):
    plt.subplot(len(imfs_9)+1,1,i+2)
    plt.plot(t5, imf, 'g')
    plt.title(f'IMF {i+1}')
plt.tight_layout()

# Battery 48
plt.figure(figsize=(10,8))
plt.subplot(len(imfs_10)+1,1,1)
plt.plot(t6, soh_data_battery48, 'r')
plt.title('Battery 48 Original Signal')
for i, imf in enumerate(imfs_10):
    plt.subplot(len(imfs_10)+1,1,i+2)
    plt.plot(t6, imf, 'g')
    plt.title(f'IMF {i+1}')
plt.tight_layout()

plt.show() #plot all the figures at once