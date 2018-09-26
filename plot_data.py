import matplotlib.pyplot as plt 


def plot_data(data):

    plt.title('X,Y,Z Plot')
    plt.plot([row[0] for row in data], label="x")
    plt.plot([row[1] for row in data], label="y")
    plt.plot([row[2] for row in data], label="z")
    plt.legend(loc='upper right')
    plt.show()

def plot_data_magnitude(data, vectors):

    plt.title('X,Y,Z, Vector Plot')
    plt.plot([row[0] for row in data], label="x")
    plt.plot([row[1] for row in data], label="y")
    plt.plot([row[2] for row in data], label="z")

    plt.plot(vectors, label="v")
    plt.legend(loc='upper right')
    plt.show()

# plot_data("test.csv")
