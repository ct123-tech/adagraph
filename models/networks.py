import torch
from models.resnet import resnet18_domain
from models.decaf import get_graph_net

model_urls = {
    'resnet18': 'https://download.pytorch.org/models/resnet18-5c106cde.pth',
    'alexnet': './alexnet_caffe/alexnet_caffe.pth.tar'
}



def load_pretrained(net,name):
	state = net.state_dict()
	state.update(torch.load(name)['state_dict'])
	net.load_state_dict(state)
	return net


def get_network(classes = 4, domains = 30, residual=False):
    if residual:
        return resnet18_domain(classes, domains, model_urls['resnet18'])
    return get_graph_net(classes, domains, model_urls['alexnet'])
