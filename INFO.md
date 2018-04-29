`pyuic5 loveApparatusInterface.ui -o ../loveApparatusInterface.py`<br />
`nltk.download('punkt')`<br />
`nltk.download('averaged_perceptron_tagger')`<br />
`nltk.download('wordnet')`<br />
`python sample.py '/home/fpoltronieri/PycharmProjects/loveapparatus/trainNeuralNetwork/trainedModel/charRNN_1.4856_1.2345_bo.ckpt' --num_samples 1000 --gpu --prime "We love the things we love for what they are."`<br />
`python train.py --in_file '/home/fpoltronieri/PycharmProjects/loveapparatus/trainNeuralNetwork/trainDatasets/train.txt' --save_dir '/home/fpoltronieri/PycharmProjects/loveapparatus/trainNeuralNetwork/trainedModel' --rnn_size 512 --num_layers 3 --gpu --num_epochs 25` <br />


