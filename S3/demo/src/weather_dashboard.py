import os
import json
import boto3
import requests
from datetime import datetime
import random
import string

class WeatherDashboard:
    def __init__(self):
        # OpenWeather API key
        self.api_key = 'XXXXXXXX563599449255292'
        
        # AWS credentials (hardcoded or from environment variables)
        self.aws_access_key_id = 'XXXXXXXX535EY'  
        self.aws_secret_access_key = 'XXXXXXXXXXXXXXL13R+rjYbe/OD4b+K'  
        self.aws_region = 'us-east-1' 

        self.bucket_name = 'weather-dashboard-' + self.generate_random_string()
        
        # Initialize S3 client with explicit credentials
        self.s3_client = boto3.client(
            's3',
            aws_access_key_id=self.aws_access_key_id,
            aws_secret_access_key=self.aws_secret_access_key,
            region_name=self.aws_region
        )
        
        # Initialize STS client
        self.sts_client = boto3.client(
            'sts',
            aws_access_key_id=self.aws_access_key_id,
            aws_secret_access_key=self.aws_secret_access_key,
            region_name=self.aws_region
        )

    def generate_random_string(self, length=8):
        """Generate a random alphanumeric string of the specified length."""
        return ''.join(random.choices(string.ascii_lowercase + string.digits, k=length))

    def create_bucket_if_not_exists(self):
        """Create S3 bucket if it doesn't exist"""
        try:
            self.s3_client.head_bucket(Bucket=self.bucket_name)
            print(f"Bucket {self.bucket_name} already exists.")
        except:
            print(f"Creating bucket {self.bucket_name}")
            try:
                if self.aws_region == 'us-east-1':
                    self.s3_client.create_bucket(Bucket=self.bucket_name)
                else:
                    self.s3_client.create_bucket(
                        Bucket=self.bucket_name,
                        CreateBucketConfiguration={'LocationConstraint': self.aws_region}
                    )
                print(f"Bucket {self.bucket_name} created successfully.")
            except Exception as e:
                print(f"Error creating bucket: {e}")

    def fetch_weather(self, city):
        """Fetch weather data from OpenWeather API"""
        base_url = "http://api.openweathermap.org/data/2.5/weather"
        params = {
            "q": city,
            "appid": self.api_key,
            "units": "imperial"
        }
        
        try:
            response = requests.get(base_url, params=params)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"Error fetching weather data: {e}")
            return None

    def save_to_s3(self, weather_data, city):
        """Save weather data to S3 bucket"""
        if not weather_data:
            return False
            
        timestamp = datetime.now().strftime('%Y%m%d-%H%M%S')
        file_name = f"weather-data/{city}-{timestamp}.json"
        
        try:
            weather_data['timestamp'] = timestamp
            self.s3_client.put_object(
                Bucket=self.bucket_name,
                Key=file_name,
                Body=json.dumps(weather_data),
                ContentType='application/json'
            )
            print(f"Successfully saved data for {city} to S3.")
            return True
        except Exception as e:
            print(f"Error saving to S3: {e}")
            return False


def main():
    dashboard = WeatherDashboard()
    
    # Create bucket if needed
    dashboard.create_bucket_if_not_exists()
    
    cities = ["Philadelphia", "Seattle", "New York"]
    
    for city in cities:
        print(f"\nFetching weather for {city}...")
        weather_data = dashboard.fetch_weather(city)
        if weather_data:
            temp = weather_data['main']['temp']
            feels_like = weather_data['main']['feels_like']
            humidity = weather_data['main']['humidity']
            description = weather_data['weather'][0]['description']
            
            print(f"Temperature: {temp}°F")
            print(f"Feels like: {feels_like}°F")
            print(f"Humidity: {humidity}%")
            print(f"Conditions: {description}")
            
            # Save to S3
            success = dashboard.save_to_s3(weather_data, city)
            if success:
                print(f"Weather data for {city} saved to S3!")
        else:
            print(f"Failed to fetch weather data for {city}.")


if __name__ == "__main__":
    main()
