
# coding: utf-8

# In[1]:


vgg16_batch_norm_url = 'https://download.pytorch.org/models/vgg16_bn-6c64b313.pth'
vgg16_url  = 'https://download.pytorch.org/models/vgg16-397923af.pth'


# In[2]:


learning_rate = 0.001
num_epochs = 100
batch_size = 32
momentum = 0.9
weight_decay = 5e-4
VOC_CLASSES = ('aeroplane', 'bicycle', 'bird', 'boat',
    'bottle', 'bus', 'car', 'cat', 'chair',
    'cow', 'diningtable', 'dog', 'horse',
    'motorbike', 'person', 'pottedplant',
    'sheep', 'sofa', 'train', 'tvmonitor')
confidence_threshold = 0.9
path_images_2012 = 'VOC_Datasets/VOC_2012_training/VOC2012/JPEGImages/'
path_text_2012 = 'voc2012train.txt'
path_images_2007 = 'VOC_Datasets/VOC_2007_testing/VOCdevkit/VOC2007/JPEGImages/'
path_text_2007 = 'voc2007test.txt'
cells_per_row = 7
cell_size = 1./cells_per_row
