"""
In this module, we are visualising the relationship between the attributes which are generated with a relationship using a scatterplot.
"""
import matplotlib.pyplot as plt
from statsmodels.tsa.statespace.sarimax import SARIMAX
import pandas as pd

class DataVisualizer:
    def __init__(self, data, relationships):
        self.data = data
        self.relationships = relationships

    # Visualizing the data with scatter plot
    def visualize_relationships(self):
        # Scatter plot for each relationship
        for i, relationship in enumerate(self.relationships):
            dependent_attr = relationship['dependent']
            independent_attr = relationship['independent'][0]
            relationship_type = relationship['type'].upper()
            plt.figure(figsize=(15, 6))
            plt.scatter(x=self.data[independent_attr], y=self.data[dependent_attr],
                        label=f"{independent_attr} vs {dependent_attr}", color='green')
            plt.xlabel(f'INDEPENDENT ATTRIBUTE {independent_attr}')
            plt.ylabel(f'DEPENDENT ATTRIBUTE {dependent_attr}')
            plt.title(f'{relationship_type} RELATIONSHIPS BETWEEN ATTRIBUTE {independent_attr} AND {dependent_attr}')
            plt.legend()
            plt.savefig(f'{relationship_type}for{independent_attr}&{dependent_attr}.png')  # Save the plot before showing it
            plt.show()

            # Plot the synthetic data
            plt.figure(figsize=(10, 6))
            plt.scatter(self.data.index, self.data[dependent_attr])
            plt.title('Synthetic Data Over Time')
            plt.xlabel('Time')
            plt.ylabel('Value')
            plt.show()

            # Plot the synthetic data
            plt.figure(figsize=(10, 6))
            plt.scatter(self.data.index, self.data[independent_attr])
            plt.title('Independent Synthetic Data Over Time')
            plt.xlabel('Time')
            plt.ylabel('Value')
            plt.show()
            
            # Fit the SARIMAX model
            model = SARIMAX(self.data[dependent_attr], order=(1,1,1), seasonal_order=(1,1,1,12))
            results = model.fit()
            
            # Plot the original data and the fitted values
            plt.figure(figsize=(10, 6))
            plt.plot(self.data[dependent_attr], label='Original Data')
            plt.plot(results.fittedvalues, label='Fitted Values')
            plt.title('SARIMAX Model')
            plt.xlabel('Time')
            plt.ylabel('Value')
            plt.legend()
            plt.show()

            # Plot the residuals
            residuals = pd.DataFrame(results.resid)
            plt.figure(figsize=(10, 6))
            plt.plot(residuals)
            plt.title('Residuals')
            plt.xlabel('Time')
            plt.ylabel('Value')
            plt.show()
