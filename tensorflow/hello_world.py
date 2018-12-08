import tensorflow as tf
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'
message = tf.constant("Hello, tensor-flow")
sess = tf.Session()
print(sess.run(message))
