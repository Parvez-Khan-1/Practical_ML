import os
import tensorflow as tf

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'


val1 = tf.placeholder(tf.int32)
val2 = tf.placeholder(tf.int32)

add = tf.add(val1, val2)
sub = tf.subtract(val1, val2)
mul = tf.multiply(val1, val2)
div = tf.divide(val1, val2)
mod = tf.mod(val1, val2)


with tf.Session() as sess:
    print("Addition : %i" % sess.run(add, feed_dict={val1: 5, val2: 10}))
    print("Subtraction : %i" % sess.run(sub, feed_dict={val1: 5, val2: 10}))
    print("Multiplication : %i" % sess.run(mul, feed_dict={val1: 5, val2: 10}))
    print("Division : %i" % sess.run(div, feed_dict={val1: 5, val2: 10}))
    print("Modulus : %i" % sess.run(mod, feed_dict={val1: 5, val2: 10}))
