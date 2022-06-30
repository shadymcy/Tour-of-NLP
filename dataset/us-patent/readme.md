## us-patent-phrase-to-phrase-matching数据集

1.**Score meanings**\
The scores are in the 0-1 range with increments of 0.25 with the following meanings:
  - 1.0 - Very close match. This is typically an exact match except possibly for differences in conjugation, quantity (e.g. singular vs. plural), and addition or removal of stopwords (e.g. “the”, “and”, “or”).
  - 0.75 - Close synonym, e.g. “mobile phone” vs. “cellphone”. This also includes abbreviations, e.g. "TCP" -> "transmission control protocol".
  - 0.5 - Synonyms which don’t have the same meaning (same function, same properties). This includes broad-narrow (hyponym) and narrow-broad (hypernym) matches.
  - 0.25 - Somewhat related, e.g. the two phrases are in the same high level domain but are not synonyms. This also includes antonyms.
  - 0.0 - Unrelated.

2.**Files**
  - train.csv - the training set, containing phrases, contexts, and their similarity scores
  - test.csv - the test set set, identical in structure to the training set but without the score
  - sample_submission.csv - a sample submission file in the correct format

3.**Columns**
  - id - a unique identifier for a pair of phrases
  - anchor - the first phrase
  - target - the second phrase
  - context - the CPC classification (version 2021.05), which indicates the subject within which the similarity is to be scored
  - score - the similarity. This is sourced from a combination of one or more manual expert ratings.
