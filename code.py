from openai import OpenAI
import os
from dotenv import load_dotenv, find_dotenv
import panel as pn  # GUI

# Load environment variables from .env file
_ = load_dotenv(find_dotenv())
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')

# Initialize the OpenAI client
client = OpenAI(
    api_key=OPENAI_API_KEY,
)

# Function to continue the conversation
def continue_conversation(messages, temperature=0):
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=messages,
        temperature=temperature,
    )
    return response.choices[0].message.content

# Function to add prompts to the conversation
def add_prompts_conversation():
    # Get the value introduced by the user
    prompt = client_prompt.value_input
    client_prompt.value = ''

    # Append to the context the user prompt
    context.append({'role': 'user', 'content': f"{prompt}"})

    # Get the response
    response = continue_conversation(context)

    # Add the response to the context
    context.append({'role': 'assistant', 'content': f"{response}"})

    # Update the panels to show the conversation
    panels.append(
        pn.Row('User:', pn.pane.Markdown(prompt, width=600))
    )
    panels.append(
        pn.Row('Assistant:', pn.pane.Markdown(response, width=600))
    )

    return pn.Column(*panels)

# Creating the prompt
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
mozzarella sausage 3.00,
canadian bacon 3.50,
romesco sauce 1.50,
peppers 1.00
Drinks:
coke 3.00, 2.00, 1.00
sprite 3.00, 2.00, 1.00
vichy catalan 5.00
"""}]

# Creating the panel
pn.extension()

panels = []

client_prompt = pn.widgets.TextInput(value="Hi", placeholder='Enter text here…')
button_conversation = pn.widgets.Button(name="Talk")

interactive_conversation = pn.bind(add_prompts_conversation, button_conversation)

dashboard = pn.Column(
    client_prompt,
    pn.Row(button_conversation),
    pn.panel(interactive_conversation, loading_indicator=True),
)

dashboard
