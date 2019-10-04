import torch.nn as nn


class DummyModel(nn.Module):
    def __init__(self, ):
        super().__init__()
        self.conv1 = nn.Conv2d(in_channels=3, out_channels=10,
                               kernel_size=3, padding=1, bias=False)
        self.relu = nn.ReLU(inplace=True)
        self.conv2 = nn.Conv2d(in_channels=10, out_channels=4,
                               kernel_size=3, padding=1, bias=False)
        self.final = nn.Sigmoid()

    def forward(self, inputs):
        x = self.relu(self.conv1(inputs))
        x = self.final(self.conv2(x))
        return x
