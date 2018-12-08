import tensorflow as tf
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'


val1 = tf.constant(5)
val2 = tf.constant(10)

sess = tf.Session()

print("Addition with constants: %i" % sess.run(val1+val2))
print("Multiplication with constants: %i" % sess.run(val1*val2))
print("Division with constants: %i" % sess.run(val1/val2))
print("Subtraction with constants: %i" % sess.run(val1-val2))
print("Modulus with constants: %i" % sess.run(val1%val2))