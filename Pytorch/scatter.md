- ' scatter ' is used to scatter the values of a tensor into another tensor according to a specified index. It takes in three inputs: the input tensor, the 
  index tensor, and the source tensor. The index tensor specifies the indices at which to scatter the values of the source tensor into the input tensor.

- For example, if we have an input tensor of shape (3, 4) and a source tensor of shape (2, 4), we can use scatter to scatter the values of the source tensor 
  into the input tensor at indices (0, 1) and (2, 3) as follows:
  
```python
input = torch.zeros(3, 4)
index = torch.tensor([[0, 1], [2, 3]])
source = torch.tensor([[1, 2, 3, 4], [5, 6, 7, 8]])
input.scatter_(0, index, source)
```
