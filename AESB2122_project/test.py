from signals import *
from operations import *


def test_create_sine_signal():
    """
    Test the create_sine_signal function with various test cases.
    
    Tests include:
    - Signal length verification
    - Initial value check
    - Amplitude validation
    - Error handling for invalid duration
    - Zero amplitude case
    """
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
    """
    Test the create_square_signal function with various test cases.
    
    Tests include:
    - Signal length verification
    - Initial value check
    - Amplitude validation
    - Error handling for invalid duration
    - Zero amplitude case
    """
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
    """
    Test the create_sawtooth_signal function with various test cases.
    
    Tests include:
    - Signal length verification
    - Initial value check
    - Amplitude validation
    - Error handling for invalid duration
    - Zero amplitude case
    """
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
    """
    Test the create_triangle_signal function with various test cases.
    
    Tests include:
    - Signal length verification
    - Initial value check
    - Amplitude validation
    - Error handling for invalid duration
    - Zero amplitude case
    """
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
    """
    Test the create_unit_step_signal function with various test cases.
    
    Tests include:
    - Signal length verification
    - Step timing and value verification
    - Amplitude validation
    - Error handling for invalid duration
    - Zero amplitude case
    """
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

def test_time_shift():
    """
    Test the time_shift function with various test cases.
    
    Tests include:
    - Signal length verification
    - Shift timing and value verification
    - Negative shift handling
    - Zero shift case
    """
    t,v = create_sine_signal(1, 0, 10, 1, 100)
    v[500] = 1 

    shifted_signal = time_shift(v, 2, 100)
    assert len(shifted_signal) == 1000
    assert shifted_signal[700] == 1 

    shifted_signal = time_shift(v, -2, 100)
    assert len(shifted_signal) == 1000
    assert shifted_signal[300] == 1

    shifted_signal = time_shift(v, 0, 100)
    assert np.array_equal(shifted_signal, v)

def test_time_scale():
    """
    Test the time_scale function with various test cases.
    
    Tests include:
    - Signal length verification
    - Scaling factor validation
    - Edge case handling
    """
    t,v = create_sine_signal(1, 0, 10, 1, 1000)

    scaled_signal = time_scale(v, 2)
    assert len(scaled_signal) == 5000
    assert np.array_equal(scaled_signal, v[::2])

    scaled_signal = time_scale(v, 0.5)
    assert len(scaled_signal) == 20000

def test_amplitude_scale():
    """
    Test the amplitude_scale function with various test cases.
    
    Tests include:
    - Amplitude scaling verification
    - Negative scaling factor handling
    - Zero scaling case
    """
    t,v = create_sine_signal(1, 0, 10, 1, 1000)

    scaled_signal = amplitude_scale(v, 2)
    assert np.array_equal(scaled_signal, v * 2)

    scaled_signal = amplitude_scale(v, -1)
    assert np.array_equal(scaled_signal, v * -1)

    scaled_signal = amplitude_scale(v, 0)
    assert np.allclose(scaled_signal, 0)

def test_add_signals():
    """
    Test the add_signals function with various test cases.
    
    Tests include:
    - Element-wise addition verification
    - Different length handling (truncates to shorter)
    - Zero signal addition
    """
    t1, v1 = create_sine_signal(1, 0, 1, 1, 100)
    t2, v2 = create_sine_signal(2, 0, 1, 2, 100)

    added_signal = add_signals(v1, v2)
    assert len(added_signal) == min(len(v1), len(v2))

    signal3 = np.array([1, 2])
    added_signal = add_signals(v1, signal3)
    assert np.array_equal(added_signal, v1[:2] + signal3)

    zero_signal = np.zeros(3)
    added_signal = add_signals(v1, zero_signal)
    assert np.array_equal(added_signal, v1[:3])

def test_multiply_signals():
    """
    Test the multiply_signals function with various test cases.
    
    Tests include:
    - Element-wise multiplication verification
    - Different length handling (truncates to shorter)
    - Zero signal multiplication
    """
    t1, v1 = create_sine_signal(1, 0, 1, 1, 100)
    t2, v2 = create_sine_signal(2, 0, 1, 2, 100)

    multiplied_signal = multiply_signals(v1, v2)
    assert np.array_equal(multiplied_signal, v1 * v2)

    signal3 = np.array([1, 2])
    multiplied_signal = multiply_signals(v1, signal3)
    assert np.array_equal(multiplied_signal, v1[:2] * signal3)

    zero_signal = np.zeros(3)
    multiplied_signal = multiply_signals(v1, zero_signal)
    assert np.allclose(multiplied_signal, 0)