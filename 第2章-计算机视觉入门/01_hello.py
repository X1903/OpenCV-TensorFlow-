# _*_ coding:utf-8 _*_
__author__ = 'Xbc'

import tensorflow as tf

hello = tf.constant('hello world')
sess = tf.Session()
print(sess.run(hello))


import cv2
print('hello opencv')