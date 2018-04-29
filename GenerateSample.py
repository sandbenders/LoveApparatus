from trainNeuralNetwork.charRNN_local.model import load_model, sample

class GenerateSample:
    def __init__(self):
        super().__init__()

    def get_sample(self, checkpoint='../trainedModel/charRNN_1.4856_1.2345_bo.ckpt', gpu=True, samples=1000, seed='love', top=10):
        net = load_model(checkpoint)
        return sample(net, samples, cuda=gpu, top_k=top, prime=seed)