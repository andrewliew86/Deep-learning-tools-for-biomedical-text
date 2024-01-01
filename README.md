# Fine-tuning open source deep learning models 
Background:
Researchers often struggle to organize publications into categories when performing literature searches. They are also often tasked with finding relevant answers from abstracts based on questions they might have (e.g is COVID-19 severity affected by antibody status). This is my attempt at creating an automated publication title classifier and a question answering model. Specifically, I fine-tune pretrained BERT models from HuggingFace to create: 
- binary classifier that assigns publication into one of two categories (cancer or bacterial cell division) 
- Q and A model that extract answers to COVID-19 related questions from a provided context (paper abstract) 

Results:
- I get decent accuracy and f1 scores (~0.98) but it will be important to perform more evaluations of the classifier with more training examples and a validation set.
- I also get decent results with the extractive Q and A model

Python libraries/tools: Standard Python libraries (Pandas, NumPy etc...), 🤗 transformers, weights and biases and PyTorch. 
