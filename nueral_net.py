import numpy as np

class model():

    def __init__(self, input_size, output_size, layer_size,n_layers):

        #initialise random weights and biases
        self.weights = {}
        self.bias = {}
        self.layers = n_layers

        self.weights[0] = np.random.randn(input_size,layer_size)
        self.bias[0]    = np.random.randn(layer_size)

        if self.layers > 1:
            for i in range(1,self.layers):
                self.weights[i] = np.random.randn(layer_size,layer_size)
                self.bias[i]    = np.random.randn(layer_size)

        self.weights[self.layers] = np.random.randn(layer_size,output_size)
        self.bias[self.layers]    = np.random.randn(output_size)


def forward(data, model):

    n_layers = model.layers

    z = data
    for i in range(n_layers+1):

        a = np.dot(z,model.weights[i]) + model.bias[i]
        z = np.maximum(a,np.zeros(a.size)) #RelU

    result = (np.tanh(z)+1)/2  #Squeeze result between 0 and 1

    return result

def cost_residuals_squared(data, true):

    fit = np.sum(np.sqrt((data-true)**2))

    return fit
