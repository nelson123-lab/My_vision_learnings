### Correlation
Correlation is a mathematical operation that measures the similarity between two signals or images. It involves sliding a template or kernel over an input image and computing the similarity between the template and the corresponding image patch. Correlation is commonly used in tasks such as template matching, where the goal is to find instances of a template within an image.

### Convolution
Convolution, on the other hand, is a mathematical operation that combines two functions to produce a third function. In the context of computer vision, convolution is typically used for filtering and feature extraction. It involves convolving an input image with a filter or kernel, which is a small matrix of weights. The convolution operation computes the weighted sum of the pixel values in the image neighborhood defined by the kernel. Convolution is widely used in tasks such as edge detection, blurring, and feature extraction using convolutional neural networks (CNNs).

While both correlation and convolution involve sliding a kernel over an image, the key difference lies in the mathematical operation performed. In correlation, the kernel is directly compared with the image patch, measuring similarity. In convolution, the kernel's weights are multiplied with the corresponding pixel values in the image patch, resulting in a weighted sum.

It's important to note that correlation and convolution are closely related, and in some cases, they can be used interchangeably by flipping the kernel. However, in computer vision, convolution is more commonly used due to its versatility and its ability to capture spatial relationships and extract meaningful features from images.

References:
- [What is digital image filtering and image convolution?](https://youtu.be/1GUgD2SBl9A)
