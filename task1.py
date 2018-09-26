import androidParser
from plot_data import plot_data, plot_data_magnitude
from util import vector_magnitude

def count_steps(data):
    print ("Accelerometer data graph")
    # plot_data(data)
    num_steps = 0
    '''
    ADD YOUR CODE HERE. This function counts the number of steps in data and returns the number of steps
    '''

    vector_data = vector_magnitude(data)
    # print(vector_data)
    
    plot_data_magnitude(data, vector_data)

    return num_steps


def run():
    # Get data
    file_name = "walking_100_new.csv"  # Change to your file name
    data = androidParser.get_data(file_name)
    number_of_steps = count_steps(data)
    print ("Number of steps counted are :", number_of_steps)

run()

