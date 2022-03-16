#!/usr/bin/env python
# coding: utf-8

# In[1]:


import bz2
import random
from tqdm import tqdm
from icecream import ic 
import torch


# In[2]:


WORD_EMBEDDING_FILE = 'dataset/sgns.weibo.word.bz2'


# In[3]:


token2embedding = {}


# ## readlines() 方法
# 用于读取所有行(直到结束符 EOF)并返回列表，该列表可以由 Python 的 for... in ... 结构进行处理。
# 
# 如果碰到结束符 EOF 则返回空字符串。

# In[4]:


with bz2.open(WORD_EMBEDDING_FILE) as f:
    token_vectors = f.readlines()
    vob_size, dim = token_vectors[0].split()


# In[5]:


print('load embedding file: {} end!'.format(WORD_EMBEDDING_FILE))


# In[6]:


token_vectors


# In[7]:


vob_size, dim


# ## 1.tqdm
# 有时候在使用Python处理比较耗时操作的时候，为了便于观察处理进度，这时候就需要通过进度条将处理情况进行可视化展示，以便我们能够及时了解情况。这对于第三方库非常丰富的Python来说，想要实现这一功能并不是什么难事。
# 
# tqdm就能非常完美的支持和解决这些问题，可以实时输出处理进度而且占用的CPU资源非常少，支持windows、Linux、mac等系统，支持循环处理、多进程、递归处理、还可以结合linux的命令来查看处理情况，等进度展示。
# 

# ## 2.assert（断言）用于判断一个表达式，在表达式条件为 false 的时候触发异常。
# 语法格式如下：
# 
# assert expression
# 等价于：
# 
# if not expression:
# 
#     raise AssertionError
# assert 后面也可以紧跟参数:
# 
# assert expression [, arguments]
# 等价于：
# 
# if not expression:
# 
#     raise AssertionError(arguments)
# 
# 实例：
# assert True     # 条件为 true 正常执行
# 
# assert False    # 条件为 false 触发异常
# 
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# AssertionError
#     
# assert 1==1    # 条件为 true 正常执行
#     
# assert 1==2    # 条件为 false 触发异常
#     
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# AssertionError

# ## 3.补全
# UNK: 低频词或未在词表中的词
#     
# PAD: 补全字符
#     
# GO/SOS: 句子起始标识符
#     
# EOS: 句子结束标识符
#     
# SEP：两个句子之间的分隔符

# In[8]:


def get_embedding(vocabulary: set):
    for line in tqdm(token_vectors[1:]):
        tokens = line.split()
        token = tokens[0].decode('utf-8')
        if token in vocabulary:
            token2embedding[token] = list(map(float,tokens[1:]))
            assert len(token2embedding[token]) == int(dim)
            
    UNK, PAD, BOS, EOS = '<unk> <pad> <bos> <eos>'.split()
    special_token_num = 4 
    token2id = {token: _id for _id, token in enumerate(token2embedding.keys(),special_token_num)}
    token2id[PAD] = 0
    token2id[UNK] = 1
    token2id[BOS] = 2
    token2id[EOS] = 3
    
    id2vec = {token2id[token]: embedding for token, embedding in token2embedding.items()}
    id2vec[0] = [0.] * int(dim)
    id2vec[1] = [0.] * int(dim)
    id2vec[2] = [random.uniform(-1, 1)] * int(dim)
    id2vec[3] = [random.uniform(-1, 1)] * int(dim)
    
    embedding = [id2vec[_id] for _id in range(len(id2vec))]
    #embedding 0,1,2,3,....,N
    
    return torch.tensor(embedding, dtype = torch.float), token2id, len(vocabulary)+4


# ## 函数定义中的 vocabulary ：set
# def f(text:str,max_len:'int>0'=80) ->str:
# 	
#     """这个是函数的帮助说明文档，help时会显示"""
#    
#    return True
# """
# 
# 函数声明中，text:str
# 
# text 是参数 :冒号后面  str是参数的注释。
# 
# 如果参数有默认值，还要给注释，如下写。
# 
# max_len:'int>0'=80
# 
# ->str 是函数返回值的注释。
# 
# 这些注释信息都是函数的元信息，保存在f.__annotations__字典中、
# 
# 需要注意，python对注释信息和f.__annotations__的一致性，不做检查
# 不做检查，不做强制，不做验证！什么都不做。
# """
# 

# In[9]:


def ttttest(ham: 42, eggs: int = 'spam') -> "Nothing to see here":
    print("函数注释", ttttest.__annotations__)
    print("参数值打印", ham, eggs)
    print(type(ham),type(eggs))


# In[10]:


ttttest('www')


# ## enumerate函数
# enumerate() 函数用于将一个可遍历的数据对象(如列表、元组或字符串)组合为一个索引序列，同时列出数据和数据下标，一般用在 for 循环当中。

# In[11]:


seasons = ['Spring', 'Summer', 'Fall', 'Winter']
print(enumerate(seasons))
list(enumerate(seasons))


# In[13]:


for _iiid, token in enumerate(seasons,5):
    print(_iiid,token)


# ### get_embedding函数中token2id测试

# In[14]:


test2id = {token: _iiid for _iiid, token in enumerate(seasons,5)}
test2id


# 其他测试

# In[15]:


a = {'name':1,'student':2}
a


# In[16]:


test1 = [0.] * int(4)
test1


# In[ ]:




