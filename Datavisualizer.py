"""
In this module, we are visualising the relationship between the attributes which are generated with a relationship using a scatterplot.
"""
import matplotlib.pyplot as plt
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf
from scipy.signal import welch

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
            '''plt.figure(figsize=(10, 6))
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

            # Plot the autocorrelation function (ACF)
            plt.figure(figsize=(10, 6))
            plot_acf(self.data[dependent_attr], lags=30)
            plt.title('Autocorrelation Function (ACF)')
            plt.xlabel('Lag')
            plt.ylabel('Correlation')
            plt.show()

            # Plot the partial autocorrelation function (PACF)
            plt.figure(figsize=(10, 6))
            plot_pacf(self.data[dependent_attr], lags=30)
            plt.title('Partial Autocorrelation Function (PACF)')
            plt.xlabel('Lag')
            plt.ylabel('Correlation')
            plt.show()

            # Plot the spectral density
            freqs, psd = welch(self.data[dependent_attr])
            plt.figure(figsize=(10, 6))
            plt.plot(freqs, psd)
            plt.title('Spectral Density')
            plt.xlabel('Frequency')
            plt.ylabel('Power')
            plt.show()'''
