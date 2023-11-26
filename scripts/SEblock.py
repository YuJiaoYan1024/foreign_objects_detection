import torch
import torch.nn as nn

class SE_Block(nn.Module):
    def __init__(self,inchannel=64,ratio=16):
        super(SE_Block, self).__init__()
        self.gap=nn.AdaptiveAvgPool2d((1,1))
        self.fc=nn.Sequential(
            nn.Linear(inchannel,inchannel//ratio),
            nn.ReLU(),
            nn.Linear(inchannel // ratio, inchannel),
            nn.Sigmoid()
        )

    def forward(self,x):
        b, c, h, w = x.size()
        y=self.gap(x).view(b,c)
        y=self.fc(y).view(b,c,1,1)
        y=y.expand_as(x)
        return x*y


input=torch.randn((1,64,224,224))
se_block=SE_Block()
output=se_block(input)
print(output.shape)