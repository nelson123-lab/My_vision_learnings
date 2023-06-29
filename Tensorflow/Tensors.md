# Tensors
- Tensors are generalization of vectors and matrices to potentially higher dimesions. The data types can be float32, int32, float64, int64, string and others.

## Creating Tensors
```python
import tensorflow as tf

string = tf.Variable('Hello World', tf.string)
number = tf.Variable(342, tf.int32)
floating_number = tf.Variable(2343.454, tf.float32)
```
