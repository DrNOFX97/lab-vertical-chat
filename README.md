![logo_ironhack_blue 7](https://user-images.githubusercontent.com/23629340/40541063-a07a0a8a-601a-11e8-91b5-2f13e4e6b441.png)

# Lab | Vertical Chat

## Getting Started

Follow the instructions provided in the notebook.

Read the instructions for each cell and provide your answers. Make sure to test your answers in each cell and save. Jupyter Notebook should automatically save your work progress. But it's a good idea to periodically save your work manually just in case.

## Deliverables

- Downloaded notebook with your responses to each of the exercises.


## Submission

- Upon completion, add your deliverables to git. 
- Then commit git and push your branch to the remote.
- Make a pull request and paste the PR link in the submission field in the Student Portal.

<br>

**Good luck!**

_____________________________

# Vertical Chat Application

## Overview

This project demonstrates how to build a vertical chat application for a small business using GPT-3.5, OpenAI, and Panel. The application acts as an OrderBot for a fast-food restaurant, collecting orders, summarizing them, and handling payments.

## Features

- **Order Collection**: The bot collects orders from customers, including beverages and extras.
- **Order Summarization**: The bot summarizes the order and confirms it with the customer.
- **Payment Collection**: The bot collects payment after confirming the order.
- **Friendly Interaction**: The bot interacts with customers in a friendly and professional manner.

## Prerequisites

- Python 3.x
- OpenAI API Key
- Panel library
- Dotenv library

## Installation

1. **Clone the Repository**:
   ```sh
   git clone github.com/DrNOFX97/lab-vertical-chat.git
   cd vertical-chat-app
   ```

2. **Install Dependencies**:
   ```sh
   pip install -r requirements.txt
   ```

3. **Set Up Environment Variables**:
   - Create a `.env` file in the root directory of the project.
   - Add your OpenAI API key to the `.env` file:
     ```env
     OPENAI_API_KEY=your_openai_api_key_here
     ```

## Usage

1. **Run the Application**:
   ```sh
   python app.py
   ```

2. **Interact with the Chatbot**:
   - Open the provided URL in your web browser.
   - Enter your message in the text input field and click the "Talk" button to interact with the chatbot.

## Prompt Examples

### Friendly and Detailed Prompt

```python
context = [{'role': 'system', 'content': """
Act as an OrderBot, you work collecting orders in a delivery-only fast food restaurant called
My Dear Frankfurt.
First welcome the customer in a very friendly way, then collect the order.
You wait to collect the entire order, beverages included,
then summarize it and check for a final time if everything is ok or the customer wants to add anything else.
Finally, you collect the payment.
Make sure to clarify all options, extras, and sizes to uniquely identify the item from the menu.
You respond in a short, very friendly style.
The menu includes:
burger 12.95, 10.00, 7.00
frankfurt 10.95, 9.25, 6.50
sandwich 11.95, 9.75, 6.75
fries 4.50, 3.50
salad 7.25
Toppings:
extra cheese 2.00,
mushrooms 1.50,
mozzarella sauce 3.00,
canadian bacon 3.50,
romesco sauce 1.50,
peppers 1.00
Drinks:
coke 3.00, 2.00, 1.00
sprite 3.00, 2.00, 1.00
vichy catalan 5.00
"""}]
```

### Concise and Professional Prompt

```python
context = [{'role': 'system', 'content': """
Act as an OrderBot for My Dear Frankfurt, a delivery-only fast food restaurant.
Welcome the customer, collect the entire order including beverages, summarize the order, and confirm.
Finally, collect the payment.
Clarify all options, extras, and sizes.
Respond professionally.
The menu includes:
burger 12.95, 10.00, 7.00
frankfurt 10.95, 9.25, 6.50
sandwich 11.95, 9.75, 6.75
fries 4.50, 3.50
salad 7.25
Toppings:
extra cheese 2.00,
mushrooms 1.50,
mozzarella sauce 3.00,
canadian bacon 3.50,
romesco sauce 1.50,
peppers 1.00
Drinks:
coke 3.00, 2.00, 1.00
sprite 3.00, 2.00, 1.00
vichy catalan 5.00
"""}]
```

### Casual and Engaging Prompt

```python
context = [{'role': 'system', 'content': """
Act as an OrderBot for My Dear Frankfurt, a cool fast food joint.
Greet the customer warmly, take their order including drinks, summarize, and confirm.
Collect payment at the end.
Make sure to clarify all options, extras, and sizes.
Keep it casual and friendly.
The menu includes:
burger 12.95, 10.00, 7.00
frankfurt 10.95, 9.25, 6.50
sandwich 11.95, 9.75, 6.75
fries 4.50, 3.50
salad 7.25
Toppings:
extra cheese 2.00,
mushrooms 1.50,
mozzarella sauce 3.00,
canadian bacon 3.50,
romesco sauce 1.50,
peppers 1.00
Drinks:
coke 3.00, 2.00, 1.00
sprite 3.00, 2.00, 1.00
vichy catalan 5.00
"""}]
