import matplotlib.pyplot as plt
import numpy as np

# Sample data
11.260472536087036
data = {'36944': 0.08662652969360352, '294984': 1.3177263736724854,
        '5242952': 20.970603942871094, '2621520':  252.88993906974792}
tests = data.keys()
time = data.values()
# x1 = (0.08662652969360352, 1.3177263736724854, 20.970603942871094, 252.88993906974792)
# y1 = (36944, 294984, 5242952, 2621520)
# x2 =  (0.0456693172454834, 0.11113476753234863, 0.31879472732543945, 1.5753357410430908)
# y2 = (9360, 37008, 147600, 589968)

# Create a figure and plot both sets of data on the same axes
plt.figure()

# Plot the first set of data
plt.bar(tests, time, color = 'pink')

# Plot the second set of data
# plt.plot(x2, y2, label='Bidirectional BFS')

# Add labels and a title
plt.xlabel('Number of States Discovered')
plt.ylabel('Time per test')
plt.title('A*')

# Add a legend

# Show the plot
plt.show()
