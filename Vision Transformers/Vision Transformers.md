## Vision Transformer

This is an extension of the transformers for image data. We use only the left part of the Transformer architecture (Encoder). The right part is the decoder which is used generally for sequencial generation task (Chat GPT). Vision Transformers are used only if we have huge
amount of data otherwise it is preferred to use CNN.

Working:-
- The inputs are converted into input embeddings which lets you project data into a vector space.
- The image to embeddings conversion is done with the help of a technique called patching.

### Patching
- The image is patched into 16 x 16 pixel tiles and pass each of the patches through the first component of the transformer encoder which gives us embeddings.

### CLS Token
- The "CLS" token in vision transformers refers to the "classification token." In vision transformers, the input image is divided into patches, and each patch is then processed by the transformer network. The "CLS" token is a special token that is added at the beginning of the sequence of patches.

- The purpose of the "CLS" token is to provide a global representation of the image that can be used for classification tasks. It allows the transformer network to learn to attend to important
  patches and capture the overall context of the image. The output of the "CLS" token can then be used as input to a classifier to make predictions.

- By including the "CLS" token, vision transformers can effectively handle both classification and other vision tasks, such as object detection or segmentation, by leveraging the power of the transformer architecture.

### The positional Embedding
- This allows models to understand where the patch is placed in the original image. It keeps track of the spatial arrangment of the patches.
- There are different ways to generate positional embeddings. One common approach is to use sine and cosine functions with different frequencies. These functions create smooth patterns that encode the position information.
- When it comes to positional embeddings, using numbers can have a few disadvantages.
  1. Limited range: Numbers have a finite range, which means that if you're working with sequences that are longer than the range of your positional embeddings, you may encounter issues. 
  2. Lack of context: Numbers used as positional embeddings don't inherently provide any contextual information about the sequence. 
  3. Fixed representation: Numbers used as positional embeddings provide a fixed representation for each position in the sequence. 
  4. Difficulty in capturing long-range dependencies: Numbers used as positional embeddings may struggle to capture long-range dependencies in the sequence. 

### Multi-head attention


### Normalization
Normalization in transformers, specifically in the context of deep learning, is an essential technique used to stabilize and accelerate the training of neural networks, including transformer models. There are two main types of normalization used in transformers: Layer Normalization and Batch Normalization.

1. **Layer Normalization (LN):** This type of normalization is typically applied independently to each layer in the transformer architecture, which includes the multi-head self-attention layers and feedforward neural network layers. Here's why we use Layer Normalization in transformers:

   - **Stability in Training:** Layer Normalization helps in stabilizing the activations within each layer during training. It addresses the problem of internal covariate shift, which occurs when the distribution of activations in a layer changes as training progresses. By normalizing the inputs to each layer, the network becomes less sensitive to the scale of inputs, which can make training more stable.

   - **Improved Gradient Flow:** Normalization techniques like Layer Normalization make it easier for gradients to flow through the network during backpropagation. This can lead to faster convergence during training.

   - **Regularization Effect:** Layer Normalization can also act as a form of regularization, helping prevent overfitting to some extent.

2. **Batch Normalization (BN):** While Layer Normalization is applied within each layer, Batch Normalization operates on mini-batches of data at each layer. It computes the mean and standard deviation of activations within a batch and then normalizes the activations based on these statistics. Batch Normalization is often used in convolutional neural networks (CNNs) but is less common in transformers. However, it can be used in combination with Layer Normalization for certain purposes.

   - **Accelerated Training:** Batch Normalization can significantly accelerate training by reducing the internal covariate shift within each layer. It helps ensure that activations maintain a similar scale throughout training, allowing for the use of higher learning rates and faster convergence.

   - **Regularization:** Similar to Layer Normalization, Batch Normalization also provides a certain level of regularization, which can help prevent overfitting.

In transformers, Layer Normalization is more commonly used because it fits the architecture's sequential nature, where each layer has its own normalization step. However, some variations and improvements to transformer architectures might incorporate Batch Normalization or other normalization techniques for specific tasks or architectures.

In summary, normalization techniques like Layer Normalization and Batch Normalization are crucial in transformers to stabilize training, accelerate convergence, and facilitate gradient flow, ultimately leading to better model performance.

### Linear Head
- This is used to avoid overfitting in some how
- In the context of transformers, a "linear head" typically refers to the output layer of the transformer model, which is often a linear transformation applied to the final hidden states of the model. This linear transformation is responsible for producing the model's predictions or outputs for a particular task. It's also sometimes called the "classification head" or "output head."

Here's how it works:

1. **Transformer Encoder:** The main part of a transformer model consists of an encoder, which takes in an input sequence and processes it through multiple layers of self-attention and feedforward neural networks. This results in a set of hidden states, one for each token in the input sequence.

2. **Linear Head:** After the input has been processed by the encoder, the final hidden states (or a specific layer's hidden states, depending on the architecture) are used as input to the linear head. The linear head is essentially a linear transformation, often followed by an activation function, that maps the high-dimensional hidden states into the desired output space for the specific task the transformer is being used for.

   - **For Classification:** In tasks like text classification or sentiment analysis, the linear head might consist of a linear layer followed by a softmax activation function to produce class probabilities.

   - **For Sequence-to-Sequence Tasks:** In tasks like machine translation or text generation, the linear head may involve a linear layer followed by a softmax or a linear layer followed by a sequence-to-sequence model.

   - **For Regression:** In regression tasks, the linear head may consist of a single linear layer to produce a continuous-valued output.

The linear head essentially learns the task-specific mapping from the learned representations in the transformer's hidden states to the output format required for the particular problem at hand. It's a crucial component of the transformer architecture, as it allows the model to adapt its learned features to different tasks without changing the encoder's architecture.

In summary, the linear head in transformers is the part of the model responsible for transforming the encoder's hidden states into the final output format for a given task, whether that's classification, regression, or another sequence-based task. It is often implemented as a linear layer followed by appropriate activation functions, depending on the specific task's requirements.

## Residuals
- They are mainly to improve the flow of information. ( To avoid vanishing gradient descent - training signals are getting lost during backpropagation )

Bias variance difference?
Reference:-

-  [Paper: An image is worth 16 x 16 words video Explanation](https://youtu.be/TrdevFK_am4)
-  [Vision Transformer Quick Guide- Theory and Code](https://youtu.be/j3VNqtJUoz0)
-  [ViT Paper](https://arxiv.org/abs/2010.11929)
-  [Vision Transformers from scratch](https://colab.research.google.com/drive/1P9TPRWsDdqJC6IvOxjG2_3QlgCt59P0w?usp=sharing)
-  [ViT Github documentation](https://github.com/lucidrains/vit-pytorch#3d-vit)
