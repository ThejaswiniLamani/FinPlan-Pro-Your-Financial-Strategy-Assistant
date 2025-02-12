# FinPlan-Pro-Your-Financial-Strategy-Assistant: A Personalized Financial Planning Assistant

Welcome to the **FinPlan-Pro-Your-Financial-Strategy-Assistant** repository! This Telegram-based bot is designed to assist users in making sound financial decisions by providing personalized financial advice. The bot takes into account important financial factors such as monthly income, expenses, and personal financial goals, and then leverages Google Gemini API to generate actionable advice.

Whether you're looking to optimize your budget, plan for a major financial goal (like buying a home or saving for retirement), or explore investment opportunities, this bot aims to provide tailored suggestions that suit your unique financial situation.

## Key Features of the Financial Advisor Bot:
- **Interactive User Experience:** The bot uses a conversational interface to engage with users, asking for their financial details (age, income, expenses, and goals) in a friendly manner.
- **Personalized Financial Plan:** Based on the collected information, the bot generates a detailed financial plan that includes suggestions on savings, feasible goals, and recommendations for investment opportunities.
- **Smart Financial Advice:** The bot offers budget optimization tips, identifies areas to cut unnecessary expenses, and proposes investment options tailored to the user's financial capacity.
- **Indian Context Focus:** The financial advice is tailored for users in India, using local terms such as 'lakh' and 'crore' for currency and understanding the unique financial context.

## Features Breakdown:
1. **User-Friendly Interaction:** The bot collects critical financial information like monthly income, expenditure, and future financial goals.
2. **Goal-Driven Financial Planning:** Once the user shares their financial goals (such as buying a home, saving for retirement, or tax-saving), the bot assesses these goals based on the user’s current financial standing.
3. **Savings Potential Analysis:** The bot calculates how much the user can save each month by analyzing income and expenses.
4. **Investment Recommendations:** Based on the user’s budget and goals, the bot suggests suitable investment options such as mutual funds, stocks, or SIPs (Systematic Investment Plans).
5. **Budget Optimization:** The bot helps users identify areas where they can cut down on unnecessary expenses and optimize their budget to increase monthly savings.
6. **Actionable Plan with Timelines:** The bot guides the user step by step on how to achieve their financial goals with a clear timeline and strategy.

## How It Works:
1. **User Initiates the Conversation:**
   - When a user starts a conversation with the bot by typing `/start`, the bot greets them and asks for basic details like age, income, expenses, and financial goals.
2. **Data Collection:**
   - The bot sequentially collects information from the user: first their age, followed by income, expenses, and financial goals.
3. **Data Processing:**
   - Once the data is collected, the bot uses Google Gemini API to process the information and generate tailored financial advice, including savings potential, investment suggestions, and budget optimization strategies.
4. **Personalized Financial Plan:**
   - After processing the data, the bot sends the user a personalized financial plan, outlining actionable steps towards achieving their goals.

## How to Use the Financial Advisor Bot:
1. **Search for the Bot:**
   - Open Telegram and search for `Finance_Advisor_Bot`.
2. **Start the Conversation:**
   - Type `/start` to begin your journey to better financial health.
3. **Provide Your Financial Information:**
   - The bot will ask for your age, monthly income, expenses, and financial goals (such as saving for a home or retirement).
4. **Receive Personalized Financial Advice:**
   - After gathering your details, the bot will provide you with a detailed, actionable financial plan tailored to your needs.

## Setup and Running the Bot:
To set up and run the bot on your local machine, follow these instructions:

1. **Clone the Repository:**
   - Clone this repository to your local machine using:
     ```bash
     git clone https://github.com/yourusername/FinPlan-Pro-Your-Financial-Strategy-Assistant.git
     ```

2. **Create the .env File:**
   - Inside your project folder, create a `.env` file to securely store your Telegram Bot Token and Google Gemini API Key.
     ```text
     TELEGRAM_BOT_TOKEN=your-telegram-bot-token
     GEMINI_API_KEY=your-google-gemini-api-key
     ```

3. **Install Dependencies:**
   - Install the required Python dependencies by running:
     ```bash
     pip install -r requirements.txt
     ```

4. **Run the Bot:**
   - Start the bot using the following command:
     ```bash
     python financial_advisor_bot.py
     ```

The bot will now be running and ready to interact with users on Telegram.

## Technologies Used:
- **Telegram Bot API:** The bot framework to interact with users through Telegram.
- **Google Gemini API:** Used to generate personalized financial advice based on user input.
- **Python:** The programming language used for bot development and data processing.

## Searching for the Bot on Telegram:
To interact with the Finance Advisor Bot, search for `Finance_Advisor_Bot` on Telegram and type `/start` to begin the conversation. The bot will guide you step by step to create your personalized financial plan.

![Screenshot 2025-02-12 122711](https://github.com/user-attachments/assets/2e6273c6-52af-49be-8a92-17441ba79e32)
![Screenshot 2025-02-12 122725](https://github.com/user-attachments/assets/0ae374c0-b2c8-47c0-afc2-6cb316fca1cf)

![Screenshot 2025-02-12 122751](https://github.com/user-attachments/assets/6a24d03c-bd6b-4727-b228-0c531129df79)

