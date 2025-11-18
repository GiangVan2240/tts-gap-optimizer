# Configuration Management

class Config:
    def __init__(self):
        self.settings = {
            'param1': 'value1',
            'param2': 'value2',
            'param3': 'value3',
        }

    def get(self, key):
        return self.settings.get(key, None)

    def set(self, key, value):
        self.settings[key] = value

# Example usage
config = Config()

# Set a value
config.set('param4', 'value4')

# Get a value
print(config.get('param1')) # Output: value1
