import torch
from torch import nn

class SPP(nn.Module):
    def __init__(self):
        super().__init__()
        self.maxpool1=nn.MaxPool2d(kernel_size=5,stride=1,padding=2)
        self.maxpool2=nn.MaxPool2d(kernel_size=9,stride=1,padding=4)
        self.maxpool3=nn.MaxPool2d(kernel_size=13,stride=1,padding=6)

    def forward(self,input):
        output1=self.maxpool1(input)
        output2=self.maxpool2(input)
        output3=self.maxpool3(input)
        output4=torch.cat((output1,output2,output3,input),dim=1)
        return output4

class SPPF(nn.Module):
    def __init__(self):
        super().__init__()
        self.maxpool=nn.MaxPool2d(kernel_size=5,stride=1,padding=2)

    def forward(self,input):
        output1=self.maxpool(input)
        output2=self.maxpool(output1)
        output3=self.maxpool(output2)
        output4=torch.cat((output1,output2,output3,input),dim=1)
        return output4

spp=SPP()
input=torch.randn(8,32,16,16)
output=spp(input)

sppf=SPPF()
output=sppf(input)