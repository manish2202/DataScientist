import numpy as np
from datascientist.model.regression.evaluation_metrics.mse import _mse

def test_mse():
    a = np.array([0, 1, 2])
    b = np.array([3, 2, 1])
    
    assert round(_mse(a, b), 2) == 3.67
