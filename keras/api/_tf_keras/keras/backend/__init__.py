"""DO NOT EDIT.

This file was autogenerated. Do not edit it by hand,
since your modifications would be overwritten.
"""


from keras.src.backend.common.dtypes import result_type
from keras.src.backend.common.global_state import clear_session
from keras.src.backend.common.keras_tensor import is_keras_tensor
from keras.src.backend.common.variables import is_float_dtype
from keras.src.backend.common.variables import is_int_dtype
from keras.src.backend.common.variables import standardize_dtype
from keras.src.backend.config import backend
from keras.src.backend.config import epsilon
from keras.src.backend.config import floatx
from keras.src.backend.config import image_data_format
from keras.src.backend.config import set_epsilon
from keras.src.backend.config import set_floatx
from keras.src.backend.config import set_image_data_format
from keras.src.utils.naming import get_uid

"""DO NOT EDIT.

This file was autogenerated. Do not edit it by hand,
since your modifications would be overwritten.
"""


from keras.src.legacy.backend import abs
from keras.src.legacy.backend import all
from keras.src.legacy.backend import any
from keras.src.legacy.backend import arange
from keras.src.legacy.backend import argmax
from keras.src.legacy.backend import argmin
from keras.src.legacy.backend import batch_dot
from keras.src.legacy.backend import batch_flatten
from keras.src.legacy.backend import batch_get_value
from keras.src.legacy.backend import batch_normalization
from keras.src.legacy.backend import batch_set_value
from keras.src.legacy.backend import bias_add
from keras.src.legacy.backend import binary_crossentropy
from keras.src.legacy.backend import binary_focal_crossentropy
from keras.src.legacy.backend import cast
from keras.src.legacy.backend import cast_to_floatx
from keras.src.legacy.backend import categorical_crossentropy
from keras.src.legacy.backend import categorical_focal_crossentropy
from keras.src.legacy.backend import clip
from keras.src.legacy.backend import concatenate
from keras.src.legacy.backend import constant
from keras.src.legacy.backend import conv1d
from keras.src.legacy.backend import conv2d
from keras.src.legacy.backend import conv2d_transpose
from keras.src.legacy.backend import conv3d
from keras.src.legacy.backend import cos
from keras.src.legacy.backend import count_params
from keras.src.legacy.backend import ctc_batch_cost
from keras.src.legacy.backend import ctc_decode
from keras.src.legacy.backend import ctc_label_dense_to_sparse
from keras.src.legacy.backend import cumprod
from keras.src.legacy.backend import cumsum
from keras.src.legacy.backend import depthwise_conv2d
from keras.src.legacy.backend import dot
from keras.src.legacy.backend import dropout
from keras.src.legacy.backend import dtype
from keras.src.legacy.backend import elu
from keras.src.legacy.backend import equal
from keras.src.legacy.backend import eval
from keras.src.legacy.backend import exp
from keras.src.legacy.backend import expand_dims
from keras.src.legacy.backend import eye
from keras.src.legacy.backend import flatten
from keras.src.legacy.backend import foldl
from keras.src.legacy.backend import foldr
from keras.src.legacy.backend import gather
from keras.src.legacy.backend import get_value
from keras.src.legacy.backend import gradients
from keras.src.legacy.backend import greater
from keras.src.legacy.backend import greater_equal
from keras.src.legacy.backend import hard_sigmoid
from keras.src.legacy.backend import in_top_k
from keras.src.legacy.backend import int_shape
from keras.src.legacy.backend import is_sparse
from keras.src.legacy.backend import l2_normalize
from keras.src.legacy.backend import less
from keras.src.legacy.backend import less_equal
from keras.src.legacy.backend import log
from keras.src.legacy.backend import map_fn
from keras.src.legacy.backend import max
from keras.src.legacy.backend import maximum
from keras.src.legacy.backend import mean
from keras.src.legacy.backend import min
from keras.src.legacy.backend import minimum
from keras.src.legacy.backend import moving_average_update
from keras.src.legacy.backend import name_scope
from keras.src.legacy.backend import ndim
from keras.src.legacy.backend import not_equal
from keras.src.legacy.backend import one_hot
from keras.src.legacy.backend import ones
from keras.src.legacy.backend import ones_like
from keras.src.legacy.backend import permute_dimensions
from keras.src.legacy.backend import pool2d
from keras.src.legacy.backend import pool3d
from keras.src.legacy.backend import pow
from keras.src.legacy.backend import prod
from keras.src.legacy.backend import random_bernoulli
from keras.src.legacy.backend import random_normal
from keras.src.legacy.backend import random_normal_variable
from keras.src.legacy.backend import random_uniform
from keras.src.legacy.backend import random_uniform_variable
from keras.src.legacy.backend import relu
from keras.src.legacy.backend import repeat
from keras.src.legacy.backend import repeat_elements
from keras.src.legacy.backend import reshape
from keras.src.legacy.backend import resize_images
from keras.src.legacy.backend import resize_volumes
from keras.src.legacy.backend import reverse
from keras.src.legacy.backend import rnn
from keras.src.legacy.backend import round
from keras.src.legacy.backend import separable_conv2d
from keras.src.legacy.backend import set_value
from keras.src.legacy.backend import shape
from keras.src.legacy.backend import sigmoid
from keras.src.legacy.backend import sign
from keras.src.legacy.backend import sin
from keras.src.legacy.backend import softmax
from keras.src.legacy.backend import softplus
from keras.src.legacy.backend import softsign
from keras.src.legacy.backend import sparse_categorical_crossentropy
from keras.src.legacy.backend import spatial_2d_padding
from keras.src.legacy.backend import spatial_3d_padding
from keras.src.legacy.backend import sqrt
from keras.src.legacy.backend import square
from keras.src.legacy.backend import squeeze
from keras.src.legacy.backend import stack
from keras.src.legacy.backend import std
from keras.src.legacy.backend import stop_gradient
from keras.src.legacy.backend import sum
from keras.src.legacy.backend import switch
from keras.src.legacy.backend import tanh
from keras.src.legacy.backend import temporal_padding
from keras.src.legacy.backend import tile
from keras.src.legacy.backend import to_dense
from keras.src.legacy.backend import transpose
from keras.src.legacy.backend import truncated_normal
from keras.src.legacy.backend import update
from keras.src.legacy.backend import update_add
from keras.src.legacy.backend import update_sub
from keras.src.legacy.backend import var
from keras.src.legacy.backend import variable
from keras.src.legacy.backend import zeros
from keras.src.legacy.backend import zeros_like