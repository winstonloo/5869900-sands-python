from signals import *
from operations import *

def create_sine_signal(f, s_t, e_t, a, s_r):
    duration = e_t - s_t
    if duration < 0:
        return np.array([]), np.array([])
    t = np.linspace(s_t, e_t, int(s_r * duration))
    v = a * np.sin(2 * np.pi * f * t)
    return t,v

def test_create_sine_signal():
    t,v = create_sine_signal(1, 0, 10, 1, 100)
    assert len(t) == 1000
    assert v[0] == 0

    t,v = create_sine_signal(1, 0, 10, 3, 100)
    assert np.isclose(max(v),3,atol=1e-6)

    t,v = create_sine_signal(1, 0, -1, 1, 100)
    assert len(t) == 0 and len(v) == 0

    t,v = create_sine_signal(5, 0, 1, 0, 100)
    assert np.allclose(v,0)

def test_create_square_signal():
    t,v = create_square_signal(1, 0, 10, 1, 100)
    assert len(t) == 1000
    assert v[0] == 0

    t,v = create_square_signal(1, 0, 10, 3, 100)
    assert np.isclose(max(v),3,atol=1e-6)

    t,v = create_square_signal(1, 0, -1, 1, 100)
    assert len(t) == 0 and len(v) == 0

    t,v = create_square_signal(5, 0, 1, 0, 100)
    assert np.allclose(v,0)