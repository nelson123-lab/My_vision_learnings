import torch
import torch.nn as nn
import torch.optim as optim
from torchvision import datasets, transforms

# Define the autoregressive model
class AutoregressiveModel(nn.Module):
    def __init__(self, input_size, hidden_size, output_size):
        super(AutoregressiveModel, self).__init__()
        self.hidden_size = hidden_size
        self.fc1 = nn.Linear(input_size, hidden_size)
        self.fc2 = nn.Linear(hidden_size, output_size)

    def forward(self, x):
        x = torch.relu(self.fc1(x))
        x = self.fc2(x)
        return x

# Define the compression function
def compress_image(image, model):
    # Flatten the image
    image = image.view(-1)
    # Initialize the compressed image
    compressed_image = torch.zeros_like(image)
    # Loop through each pixel in the image
    for i in range(len(image)):
        # Predict the next pixel value using the autoregressive model
        predicted_pixel = model(compressed_image[:i])
        # Calculate the residual between the predicted pixel value and the actual pixel value
        residual = image[i] - predicted_pixel
        # Store the residual in the compressed image
        compressed_image[i] = residual
    return compressed_image

# Define the decompression function
def decompress_image(compressed_image, model):
    # Initialize the decompressed image
    decompressed_image = torch.zeros_like(compressed_image)
    # Loop through each pixel in the compressed image
    for i in range(len(compressed_image)):
        # Predict the next pixel value using the autoregressive model
        predicted_pixel = model(decompressed_image[:i])
        # Add the residual to the predicted pixel value to get the actual pixel value
        actual_pixel = predicted_pixel + compressed_image[i]
        # Store the actual pixel value in the decompressed image
        decompressed_image[i] = actual_pixel
    # Reshape the decompressed image to its original shape
    decompressed_image = decompressed_image.view(image.shape)
    return decompressed_image

# Load the MNIST dataset
train_dataset = datasets.MNIST(root='./data', train=True, download=True, transform=transforms.ToTensor())
test_dataset = datasets.MNIST(root='./data', train=False, download=True, transform=transforms.ToTensor())
train_loader = torch.utils.data.DataLoader(train_dataset, batch_size=64, shuffle=True)
test_loader = torch.utils.data.DataLoader(test_dataset, batch_size=64, shuffle=True)

# Initialize the autoregressive model
model = AutoregressiveModel(input_size=1, hidden_size=256, output_size=1)

# Define the loss function and optimizer
criterion = nn.MSELoss()
optimizer = optim.Adam(model.parameters(), lr=0.001)

# Train the autoregressive model
for epoch in range(10):
    for batch_idx, (data, target) in enumerate(train_loader):
        # Compress the image
        compressed_image = compress_image(data, model)
        # Decompress the image
        decompressed_image = decompress_image(compressed_image, model)
        # Calculate the loss
        loss = criterion(decompressed_image, data)
        # Backpropagate the loss
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()
        # Print the loss every 100 batches
        if batch_idx % 100 == 0:
            print('Train Epoch: {} [{}/{} ({:.0f}%)]\tLoss: {:.6f}'.format(
                epoch, batch_idx * len(data), len(train_loader.dataset),
                100. * batch_idx / len(train_loader), loss.item()))

# Test the autoregressive model
test_loss = 0
with torch.no_grad():
    for data, target in test_loader:
        # Compress the image
        compressed_image = compress_image(data, model)
        # Decompress the image
        decompressed_image = decompress_image(compressed_image, model)
        # Calculate the loss
        test_loss += criterion(decompressed_image, data).item()
test_loss /= len(test_loader.dataset)
print('Test set: Average loss: {:.4f}'.format(test_loss))
