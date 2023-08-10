# Global imports (for independent module run)
import os
import sys

parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(parent_dir)

from __init__ import *
from DC_settings import *

def main(src3_parse):
    df = src3_parse
    L_plates = df['Plates'].tolist()

    # Legal letters
    legal_letters = ['А', 'В', 'Е', 'К', 'М', 'Н', 'О', 'Р', 'С', 'Т', 'У', 'Х', 'а', 'в', 'е', 'к', 'м', 'н', 'о', 'р', 'с', 'т', 'у', 'х']

    # Define Neural Network Architecture
    input_dim = 4
    hidden_dim = 4
    output_dim = 1

    # Initialize weights and biases for the first hidden layer manually
    weights1 = np.array([[1, 0.6, 0.7, 0.8],
                         [0.2, 0.3, 0.4, 0.5],
                         [0.3, 0.4, 0.5, 0.6],
                         [0.4, 0.5, 0.6, 0.7]])

    bias1 = np.array([-0.4, -0.3, -0.6, -0.5])

    # Define Sigmoid Activation Function
    def sigmoid(x):
        return 1 / (1 + np.exp(-x))

    # Training Loop
    learning_rate = 0.1
    epochs = 1000

    # Define the plate validation function using the neural network
    def is_valid_plate(plate):
        # Vectorize the plate properties
        input_data = []

        # Plate length
        input_data.append(1 if len(plate) == 9 and ' ' not in plate else 0)

        # String has 3 letters
        input_data.append(2 if len([c for c in plate if c.isalpha()]) == 3 else 0)

        # String has 6 digits
        input_data.append(3 if len([c for c in plate if c.isdigit()]) == 6 else 0)

        # String letters are legal
        input_data.append(4 if all(c in legal_letters for c in plate if c.isalpha()) else 0)

        # Forward Propagation
        hidden_layer1 = np.dot(input_data, weights1) + bias1
        hidden_output1 = sigmoid(hidden_layer1)
        output_layer = np.dot(hidden_output1, weights1) + bias1
        output = sigmoid(output_layer)

        # If the output is close to 1, it is considered a valid plate
        return output >= 0.8

    # Validation
    for plate in L_plates:
        if len(plate) > 1:
            is_valid = is_valid_plate(plate[1])
            print(f"Plate: {plate[1]}, Valid: {is_valid}")
        is_valid = is_valid_plate(plate[0])
        print(f"Plate: {plate[0]}, Valid: {is_valid}")
         

        

if __name__ == '__main__':
    main()
    start_time = time.time()
    pprint("--- %s seconds ---" % (time.time() - start_time))
