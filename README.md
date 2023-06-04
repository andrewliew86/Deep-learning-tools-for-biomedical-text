# Classifying papers based on publication title
Background:
Researchers often struggle to organize publications into categories when performing literature searches. This is my attempt to create a basic automated publication title classifier. Specifically, I use the BioBERT model from HuggingFace to create a basic binary classifier that assigns publication into one of two categories: cancer or bacterial cell division.

Results:
I get decent accuracy and f1 scores (~0.98) but it will be important to perform more evalautions of the classifier with more training examples and a validation set.

Python libraries/tools: Standard Python libraries, transformers and PyTorch. 
