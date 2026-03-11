import pickle
import numpy as np

class Insurance_Prediction:
    def __init__(self):
        # Load the scaler
        with open("artifacts/scaler.pkl", "rb") as f:
            self.scaler = pickle.load(f)
        
        # Load the model
        with open("artifacts/model.pkl", "rb") as f:
            self.model = pickle.load(f)

    def prediction(self, Age, Annual_Income_LPA, Policy_Term_Years, Sum_Assured_Lakhs):
        # Make input a 2D array
        input_data = np.array([[Age, Annual_Income_LPA, Policy_Term_Years, Sum_Assured_Lakhs]])
        
        # Scale the input
        scaled_input = self.scaler.transform(input_data)
        
        # Predict
        result = self.model.predict(scaled_input)
        return result[0]