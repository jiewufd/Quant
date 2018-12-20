import unittest

import numpy as np

import customized_obj as cus_obj


class SigmoidLtObjCase(unittest.TestCase):
    def test_sigmoid_linear_transform(self):
        delta = 1e-6

        a = 20
        b = -0.15
        x = np.arange(-1,4)*0.1

        sigmoid, grad, hess = cus_obj.sigmoid_linear_transform(x,a,b)

        # Test sigmoid
        sigmoid_expected = np.array([0.0066928509242848554,
                            0.04742587317756678,
                            0.26894142136999516,
                            0.731058578630005,
                            0.9525741268224334])
        self.assertTrue(np.alltrue(sigmoid_expected - sigmoid < delta))

        delta_x = 1e-6
        x1 = x-delta_x
        x2 = x+delta_x
        sigmoid1, grad1, hess1 = cus_obj.sigmoid_linear_transform(x1,a,b)
        sigmoid2, grad2, hess2 = cus_obj.sigmoid_linear_transform(x2,a,b)

        # Test gradient
        grad_expected = (sigmoid2 - sigmoid1)/(x2-x1)
        self.assertTrue(np.alltrue(grad_expected-grad<delta))

        # Test hessian
        hess_expected = (grad2-grad1)/(x2-x1)
        self.assertTrue(np.alltrue(hess_expected-hess<delta))


    def test_sigmoid_lt_obj_generator(self):
        delta = 1e-6

        a = 20
        b = -0.15
        y_pred = np.arange(-1, 4) * 0.1
        y_true = y_pred*0.9
        # sigmoid_expected = np.array([0.0066928509242848554,
        #                              0.04742587317756678,
        #                              0.26894142136999516,
        #                              0.731058578630005,
        #                              0.9525741268224334])
        # grad_expected = a * sigmoid_expected * (1 - sigmoid_expected)
        # hess_expected = a * (1 - 2 * sigmoid_expected) * grad_expected
        # obj = cus_obj.sigmoid_lt_obj_generator(a,b)
        # grad, hess = obj(y_true,y_pred)
        #
        # print(grad)
        # print(hess)
        # self.assertTrue(np.alltrue(y_true * grad_expected - grad < delta))
        # self.assertTrue(np.alltrue(y_true * hess_expected - hess < delta))

        obj = cus_obj.sigmoid_lt_obj_generator(a, b)
        grad, hess = obj(y_true, y_pred)

        delta_y = 1e-6
        y1 = y_pred - delta_y
        y2 = y_pred + delta_y
        sigmoid1 = - y_true * cus_obj.sigmoid_linear_transform(y1,a,b)[0]
        sigmoid2 = - y_true * cus_obj.sigmoid_linear_transform(y2,a,b)[0]

        grad1, hess1 = obj(y_true,y1)
        grad2, hess2 = obj(y_true,y2)

        # Test gradient
        grad_expected = (sigmoid2 - sigmoid1) / (y2 - y1)
        self.assertTrue(np.alltrue(grad_expected - grad < delta))

        # Test hessian
        hess_expected = (grad2 - grad1) / (y2 - y1)
        self.assertTrue(np.alltrue(hess_expected - hess < delta))

        print(grad)
        print(hess)


if __name__ == '__main__':
    unittest.main()
