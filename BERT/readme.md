# BERT

*参考论文:*\
BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding, 	arXiv:1810.04805\
The code and pre-trained models are available at https://github.com/google-research/bert.


### trick:
NoisyTune: A Little Noise Can Help You Finetune Pretrained Language Models Better \
https://aclanthology.org/2022.acl-short.76.pdf 
```
noise_lambda = 0.5
for name, para in model.named_parameters():
	  model.state_dict()[name][:] += (torch.rand(para.size()).to(config['device'])-0.5) * noise_lambda * torch.std(para).to(config['device'])
```
