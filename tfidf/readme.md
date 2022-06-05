# 随机森林 and tfidf

*sklearn 的 TfidfVectorizer* 可以把原始文本内容变换为以 tf-idf 组成的特征矩阵，为后续的文本分类、计算文本相似度、主题模型等工作奠定基础；TfidfVectorizer 本质上是 CountVectorizer 词频计算类和 TfidfTransformer tf-idf 变换类的结合体。\
参数说明及属性说明详见:https://www.knowledgedict.com/tutorial/sklearn-tfidfvectorizer-parameters-and-attributes.html

TF-IDF算法介绍及实现:https://blog.csdn.net/asialee_bird/article/details/81486700
