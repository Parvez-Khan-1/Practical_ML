from tensorflow.examples.tutorials.mnist import input_data
import tensorflow as tf
mnist = input_data.read_data_sets("/tmp/data/", one_hot=True)

learning_rate = 0.01
num_steps = 500
batch_size = 128
display_step = 100


n_hidden_1 = 256
n_hidden_2 = 256
num_input = 784
num_classes = 10

X = tf.placeholder("float", [None, num_input])
Y = tf.placeholder("float", [None, num_classes])

weights = {
    'h1' : tf.Variable(tf.random_normal([num_input, n_hidden_1])),
    'h2' : tf.Variable(tf.random_normal([n_hidden_1, n_hidden_2])),
    'out' : tf.Variable(tf.random_normal([n_hidden_2, num_classes]))
}

biases = {
    'b1': tf.Variable(tf.random_normal([n_hidden_1])),
    'b2': tf.Variable(tf.random_normal([n_hidden_2])),
    'out': tf.Variable(tf.random_normal([num_classes]))
}


def neural_net(x):
    layer1 = tf.add(tf.matmul(x, weights['h1']), biases['b1'])
    layer2 = tf.add(tf.matmul(layer1, weights['h2']), biases['b2'])
    out_layer = tf.matmul(layer2, weights['out']) + biases['out']
    return out_layer


logits = neural_net(X)
prediction = tf.nn.softmax(logits)

print(logits)

# Define loss and optimizer
loss_op = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits(logits=logits, labels=Y))
optimizer = tf.train.AdamOptimizer(learning_rate=learning_rate)
train_op = optimizer.minimize(loss_op)


# Evaluate Model
correct_pred = tf.equal(tf.argmax(prediction, 1), tf.argmax(Y, 1))
accuracy =  tf.reduce_mean(tf.cast(correct_pred, tf.float32))

init = tf.global_variables_initializer()


# Start training
with tf.Session() as sess:

    # Run the initializer
    sess.run(init)

    for step in range(1, num_steps+1):
        batch_x, batch_y = mnist.train.next_batch(batch_size)
        # Run optimization op (backprop)
        sess.run(train_op, feed_dict={X: batch_x, Y: batch_y})
        if step % display_step == 0 or step == 1:
            # Calculate batch loss and accuracy
            loss, acc = sess.run([loss_op, accuracy], feed_dict={X: batch_x,
                                                                 Y: batch_y})
            print("Step " + str(step) + ", Minibatch Loss= " + \
                  "{:.4f}".format(loss) + ", Training Accuracy= " + \
                  "{:.3f}".format(acc))

    print("Optimization Finished!")

    # Calculate accuracy for MNIST test images
    print("Testing Accuracy:", sess.run(accuracy, feed_dict={X: mnist.test.images, Y: mnist.test.labels}))