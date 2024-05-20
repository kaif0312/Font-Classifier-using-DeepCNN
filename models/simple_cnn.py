import torch.nn as nn
import torch.nn.functional as F
class SimpleCNN(nn.Module):
    def __init__(self):
        super(SimpleCNN, self).__init__()
        # Define the layers
        self.conv1 = nn.Conv2d(1, 64, 5, padding=2)  # Changed kernel size to 5 to accommodate 64x64 input
        self.pool = nn.MaxPool2d(2, 2)    # kernel size, stride
        self.conv2 = nn.Conv2d(64, 128, 5, padding=2)  # Changed kernel size to 5 to maintain feature map size
        self.fc1 = nn.Linear(128 * 16 * 16, 512)  # Adjusted based on input size after pooling
        self.fc2 = nn.Linear(512, 8)

    def forward(self, x):
        # Define the forward pass
        x = self.pool(F.relu(self.conv1(x)))
        x = self.pool(F.relu(self.conv2(x)))
        x = x.view(-1, 128 * 16 * 16)  # Adjusted based on input size after pooling
        x = F.relu(self.fc1(x))
        x = F.dropout(x, p=0.5, training=self.training)  # Dropout layer with 0.5 probability
        x = self.fc2(x)
        return F.log_softmax(x, dim=1)  # Log softmax for output layer