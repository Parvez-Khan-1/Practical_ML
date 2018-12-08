import tensorflow as tf

try:
    tf.contrib.eager.enable_eager_execution()
except ValueError:
    raise

tensor = tf.constant('Hello, World')
tensor_value = tensor.numpy()
print(tensor_value)

