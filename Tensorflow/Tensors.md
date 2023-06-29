# Tensors
- Tensors are generalization of vectors and matrices to potentially higher dimesions. The data types can be float32, int32, float64, int64, string and others.

## Creating Tensors
```python
import tensorflow as tf

string = tf.Variable('Hello World', tf.string)
number = tf.Variable(342, tf.int32)
floating_number = tf.Variable(2343.454, tf.float32)
```
## Ranking of Tensors

- Depending on the dimesions involved in the tensors the rank/degree varies. The .shape method is used to find he shape.
```python
data = tf.Variable([[42,785657], [342,787], [2,78]], tf.int32)
print(data.shape)
"""
Output
(2, 2)
"""
```
- Degree of the tensors can be changed using reshaping.
```python
# When we are adding a -1, it calculates the size of the dimension in that place.
new_data = tf.reshape(data, [1, -1])
print(new_data.shape)
"""
Output
(1, 6)
"""
```

## Different types of Tensors
- Variables
  -  Used to store and update parameters during the training process. They hold values that can be modified, such as weights and biases       in a neural network. Variables are typically initialized with an initial value and can be updated during training to optimize the        model's performance.
- Constant
  -  Holds fixed values that do not change during the execution of a program. They are used to store values that remain constant              throughout the computation, such as hyperparameters or predefined values.
- Placeholder
  -  Used to feed input data into a TensorFlow computational graph. They act as empty containers that are filled with data at runtime.        Placeholders are commonly used when training a model with mini-batch or streaming data, where the input data is not known in             advance.
- SpareTensor
  -  A SparseTensor is a data structure used to efficiently represent and manipulate sparse data. Sparse data refers to data where most       of the elements are zero or empty. SparseTensors store only the non-zero or non-empty values along with their indices, saving            memory and computational resources. They are commonly used in applications such as natural language processing and recommendation        systems.
