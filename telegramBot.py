import telebot
import google.generativeai as genai

# Replace with your actual tokens (consider using environment variables for security)
BOT_TOKEN = "8179170078:AAFwFYleFhbWRURKEwHEsPA9wkahCxkQTzQ"
GEMINI_API_KEY = "AIzaSyBNTf7yazjxvZ1IZ13AGEmZ7_4MBEyXvNU"

# Initialize the Telegram bot and Google GenAI model
bot = telebot.TeleBot(BOT_TOKEN)
genai.configure(api_key=GEMINI_API_KEY)
model = genai.GenerativeModel("gemini-pro")

# Dictionary to store conversation data for each user
user_data = {}

# Start command handler
@bot.message_handler(commands=["start"])
def start(message):
    user_id = message.chat.id
    user_data[user_id] = {}  # Initialize user data

    # Welcome message with an introduction to the financial planning bot
    bot.send_message(
        user_id,
        "Welcome to Finance Bot!\n"
        "Let's create a personalized financial plan for you. \n\n"
        "First, share your age:"
    )

    # Set the next handler to capture the user's age
    bot.register_next_step_handler(message, get_age)

# Function to capture age
def get_age(message):
    user_id = message.chat.id
    user_data[user_id]["age"] = message.text  # Save the user's age

    # Ask for the user's monthly income
    bot.send_message(user_id, "Thanks! Now, please share your monthly income (in ₹):")
    bot.register_next_step_handler(message, get_income)

# Function to capture income
def get_income(message):
    user_id = message.chat.id
    user_data[user_id]["income"] = message.text  # Save the user's income

    # Ask for the user's monthly expenses
    bot.send_message(user_id, "Thanks! What are your monthly expenses (in ₹)?")
    bot.register_next_step_handler(message, get_expenses)

# Function to capture expenses
def get_expenses(message):
    user_id = message.chat.id
    user_data[user_id]["expenses"] = message.text  # Save the user's expenses

    # Ask for the user's financial goals
    bot.send_message(user_id, "Finally, please share your financial goals (e.g., Buy a home, Retirement, Tax saving):")
    bot.register_next_step_handler(message, finish_conversation)

# Function to finish the conversation and generate a personalized financial plan
def finish_conversation(message):
    user_id = message.chat.id
    user_data[user_id]["goals"] = message.text  # Save the user's financial goals

    # Build a detailed prompt for the GenAI model
    prompt = f"""
    Act as a certified Indian financial advisor. Create a personalized plan for a {user_data[user_id]['age']}-year-old with:
    - Monthly income: ₹{user_data[user_id]['income']}
    - Monthly expenses: ₹{user_data[user_id]['expenses']}
    - Financial goals: {user_data[user_id]['goals']}

    Provide advice tailored to an Indian citizen, taking into account the current income, expenses, and future financial goals.
    1. Savings Potential: Calculate how much the user can save monthly.
    2. Feasibility of Financial Goals: Assess whether the goal is realistic based on income and savings.
    3. Investment Recommendations: Suggest suitable investment options based on affordability.
    4. Budget Optimization: Provide recommendations to cut unnecessary expenses and increase savings.
    5. Action Plan with Timelines: Guide the user with a step-by-step approach to achieving their financial goals.

    Use ₹ currency, and terms like 'lakh'/'crore'. Avoid jargon. Give in a format that Telegram bot can display.
    """

    try:
        # Generate personalized financial advice using the GenAI model
        response = model.generate_content(prompt)

        # Send the generated advice back to the user
        bot.send_message(user_id, f"Here's Your India-Focused Financial Plan\n\n{response.text}")
    except Exception as e:
        # If there is an error during content generation, notify the user
        bot.send_message(user_id, "Error generating advice. Please try again!")

# Start the bot to listen for incoming messages
if __name__ == "__main__":
    bot.infinity_polling()
