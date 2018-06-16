
# coding: utf-8

# In[3]:


import torch.nn as nn
import math
from torch.nn import functional as F
from torch.utils import model_zoo


# In[37]:


class vgg(nn.Module):
    
    def __init__(self,batch_norm = False):
        super(vgg,self).__init__()
        self.layers = []
        self.batch_norm = batch_norm
        self.layers += self.layer(3,64)
        self.layers += self.layer(64,64)
        self.layers += [nn.MaxPool2d(kernel_size = 2, stride = 2)]
        self.layers += self.layer(64,128)
        self.layers += self.layer(128,128)
        self.layers += [nn.MaxPool2d(kernel_size = 2, stride = 2)]
        self.layers += self.layer(128,256)
        self.layers += self.layer(256,256)
        self.layers += self.layer(256,256)
        self.layers += [nn.MaxPool2d(kernel_size = 2, stride = 2)]
        self.layers += self.layer(256,512)
        self.layers += self.layer(512,512)
        self.layers += self.layer(512,512)
        self.layers += [nn.MaxPool2d(kernel_size = 2, stride = 2)]
        self.layers += self.layer(512,512)
        self.layers += self.layer(512,512)
        self.layers += self.layer(512,512)
        self.layers += [nn.MaxPool2d(kernel_size = 2, stride = 2)]
#         print(self.layers)
        self.features = nn.Sequential(*self.layers)
        self.classifier = nn.Sequential(
            nn.Linear(512 * 7 * 7, 4096),
            nn.ReLU(True),
            nn.Dropout(),
            nn.Linear(4096, 4096),
            nn.ReLU(True),
            nn.Dropout(),
            nn.Linear(4096, 1000)
        )
    
    def layer(self,input_channels, kernels):
        if self.batch_norm:
            return [nn.Conv2d(input_channels,kernels,kernel_size = 3,padding = 1),nn.BatchNorm2d(kernels), nn.ReLU(inplace = True)]
        else:
            return [nn.Conv2d(input_channels,kernels,kernel_size = 3,padding = 1), nn.ReLU(inplace = True)]
        
    def forward(self,x):
        x = self.features(x)
        x = x.view(x.size(0), -1)
        x = self.classifier(x)
        x = F.sigmoid(x) 
        x = x.view(-1,7,7,30)
        return x

# def make_net(



