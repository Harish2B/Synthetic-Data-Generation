class SmoothingFunction:
    def __init__(self, smoothing_percentage):
        self.smoothing_percentage = smoothing_percentage

    def smooth(self, data):
        if self.smoothing_percentage == 0:
            return data
        elif self.smoothing_percentage == 1:
            return [data.mean()] * len(data)
        else:
            smoothed_data = []
            for i in range(len(data)):
                if i == 0:
                    smoothed_data.append(data[i])
                else:
                    smoothed_data.append((1 - self.smoothing_percentage) * data[i] + self.smoothing_percentage * smoothed_data[i-1])

            return smoothed_data
