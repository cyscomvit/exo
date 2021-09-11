from exo.exocore import ExoCore

API_KEY = "" #Enzoic API Key here
SECRET_KEY = "" #Enzoic Secret Key here
exo = ExoCore(API_KEY, SECRET_KEY)

DecisionTreePredict, LogisticRegressionPredict, NaiveBayesPredict, NeuralNetworkPredict, status, count, score = exo.results("abc123")

print(DecisionTreePredict, LogisticRegressionPredict, NaiveBayesPredict, NeuralNetworkPredict, status, count, score)