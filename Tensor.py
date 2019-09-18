import numpy as np

class Tensor (object):
    def __init__(self, data,
                 auto_grad=False,
                 creators=None,
                 creation_op=None,
                 id=None):
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

a = Tensor([1, 2, 3, 4, 5], autograd=True)
b = Tensor([2, 2, 2, 2, 2], autograd=True)
c = Tensor([5, 4, 3, 2, 1], autograd=True)

d = a + b
e = b + c
f = d + e

f.backward(Tensor(np.array([1, 1, 1, 1, 1])))

print(b.grad.data == np.array([2, 2, 2, 2, 2]))
