import matplotlib.pyplot as plt
data = {'1000':  1.1743477821350098, '5000':  5.807514585494995,
        '10000': 11.580662042617798, '20000':  23.562452068328858}
tests = data.keys()
time = data.values()
# Create a figure and plot both sets of data on the same axes
plt.figure()

# Plot the first set of data
plt.bar(tests, time, color = 'red')

# Add labels and a title
plt.xlabel('Budget')
plt.ylabel('Time')
plt.title('MCTS-h1 with C = 0.1')

# Show the plot
plt.show()
