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
- In transformer, we use a layer normalization not a batch normalization.

### Linear Head
- This is used to avoid overfitting in some how

## Residuals
- They are mainly to improve the flow of information. ( To avoid vanishing gradient descent - training signals are getting lost during backpropagation )

Bias variance difference?
Reference:-

-  [Paper: An image is worth 16 x 16 words video Explanation](https://youtu.be/TrdevFK_am4)
-  [Vision Transformer Quick Guide- Theory and Code](https://youtu.be/j3VNqtJUoz0)
-  [ViT Paper](https://arxiv.org/abs/2010.11929)
-  [Vision Transformers from scratch](https://colab.research.google.com/drive/1P9TPRWsDdqJC6IvOxjG2_3QlgCt59P0w?usp=sharing)
-  [ViT Github documentation](https://github.com/lucidrains/vit-pytorch#3d-vit)
