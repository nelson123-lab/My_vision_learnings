-' einsum ' is a function in NumPy and PyTorch that provides a concise way to perform various tensor operations, including matrix multiplication, dot product, and 
  outer product. The name "einsum" stands "Einstein summation", named after the physicist Albert Einstein, who developed the concept of tensor calculus.

- The einsum function takes in a string that specifies the desired tensor operation, as well as one or more input tensors. The string specifies the indices of the
  input tensors that should be multiplied or summed, and the resulting indices of the output tensor.

- For example, suppose we have two matrices A and B of shape (3, 4) and (4, 5), respectively. We can use einsum to perform matrix multiplication as follows:
