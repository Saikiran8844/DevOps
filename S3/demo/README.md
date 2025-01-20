# Weather Dashboard Demo

This project demonstrates a **Weather Dashboard** that fetches real-time weather data using the OpenWeather API and saves it to an AWS S3 bucket.

## Features
- Fetches weather data for multiple cities.

- Displays temperature, humidity, and weather conditions.

- Saves weather data to AWS S3 as JSON files.

- Implements environment variable management using `.env` files.

- Utilizes Python libraries like `boto3`, `requests`, and `dotenv`.


## Prerequisites
To run this project, ensure you have the following:
- Python 3.8 or above installed
  
- AWS account and credentials configured

- OpenWeather API key

- Git installed on your machine


## Installation

Follow these steps to set up and run the project on your local machine:

1. **Clone the Repository**
   ```bash
   git clone https://github.com/Saikiran8844/DevOps.git
   cd S3/demo

2. **Install required dependencies**
   ```bash
   pip install -r requirements.txt

3. **Configure Environment Variables**
- Create a `.env` file in the root directory and add the following:
  ```bash
   OPENWEATHER_API_KEY=your_openweather_api_key
   AWS_ACCESS_KEY_ID=your_aws_access_key_id
   AWS_SECRET_ACCESS_KEY=your_aws_secret_access_key
   AWS_BUCKET_NAME=your_unique_bucket_name
   AWS_DEFAULT_REGION=your_preferred_aws_region

- Replace `your_openweather_api_key`, `your_aws_access_key_id`, `your_aws_secret_access_key`,`your_unique_bucket_name`, and `your_preferred_aws_region` with actual values.

4. **Configure AWS CLI**
- Run `aws configure` and set up your credentials:
   ```bash
   aws configure

- Ensure the configured region matches the `AWS_DEFAULT_REGION` in `.env`.


## Usage

1. **Run the Weather Dashboard script**
   ```bash
    python src/weather_dashboard.py

2. **Weather Data Workflow**

The script will:
- Create the specified S3 bucket if it does not exist.
- Fetch weather data for predefined cities.
- Save the fetched data as JSON files to the S3 bucket.


## Project Structre
>
>   ```
>   S3/demo/
>   ├── src/
>   │   ├── weather_dashboard.py       # Main application script           # Script to validate API key
>   ├── .env                           # Environment variables
>   ├── requirements.txt               # Python dependencies
>   ├── README.md                      # Project documentation


## Key Concepts
- **API Integration**: Using the OpenWeather API to fetch weather data.

- **Environment Variables**: Storing sensitive data securely using python-dotenv.

- **AWS S3 Buckets**: Creating and interacting with S3 buckets using boto3.

- **Error Handling**: Gracefully managing API and AWS errors.

- **Modular Python Code**: Structuring Python scripts for readability and reusability.


