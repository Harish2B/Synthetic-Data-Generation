"""In this module, we get the time series data to generate synthetic data. we collect the start time, end time, and time interval as user input.
from this string data we convert it into integer data and generate the data into a time series stamp data"""
from datetime import datetime, timedelta
class Time_Series_Generator:
    def __init__(self, start_time, end_time, time_interval):
        self.start_time = start_time
        self.end_time = end_time
        self.time_interval = time_interval

    def generate_time_series_data(self):
        # Convert input strings to datetime
        start_date = datetime.strptime(self.start_time, '%d-%m-%Y %H:%M:%S')
        end_date = datetime.strptime(self.end_time, '%d-%m-%Y %H:%M:%S')

        # Check if the inputs are proper
        self.time_interval = int(self.time_interval)
        if self.time_interval <= 0:
            raise ValueError("Time interval must be a positive integer.")
        if start_date >= end_date:
            raise ValueError("Start date must be before end date.")

        # Generate the time series data
        delta = timedelta(minutes=self.time_interval)
        output= []
        while start_date <= end_date:
            output.append(start_date.strftime('%d-%m-%Y %H:%M:%S'))
            start_date += delta

        return output
