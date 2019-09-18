import numpy as np

class Tensor (object):
    def __init__(self, data,
                 auto_grad = False,
                 creators = None,
                 creation_op = None,
                 id = None):
        self.data = np.array(data)
        self.auto_grad = auto_grad
        self.creators = creators
        self.creation_op = creation_op
        self.grad = None

        self.children = {}

        if ()

    def all_children_grads_accounted_for(self):

    def backward(self, grad=None, grad_origin=None):

    def __add__(self, other):

    def __reptr__(self):

    def __str__(self):
