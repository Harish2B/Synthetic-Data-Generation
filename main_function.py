"""
this is a code to GENERATE SYNTHETIC DATA using a few inputs from the user. the functions in this program is explained below:
time series generator class calls the start time,end time and time interval which is a user input to create time stamp data.
constraint calculator calls the range constraints set by the user for each attribute.
synthetic data generation calls the random value generator function to substitute the constraints for the attribute and generate random values
relationship generator and apply relationship class calls the user input for dependent attribute,independent attribute adn the type of relationship and generates the random values based on it
datanoiser is the class which calls for the noise percentage and outlier percentage for the data which creates a realistic synthetic data
datavisualizer class plots the synthetic data which has been created with the relationship and added noise and outliers.
"""
import configparser
import pandas as pd
from Time_Series_Generator import Time_Series_Generator
from synthetic_data_generation import synthetic_data_generation
from apply_relationship import apply_relationship
from DataNoiser import DataNoiser
from Datavisualizer import DataVisualizer
from temporal_pattern import TemporalPatternGenerator
from seasonality import SeasonalPatternGenerator

class SyntheticDataGenerator:
    def __init__(self, config):
        self.config = config

    def get_attributes(self):
        return [attr.strip() for attr in self.config['Attributes'].values()]

    def get_constraints(self):
        constraints = {}
        for key, value in self.config['Constraints'].items():
            attr, constraint_info = value.split(':')
            min_val, max_val, seasonality, temporal_pattern, amplitude = constraint_info.split(',')
            constraints[attr] = {
                'min': float(min_val),
                'max': float(max_val),
                'seasonality': seasonality.strip(),
                'temporal_pattern': temporal_pattern.strip(),
                'amplitude': float(amplitude.strip())  # Store amplitude as well
            }
        return constraints

    def get_time_series_data(self):
        start_time = self.config['Time Series']['start_time']
        end_time = self.config['Time Series']['end_time']
        time_interval = self.config['Time Series']['time_interval']

        if 'hour' in time_interval:
            value, unit = time_interval.split()
            time_interval = int(float(value) * 60)
        elif 'min' in time_interval:
            value, unit = time_interval.split()
            time_interval = int(value)
        else:
            raise ValueError("Invalid time interval format. It should be in 'X hour' or 'X min' format.")

        time_series_generator = Time_Series_Generator(start_time, end_time, time_interval)
        return time_series_generator.generate_time_series_data()

    def get_relationships(self):
        relationships = []
        for key in self.config['Relationships']:
            rel_str = self.config['Relationships'][key]
            rel_type, rel_eq = rel_str.split(':')
            rel_eq = rel_eq.split(',')
            relationships.append(
                {'type': rel_type.strip(), 'dependent': rel_eq[0].strip(), 'independent': [rel_eq[1].strip()]})
        return relationships

    def generate_synthetic_data(self):
        attributes = self.get_attributes()
        constraints = self.get_constraints()
        time_series_data = self.get_time_series_data()
        num_records = len(time_series_data)
        relationships = self.get_relationships()

        # Generate synthetic data with constraints
        synthetic_data = synthetic_data_generation(attributes, num_records, constraints)
        synthetic_data = synthetic_data.synthetic_data_generator()

        # Apply relationships to the generated data
        apply_relationship_formula = apply_relationship(synthetic_data, relationships, constraints)
        synthetic_data = apply_relationship_formula.apply_relationships()

        # Apply temporal pattern and seasonality to the synthetic data
        for i, attr in enumerate(attributes):
            trend_type = constraints[attr]['temporal_pattern']
            trend_value = constraints[attr]['amplitude']
            seasonality_type = constraints[attr]['seasonality']
            min_val=constraints[attr]['min']
            max_val=constraints[attr]['max']

            # Call the temporal pattern function to add temporal characteristics
            temporal_pattern_generator = TemporalPatternGenerator(num_records, trend_type, trend_value,min_val,max_val)
            temporal_pattern = temporal_pattern_generator.generate_temporal_pattern()

            # Call the seasonality function to add seasonal characteristics
            seasonal_pattern_generator = SeasonalPatternGenerator(num_records, seasonality_type,min_val,max_val)
            seasonal_pattern = seasonal_pattern_generator.generate_seasonal_pattern()

            # Apply temporal pattern and seasonality to the attribute
            synthetic_data[attr] = synthetic_data[attr] +temporal_pattern + seasonal_pattern

        # Create a DataFrame from the synthetic data
        df = pd.DataFrame(synthetic_data)

        # Add timestamp to the DataFrame
        df['Time stamp'] = time_series_data
        df.set_index('Time stamp', inplace=True)
        return df

    def add_noise_and_outliers(self, df):
        noise_level = float(self.config['Noise']['noise_level'])
        outlier_proportion = float(self.config['Noise']['outlier_proportion'])
        outlier_magnitude = float(self.config['Noise']['outlier_magnitude'])

        noiser = DataNoiser(df)
        noiser.add_noise(noise_level)
        noiser.add_outliers(outlier_proportion, outlier_magnitude)

        return noiser.data

    @staticmethod
    def visualize_relationships(df, relationships):
        visualizer = DataVisualizer(df, relationships)
        visualizer.visualize_relationships()

def main(config):
    # Initialize the SyntheticDataGenerator class
    generator = SyntheticDataGenerator(config)

    # Generate synthetic data based on user inputs from the config file
    df = generator.generate_synthetic_data()

    # Add noise and outliers to the synthetic data
    df = generator.add_noise_and_outliers(df)

    # Visualize relationships in the data
    generator.visualize_relationships(df, generator.get_relationships())

    # Save DataFrame to Excel file
    df.to_excel('output.xlsx', index=True)
if __name__ == "__main__":
    config = configparser.ConfigParser()
    config.read('config.ini')
    main(config)
