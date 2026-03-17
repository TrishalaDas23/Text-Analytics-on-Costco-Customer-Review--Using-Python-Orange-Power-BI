# Executive Summary
Customer feedback is one of the most valuable sources of insight for improving business operations and customer satisfaction. This project analyzes customer reviews of Costco collected from TrustPilot using Sentiment Analysis and Topic Modelling techniques to identify customer sentiment trends and key recurring issues.

# Software/Tools
•	**Python**

•	**Orange**

•	**Power BI**

# Techniques
•	Web scrapping using Python Selenium library. Natural Language Processing (NLP) methods were then applied to clean and prepare the textual data for analysis. 
•	Sentiment Analysis using the VADER algorithm in the Orange tool 
•	Topic Modelling (LDA) to identify recurring themes and concerns within customer reviews.
# Data Collection
2.1 Data Source
Customer reviews were collected from TrustPilot, a widely used online review platform where customers share their experiences with companies.
The reviews were collected using Python with the Selenium library, which automated the process of navigating through multiple review pages and extracting the relevant information.
Each review page contained approximately 20 customer reviews, and the scraping process captured the following attributes:
•	Review Rating
•	Review Date
•	Review Title
•	Review Content
Company replies to customer reviews were intentionally excluded to focus solely on customer feedback.

# Dataset Overview
The final raw dataset contains 2276 customer reviews spanning from 2011 to 2024.
The dataset includes four primary attributes:
Attribute	Description
Rating	Numerical score from 1 (Poor) to 5 (Excellent)
Date	Date when the review was posted
Review Title	Short summary of the customer’s feedback
Review	Detailed description of the customer’s experience
Since the dataset was collected from a public platform, it contained inconsistencies such as varying date formats, duplicate entries, and textual noise. Therefore, a comprehensive data preprocessing process was required before analysis.
# Data Pre-Processing
Data preprocessing was conducted using Python to ensure the dataset was clean, consistent, and suitable for text analysis.
## Removing Missing Values
Rows containing missing values were identified and removed using the dropna() function, ensuring that only complete reviews were retained for analysis.
## Standardizing Date Format
The date column contained mixed formats such as:
•	Exact dates
•	Relative expressions (e.g., “a day ago”, “2 days ago”, “hours ago”)
 
These values were converted into a standardized DD/MM/YYYY format using Python loops and conditional logic as follows:
  
## Text Cleaning
To ensure consistency in textual analysis, the following steps were applied:
•	Converted all text to lowercase
•	Removed special characters, emojis, and symbols
•	Retained only meaningful words for analysis
A custom text-cleaning function was used to process both the Review Title and Review columns.
## Removing Duplicate Reviews
Duplicate reviews were identified based on the Review Title and Review content and removed using the drop_duplicates() function, ensuring each review appeared only once.
## Stop Word Removal
Common words such as “the”, “is”, and “and” do not contribute meaningful insights in text analysis. These were removed using the NLTK stop word dictionary, reducing noise in the dataset.

## Lemmatization
Lemmatization was applied using NLTK’s WordNetLemmatizer to reduce words to their base form.
For example:
•	running → run
•	ran → run
•	runner → run
This improves the accuracy of text analysis by treating different word forms as a single term.
# Sentiment Analysis and Topic Modelling
The flow diagram for sentiment analysis and topic modelling techniques was done in Orange tool as follows:
 
# Sentiment Analysis
To understand customer satisfaction levels, Sentiment Analysis was performed using the VADER algorithm in the Orange tool.
VADER assigns four sentiment scores:
•	Positive
•	Negative
•	Neutral
•	Compound score
The compound score ranges from -1 to +1 and represents the overall sentiment of each review.
  

# # Yearly Sentiment Trends
The average compound sentiment score was calculated for each year between 2011 and 2024.
 
Key observations include:
•	2011–2013: Strong positive sentiment (above 0.70)
•	2014–2016: Significant decline in sentiment
•	2017–2020: Sentiment remained moderately negative
•	2021: Lowest sentiment score (-0.28)
•	2023–2024: Slight improvement but still slightly negative
To illustrate the trends over time, the average yearly compound sentiment scores were plotted using a line chart in Power BI as follows:
 
Insight: These trends suggest that customer satisfaction has declined over time and may reflect operational challenges or changes in customer expectations.

# Topic Modelling
To identify recurring issues within customer feedback, Latent Dirichlet Allocation (LDA) topic modelling was applied using the Orange tool.
The analysis generated 10 major topics, each representing common themes in customer reviews.
 
## Key Topics Identified
1. Customer Service Issues
Reviews frequently mention concerns regarding employee responsiveness, management behavior, and service quality.
2. Delivery Delays
Customers expressed frustration regarding long waiting times and delayed deliveries.
3. Product Returns and Defects
Many reviews highlighted difficulties in returning defective products or resolving purchase-related issues.
4. Membership Dissatisfaction
Some customers questioned the value of Costco’s membership and reported negative in-store experiences.
5. Delivery Scheduling
Customers reported inefficiencies in delivery timing and scheduling policies.
6. Product Quality Feedback
While many customers praised product quality and pricing, others reported inconsistent product experiences.
7. Pricing and Refund Concerns
Customers mentioned dissatisfaction regarding pricing transparency and refund procedures.
8. Employee Interaction
Several reviews referenced negative interactions with staff during refund or membership processes.
9. Online Ordering Issues
Customers reported technical issues and delays related to online orders.
10. Communication and Shipping Updates
Reviews highlighted a lack of timely communication regarding shipping status and order updates.
The LDA model achieved:
•	Log Perplexity: 54.99
•	Topic Coherence: 0.57
These values indicate moderate interpretability and reliable topic grouping.
# Key Insights of the Analysis
The analysis highlights several important insights for Costco management:
•	Customer sentiment has declined significantly since 2013.
•	Operational issues such as delivery delays and communication gaps are major sources of dissatisfaction.
•	Customer service quality is frequently mentioned in negative reviews.
•	Customers value Costco’s product quality and pricing, but operational issues reduce overall satisfaction.
•	Online shopping experience and refund processes require improvement.
# Strategic Recommendations
Based on the analysis, the following strategic actions are recommended.
1.	Improve Delivery Operations
Enhance logistics planning and provide real-time updates to customers to reduce delivery delays.
2.	Strengthen Customer Service Training
Invest in employee training programs focused on customer interaction and problem resolution.
3.	Enhance Online Shopping Platform
Improve the stability and efficiency of the online ordering system to minimize technical issues.
4.	Simplify Return and Refund Processes
Streamline refund procedures to ensure faster and more transparent customer service.
5.	Improve Customer Communication
Provide proactive communication regarding shipping updates, order status, and service inquiries.
# Conclusion
This analysis demonstrates the value of using data analytics and natural language processing techniques to understand customer feedback at scale.
Although Costco maintains strengths in product quality and pricing, the analysis shows that operational inefficiencies and service-related issues have impacted customer satisfaction in recent years.
By addressing these concerns through targeted operational improvements and enhanced customer engagement strategies, Costco can strengthen its brand reputation, improve customer loyalty, and sustain long-term business growth.

