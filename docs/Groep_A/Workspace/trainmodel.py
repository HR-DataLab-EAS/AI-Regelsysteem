import torch
import torch.nn.functional as F
import torch.nn as nn
import torch.optim as optim
import scipy.io
import pandas as pd
import numpy as np
from scipy.optimize import minimize
import matplotlib.pyplot as plt
import time

train_losses = []
test_losses = []

class TorchNeuralNetwork(nn.Module):
    def __init__(self, input_layer_size, hidden_layer_size, output_layer_size):
        super(TorchNeuralNetwork, self).__init__()
        self.fc1 = nn.Linear(input_layer_size, hidden_layer_size)
        self.fc2 = nn.Linear(hidden_layer_size, output_layer_size)

    def forward(self, x):
        x = torch.sigmoid(self.fc1(x))
        x = torch.sigmoid(self.fc2(x))  # of softmax bij multi-class classificatie
        return x
    
    
def train_model(X, y, input_layer_size, hidden_layer_size, output_layer_size, lamb=0.0, lr=0.1, epochs=1000):
    # Tensors
    X = torch.tensor(X, dtype=torch.float32)
    y = torch.tensor(y, dtype=torch.long)  # class labels

    # Model + optimizer
    model = TorchNeuralNetwork(input_layer_size, hidden_layer_size, output_layer_size)
    optimizer = optim.Adam(model.parameters(), lr=lr)

    # Loss functie
    criterion = nn.CrossEntropyLoss()
    


    for epoch in range(epochs):
        model.train()
        optimizer.zero_grad()
        output = model(X)                    # Forward pass
        loss = criterion(output, y)          # Cross-entropy loss

        # L2 regularisatie (optioneel)
        if lamb > 0:
            l2_reg = 0
            for param in model.parameters():
                for param in model.parameters():
                    l2_reg += torch.sum(param[:, 1:] ** 2) if param.ndim == 2 else 0
            loss += (lamb / (2 * len(X))) * l2_reg

        loss.backward()
        optimizer.step()
        train_losses.append(loss.item())
        
        # ➕ Test loss meten
        model.eval()
        with torch.no_grad():
            test_output = model(X_test_tensor)
            test_loss = criterion(test_output, Y_test_tensor)
            test_losses.append(test_loss.item())


        if epoch % 100 == 0:
            print(f"Epoch {epoch}: Loss = {loss.item()}")
            print(f"Epoch {epoch}: Train Loss = {loss.item()}, Test Loss = {test_loss.item()}")

    return model

csv_path = '/Users/mitchelreints/Documents/Visuel Studio Code/Workspace [Python]/#AIregelsysteem/simulatie_resultaten_2025-03-04_12-48-39.csv'
CSV_data = pd.read_csv(csv_path)

x = CSV_data[["Doel Hoogte (m)", "Daadwerkelijke Hoogte (m)"]] / 1
x["Doel Hoogte (m)"] = x["Doel Hoogte (m)"] / 1
x["Daadwerkelijke Hoogte (m)"] = x["Daadwerkelijke Hoogte (m)"] / 1
x = x.to_numpy()

Y = CSV_data["PWM (%)"]

Y = Y.to_numpy()


X_train = x[:500, :] #pakt de eerste 60.000 rijen van de array x
Y_train = Y[:500] #pakt de eerste 60.000 rijen van de array Y
X_test = x[500:, :] #pakt de laatste 60.000 rijen van de array x
Y_test = Y[500:] #pakt de laatste 60.000 rijen van de array Y
m = x.shape[0] #aantal rijen van de array x

input_layer_size = 2  #Setpoints + Sample huidige hoogte + vorige Sample (N-1) + (N-2) + (N-3) + (N-...)
hidden_layer_size = 100
output_layer_size = 101 # 0 - 100 

start_time = time.time()
model = train_model(X_train, Y_train,
                    input_layer_size,
                    hidden_layer_size,
                    output_layer_size,
                    lamb=1.0,
                    lr=0.1,
                    epochs=1000)

end_time = time.time()
print(f"Training time: {end_time - start_time:.2f} seconds")
X_test_tensor = torch.tensor(X_test, dtype=torch.float32)
Y_test_tensor = torch.tensor(Y_test, dtype=torch.long)

def evaluate_model(model, X_tensor, Y_tensor, name="Set"):
    model.eval()
    with torch.no_grad():
        predictions = model(X_tensor)
        predicted_classes = torch.argmax(predictions, 1)

        correct = (predicted_classes == Y_tensor).sum().item()
        total = Y_tensor.size(0)
        accuracy = correct / total * 100

        # Precision berekening (voor classificatie: TP / (TP + FP))
        true_positive = ((predicted_classes == Y_tensor) & (Y_tensor == predicted_classes)).sum().item()
        false_positive = ((predicted_classes != Y_tensor) & (Y_tensor != predicted_classes)).sum().item()
        precision = true_positive / (true_positive + false_positive) if (true_positive + false_positive) > 0 else 0.0

        print(f"{name} Accuracy: {accuracy:.2f}%")
        print(f"{name} Precision: {precision:.4f}")

        return accuracy, precision

# Test set
X_test_tensor = torch.tensor(X_test, dtype=torch.float32)
Y_test_tensor = torch.tensor(Y_test, dtype=torch.long)
evaluate_model(model, X_test_tensor, Y_test_tensor, name="Test")

# Training set
X_train_tensor = torch.tensor(X_train, dtype=torch.float32)
Y_train_tensor = torch.tensor(Y_train, dtype=torch.long)
evaluate_model(model, X_train_tensor, Y_train_tensor, name="Train")

# Plot train vs test loss
plt.figure()
plt.plot(train_losses, label="Train Loss")
plt.plot(test_losses, label="Test Loss")
plt.xlabel("Epoch")
plt.ylabel("Loss")
plt.legend()
plt.title("Train vs Test Loss")
plt.show(block=False)


# Opslaan van gewichten in een tekstbestand
with open("/Users/mitchelreints/Documents/Visuel Studio Code/Workspace [Python]/#AIregelsysteem/model_gewichten.txt", "w") as f:
    for name, param in model.named_parameters():
        f.write(f"{name}:\n")
        f.write(f"{param.data.numpy()}\n\n")
