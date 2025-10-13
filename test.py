from signals import *
from operations import *


def test_create_sine_signal():
    t,v = create_sine_signal(1, 0, 10, 1, 1000)
    assert len(t) == 10000
    assert v[0] == 0

    t,v = create_sine_signal(1, 0, 10, 3, 1000)
    assert np.isclose(max(v),3,atol=1e-3)

    t,v = create_sine_signal(1, 0, -1, 1, 1000)
    assert len(t) == 0 and len(v) == 0

    t,v = create_sine_signal(5, 0, 1, 0, 1000)
    assert np.allclose(v,0)

def test_create_square_signal():
    t,v = create_square_signal(1, 0, 10, 1, 1000)
    assert len(t) == 10000
    assert v[0] == 0

    t,v = create_square_signal(1, 0, 10, 3, 1000)
    assert np.isclose(max(v),3,atol=1e-3)

    t,v = create_square_signal(1, 0, -1, 1, 1000)
    assert len(t) == 0 and len(v) == 0

    t,v = create_square_signal(5, 0, 1, 0, 1000)
    assert np.allclose(v,0)

def test_create_sawtooth_signal():
    t,v = create_sawtooth_signal(1, 0, 10, 1, 1000)
    assert len(t) == 10000
    assert v[0] == -1

    t,v = create_sawtooth_signal(1, 0, 10, 3, 1000)
    assert np.isclose(max(v),3,atol=1e-3)

    t,v = create_sawtooth_signal(1, 0, -1, 1, 1000)
    assert len(t) == 0 and len(v) == 0

    t,v = create_sawtooth_signal(5, 0, 1, 0, 1000)
    assert np.allclose(v,0)

def test_create_triangle_signal():
    t,v = create_triangle_signal(1, 0, 10, 1, 1000)
    assert len(t) == 10000
    assert v[0] == -1

    t,v = create_triangle_signal(1, 0, 10, 3, 1000)
    assert np.isclose(max(v),3,atol=1e-3)

    t,v = create_triangle_signal(1, 0, -1, 1, 1000)
    assert len(t) == 0 and len(v) == 0

    t,v = create_triangle_signal(5, 0, 1, 0, 1000)
    assert np.allclose(v,0)
    
def test_create_unit_step_signal():
    t,v = create_unit_step_signal(0, 10, 1000, 1, 5)
    assert len(t) == 10000
    assert v[0] == 0
    assert v[5000] == 1

    t,v = create_unit_step_signal(0, 10, 1000, 3, 5)
    assert np.isclose(max(v),3,atol=1e-3)

    t,v = create_unit_step_signal(0, -1, 1, 1, 0)
    assert len(t) == 0 and len(v) == 0

    t,v = create_unit_step_signal(0, 10, 1000, 0, 5)
    assert np.allclose(v,0)

