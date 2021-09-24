import joblib as joblib
import os
import hashlib
import requests
import json
import base64
import pkg_resources

class ExoCore:
    def __init__(self, apiKey, secretKey):
        self.DecisionTree = pkg_resources.resource_stream(__name__, 'DecisionTree_Model.joblib')
        self.LogisticRegression = pkg_resources.resource_stream(__name__, 'LogisticRegression_Model.joblib')
        self.NaiveBayes = pkg_resources.resource_stream(__name__, 'NaiveBayes_Model.joblib')
        self.NeuralNetwork = pkg_resources.resource_stream(__name__, 'NeuralNetwork_Model.joblib')
        
        self.DecisionTree_Model = joblib.load(self.DecisionTree)
        self.LogisticRegression_Model = joblib.load(self.LogisticRegression)
        self.NaiveBayes_Model = joblib.load(self.NaiveBayes)
        self.NeuralNetwork_Model = joblib.load(self.NeuralNetwork)
        self.apiKey = apiKey
        self.secretKey = secretKey
        
    def callEnzoicAPI(self, password):
        apiKey = self.apiKey
        secretKey = self.secretKey
        authorizationParameter = apiKey+":"+secretKey
        authorizationParameter = authorizationParameter.encode('ascii')
        authorizationParameter = (base64.b64encode(authorizationParameter)).decode('ascii')
        authorizationParameter = "basic "+str(authorizationParameter)
        password = password.encode('utf-8')
        sha1HashTemp = hashlib.sha1(password)
        sha1Hash = str(sha1HashTemp.hexdigest())
        sha256HashTemp = hashlib.sha256(password)
        sha256Hash = str(sha256HashTemp.hexdigest())
        md5HashTemp = hashlib.md5(password)
        md5Hash = str(md5HashTemp.hexdigest())
        rawData = {'partialSHA1':sha1Hash, 'partialSHA256':sha256Hash, 'partialMD5':md5Hash}
        url = 'https://api.enzoic.com/passwords'
        response = requests.post(url, data = json.dumps(rawData),headers={'content-type':'application/json',
        'authorization':authorizationParameter})
        if(response.status_code == 404):
            print("Not found")
            return (False,0)
        finalResponse = json.loads(response.content.decode('ascii'))
        return (finalResponse["candidates"][0]["revealedInExposure"], finalResponse["candidates"][0]["exposureCount"])
    
    def scoreCalculate(self, password):
        length = len(password)
        score = 0
        upper = 0
        lower = 0
        numbers = 0
        symbols = 0
        consecutiveLower = 0
        consecutiveUpper = 0
        consecutiveNumber = 0
        for i in range(0,length-1):
            if(password[i].isupper()):
                upper += 1
            elif(password[i].islower()):
                lower += 1
            elif(password[i].isdigit()):
                numbers += 1
            else:
                symbols += 1

            if(password[i].isupper() and password[i+1].isupper()):
                consecutiveUpper += 1
            else:
                score = score-consecutiveUpper*2
                consecutiveUpper = 0
            if(password[i].islower() and password[i+1].islower()):
                consecutiveLower += 1
            else:
                score = score-consecutiveLower*2
                consecutiveLower = 0
            if(password[i].isdigit() and password[i+1].isdigit()):
                consecutiveNumber += 1
            else:
                score = score-consecutiveNumber*2
                consecutiveNumber = 0


        score = score + length*4+((length-lower)*2)+((length-upper)*2)+(numbers*4)+symbols*6

        if(numbers==0 and symbols==0):
            score = score - length

        if(upper==0 and lower==0 and symbols==0):
            score = score - length

        return score
    
    def results(self, password):
        transformedPassword = [password]

        DecisionTreePredict = self.DecisionTree_Model.predict(transformedPassword)
        LogisticRegressionPredict = self.LogisticRegression_Model.predict(transformedPassword)
        NaiveBayesPredict = self.NaiveBayes_Model.predict(transformedPassword)
        NeuralNetworkPredict = self.NeuralNetwork_Model.predict(transformedPassword)
        status, count = self.callEnzoicAPI(password)
        score = self.scoreCalculate(password)
        
        response = {0: "Weak", 1: "Moderate", 2: "Strong"}
        
        result = {"password": password, "score": score, "DecisionTree": {"score": DecisionTreePredict[0], "response": response[DecisionTreePredict[0]]}, "LogisticRegression": {"score": LogisticRegressionPredict[0], "response": response[LogisticRegressionPredict[0]]}, "NaiveBayes": {"score": NaiveBayesPredict[0], "response": response[NaiveBayesPredict[0]]}, "NeuralNetwork": {"score": NeuralNetworkPredict[0], "response": response[NeuralNetworkPredict[0]]}, "Breached": status, "BreachCount": count}
        
        return result

