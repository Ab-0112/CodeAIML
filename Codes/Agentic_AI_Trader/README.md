
### 📈 Agentic AI Stock Trader

This project demonstrates how to build an AI agent for stock trading using **Agentic AI** principles and **Deep Q-Learning (DQN)**. The agent is trained to perceive a simulated stock market environment and make autonomous decisions to maximize profit.

The code is refactored into a modular structure, making it clean, scalable, and easy to understand.

### ✨ Features

  * **Deep Q-Network (DQN)**: A neural network that learns to predict the best trading actions.
  * **Custom Trading Environment**: A simulated stock market where the agent learns and operates.
  * **Experience Replay**: The agent stores and reuses past experiences to learn more effectively from batches of data.
  * **Exploration vs. Exploitation**: The agent balances taking random actions to discover new strategies and using its learned knowledge to make profitable decisions.
  * **Interactive UI**: A simple user interface built with Streamlit to demonstrate the agent's training and performance.

### 🚀 Getting Started

#### Prerequisites

Ensure you have Python 3.8 or higher installed on your system.

#### Installation

1.  **Clone the repository:**

    ```bash
    git clone https://github.com/your-username/agentic-ai-trader.git
    cd agentic-ai-trader
    ```

2.  **Create a virtual environment (recommended):**

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows: `venv\Scripts\activate`
    ```

3.  **Install the required libraries:**
    The project uses a `requirements.txt` file to manage dependencies.

    ```bash
    pip install -r requirements.txt
    ```

### 🖥️ How to Run the UI

To start the interactive demonstration, run the Streamlit application from your terminal:

```bash
streamlit run streamlit_app.py
```

This will open a new window in your web browser where you can configure and run the training simulation.

### 📂 Project Structure

```
agentic-ai-trader/
├── src/
│   ├── __init__.py         # Marks src as a Python package
│   ├── environment.py      # Defines the TradingEnvironment class
│   └── model.py            # Defines the DQN and DQNAgent classes
├── streamlit_app.py        # Main file for the interactive UI
├── requirements.txt        # Lists all project dependencies
├── README.md               # The file you are currently reading
└── .gitignore              # Specifies files and directories to ignore
```

### 🤝 Contribution

Feel free to open an issue or submit a pull request if you have any suggestions or improvements.