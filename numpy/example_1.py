import numpy as np

sensor_data = np.array([20.1, 20.4, 21.0, 20.7, 20.3, 20.8])

window = 3
moving_avg = np.convolve(sensor_data,
                          np.ones(window)/window,
                          mode='valid')

print(moving_avg)
