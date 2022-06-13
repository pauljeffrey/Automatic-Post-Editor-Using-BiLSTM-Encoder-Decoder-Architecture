# Automatic-Post-Editor-Using-BiLSTM-Encoder-Decoder-Architecture

# INTRODUCTION
The APE model is a research based custom model developed from scratch in TensorFlow. It was trained to make edits and corrections to output result made by state of the art and trained Neural Machine Translation Systems. Subsequently, I use an online learning method (one training data at a time) to train a copy of this model and then compare its performance with the model trained using batch training method.

it was trained on the following datasets creating 3 different models:

- English to Spanish
- English to Chinese
- German to English.

## INPUT
It takes the text to be translated and the translated text by a neural machine translator model as input.

## OUTPUT
It returns a corrected or edited translation of the previous translation made by the neural machine translator.

## METHOD
It uses a Bi-LSTM as encoder to encode both inputs and uses a decoder with attention to attend to the encoded input to produce a corrected or improved translation originally made by the former neural machine translator.

## EVALUATION
it was evaluated using a TER score that takes into account the number of deletions, insertions, substitutions and rearrangement made by the trained model.

For more info, go through the .ipynb jupyter notebook for code, training and indepth explanation.
