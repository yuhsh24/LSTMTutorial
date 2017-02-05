import numpy as np
from LSTM import LstmParam, LstmNetwork

class ToyLossLayer:

    @classmethod
    def loss(cls, pred, label):
        return (pred[0] - label) ** 2

    @classmethod
    def bottom_diff(cls, pred, label):
        diff = np.zeros_like(pred)
        diff[0] = 2 * (pred[0] - label)
        return diff

def example_0():
    np.random.seed(0)

    mem_cell_ct = 1000
    x_dim = 50
    concat_len = x_dim + mem_cell_ct
    lstm_param = LstmParam(mem_cell_ct, x_dim)
    lstm_net = LstmNetwork(lstm_param)
    y_list = [-0.5, 0.2, 0.1, -0.5]
    input_val_arr = [np.random.random(x_dim) for _ in y_list]

    for cur_iter in range(1000):
        print "cur iter: ", cur_iter
        for ind in range(len(y_list)):
            lstm_net.x_list_add(input_val_arr[ind])
            print "y_pred[%d] : %f" % (ind, lstm_net.lstm_node_list[ind].state.h[0])

        loss = lstm_net.y_list_is(y_list, ToyLossLayer)
        print "loss: ", loss
        lstm_net.lstm_param.apply_diff(lr=0.1)
        lstm_net.x_list_clear()

if __name__ == "__main__":
    example_0()