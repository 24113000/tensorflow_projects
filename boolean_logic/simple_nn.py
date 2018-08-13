import tensorflow as tf
import numpy as np

X_ = np.array([[1, 1], [1, 0], [0, 1], [0, 0]])
Y_ = np.array([[1.], [0.], [1.], [0.]])

x = tf.placeholder(tf.float32, [None, 2])
y = tf.placeholder(tf.float32, [None, 1])

hidden1 = tf.layers.dense(x, 10, tf.nn.relu)
hidden2 = tf.layers.dense(hidden1, 3, tf.nn.relu)
output = tf.layers.dense(hidden2, 1, tf.nn.sigmoid)

loss = tf.losses.mean_squared_error(y, output)
optimizer = tf.train.GradientDescentOptimizer(0.01).minimize(loss)

init = tf.global_variables_initializer()
with tf.Session() as sess:
    sess.run(init)
    for i in range(10000):
        _, cost = sess.run([optimizer, loss], feed_dict={x: X_, y: Y_})
        print(cost)

    result = sess.run(output, feed_dict={x: [[1, 1]]})
    print(result)
