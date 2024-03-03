import matplotlib.pyplot as plt
data = {'5 moves':  0.4963345527648926, '7 moves':  4.9502346515655,
        '9 moves': 5.488623698933919, '11 moves':  5.61386018991470}
tests = data.keys()
time = data.values()
# Create a figure and plot both sets of data on the same axes
plt.figure()

# Plot the first set of data
plt.bar(tests, time, color = 'blue')

# Add labels and a title
plt.xlabel('States')
plt.ylabel('Time')
plt.title('A*-h3')

# Show the plot
plt.show()
