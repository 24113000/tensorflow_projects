import tensorflow as tf
import numpy as np

group_mask = np.array([0, 1, 2, 3])


def to_group_masks(Y_):
    result = list()
    for i in range(Y_.shape[0]):
        number_group = Y_[i]
        result.append((group_mask == number_group).astype(np.int))
    return np.array(result)


X_ = np.load("x_data.npy")
Y_ = np.load("y_data.npy")
Y_ = to_group_masks(Y_)

x = tf.placeholder(tf.float32, [None, 40])
y = tf.placeholder(tf.float32, [None, 4])

hidden1 = tf.layers.dense(x, 2000, tf.nn.relu)
hidden2 = tf.layers.dense(hidden1, 2000, tf.nn.relu)
hidden3 = tf.layers.dense(hidden2, 1000, tf.nn.relu)
hidden4 = tf.layers.dense(hidden3, 700, tf.nn.relu)
hidden5 = tf.layers.dense(hidden4, 200, tf.nn.relu)
hidden6 = tf.layers.dense(hidden5, 80, tf.nn.relu)
hidden7 = tf.layers.dense(hidden6, 30, tf.nn.relu)
hidden8 = tf.layers.dense(hidden7, 10, tf.nn.relu)
output = tf.layers.dense(hidden8, 4, tf.nn.sigmoid)

loss = tf.losses.mean_squared_error(y, output)
optimizer = tf.train.GradientDescentOptimizer(0.01).minimize(loss)

init = tf.global_variables_initializer()
with tf.Session() as sess:
    sess.run(init)
    for i in range(2000):
        _, cost = sess.run([optimizer, loss], feed_dict={x: X_, y: Y_})
        print(cost)

    #result = sess.run(output, feed_dict={x: [[1, 1]]})
    #print(result)
