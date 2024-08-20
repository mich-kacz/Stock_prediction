import pickle
import torch
import pandas as pd
import numpy as np
from torch import nn
from sklearn.svm import SVR
from sklearn.multioutput import MultiOutputRegressor


class Predictor:
    def __init__(self, modelID, scaler = None) -> None:
        self.scaler = scaler
        self.modelID = modelID
        self.device = (
            "cuda"
            if torch.cuda.is_available()
            else "mps"
            if torch.backends.mps.is_available()
            else "cpu"
        )
        if (modelID=="SVR"):
            self.model = pickle.load(open("models/svr_params.pickle", "rb"))
            self.samplesForPrediction = 5
            self.samplesPredicted = 1
        elif(modelID == "LSTM"):
            self.samplesForPrediction = 15
            self.samplesPredicted = 1
            self.model = torch.jit.load('models/lstm.pt')
            self.model.to(self.device)
            self.model.eval()
        elif(modelID) == "CNN-LSTM":
            self.samplesForPrediction = 15
            self.samplesPredicted = 1
            self.model = torch.jit.load('models/cnn_lstm.pt')
            self.model.to(self.device)
            self.model.eval()
            
        elif(modelID) == "Transformer":
            pass
        else:
            Exception("Model not defined")

    def __call__(self, data : pd.DataFrame):
        trainX, trainY, dates, datesX = self._createSequence(data, data["Close"], self.samplesForPrediction, self.samplesPredicted)
        
        if (self.modelID == "SVR"):
            x = np.array(trainX)
            y = np.array(trainY)
            num_samples, num_days, num_features = x.shape
            x = x.reshape(num_samples, num_days * num_features)
            predictions = self.model.predict(x)
        else:
            x = torch.Tensor(trainX).to(self.device)
            y = torch.Tensor(trainY).to(self.device)
            predictions = self.model(x).cpu()
            predictions = predictions.detach().numpy()

        predictions, real = self._rescall(data, predictions)

        return predictions, real, dates, datesX

    def _createSequence(self, dataX, dataY, lengthX, predictionHorizont = 1):
        datesX = dataX.index[lengthX+1:].to_list()
        datesX.append("Next day")
        dates = dataX.index[lengthX+1:].to_list()
        xData = []
        yData = []
        for i in range(len(dataX) - lengthX):# - predictionHorizont):
            xData.append(dataX[i:i+lengthX].values)
            #yData.append(dataY[(lengthX + i):(lengthX + predictionHorizont + i)].values)
        return xData, yData, dates, datesX
    
    def _rescall(self, data, predictions):
        dummyDataset = data.tail(len(predictions))
        dummyDataset["Close"] = predictions
        dummyDataset = self.scaler.inverse_transform(dummyDataset)
        predictions = dummyDataset[:,3]

        dummyDataset = data.tail(len(predictions)-self.samplesPredicted)
        dummyDataset = self.scaler.inverse_transform(dummyDataset)
        real = dummyDataset[:,3]
        return predictions, real