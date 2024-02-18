# AI-Model

# Overview
Our project focuses on the development of two AI models designed to provide valuable insights and assistance for startups and businesses. These models, businessRater and fundingEstimer, are tailored to address specific tasks aimed at enhancing decision-making processes and strategic planning.

## BusinessRater
businessRater is an AI model designed to evaluate and rate businesses based on a set of unique parameters. These parameters include total funding, geographical location, domain expertise, and other relevant factors. The model has been trained using supervised learning techniques on a comprehensive dataset comprising data from over 900 startups and businesses.

### Model Training
Using the RandomForestRegression algorithm, businessRater learns to extract key factors that influence the success rate of a business. By analyzing historical data and identifying patterns, the model can accurately forecast the likelihood of success for a given business venture.

## FundingEstimer
fundingEstimer complements the functionality of businessRater by estimating the total funding required for a project or startup to succeed. Leveraging the output of businessRater, this model provides an accurate estimation of the financial resources needed to support a venture.

## Collaboration with BusinessRater
The output of businessRater, which represents the success rate of a project or startup, serves as the input for fundingEstimer. By analyzing this data alongside additional factors, such as market conditions and industry trends, fundingEstimer generates a precise estimate of the total funding required to achieve success.

## Usage
To utilize the capabilities of our AI models, users can provide input data about their project or startup to businessRater. The model will then deliver a success rate, which can be used as input for fundingEstimer to determine the necessary total funding.

For more detailed information and examples, please refer to the accompanying .ipynb file.

# Conclusion
By combining the capabilities of businessRater and fundingEstimer, our AI models offer valuable assistance and insights to stakeholders in the business community. Whether you're a startup founder seeking strategic guidance or an investor evaluating potential opportunities, our intelligent business simulator system can provide meaningful support.
