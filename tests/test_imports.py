def test_imports():
    import tensorflow as tf
    import tensorflow_probability as tfp
    assert tf.__version__
    assert tfp.__version__
