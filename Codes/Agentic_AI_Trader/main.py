import streamlit as st
import yfinance as yf
import matplotlib.pyplot as plt

# Import the refactored components
from src.environment import TradingEnvironment
from src.model import DQNAgent

# --- Data Loading and Preprocessing ---
@st.cache_data
def get_data(symbol="AAPL", start_date="2020-01-01", end_date="2025-02-14"):
    """Fetches and preprocesses stock data with caching."""
    data = yf.download(symbol, start=start_date, end=end_date)
    data['SMA_5'] = data['Close'].rolling(window=5).mean()
    data['SMA_20'] = data['Close'].rolling(window=20).mean()
    data['Returns'] = data['Close'].pct_change()
    data.dropna(inplace=True)
    data.reset_index(drop=True, inplace=True)
    return data

# --- Main UI Logic ---
st.title("Agentic AI Stock Trader 📈")
st.markdown("A demonstration of an AI agent using Deep Q-Learning to trade stocks.")

# User inputs
symbol = st.selectbox("Select Stock Symbol", ["AAPL", "GOOG", "MSFT"])
episodes = st.slider("Number of Training Episodes", 100, 1000, 500)

if st.button("Start Training and Demo"):
    st.subheader("1. Data Preparation")
    with st.spinner("Fetching and preprocessing data..."):
        stock_data = get_data(symbol)
        st.success("Data loaded successfully!")
        st.dataframe(stock_data.head())
    
    # --- Training ---
    st.subheader("2. Training the Agent")
    train_status = st.empty()
    total_rewards = []
    
    env = TradingEnvironment(stock_data)
    agent = DQNAgent(state_size=4, action_size=3)
    batch_size = 32

    for episode in range(episodes):
        state = env.reset()
        done = False
        total_reward = 0
        while not done:
            action = agent.act(state)
            next_state, reward, done, _ = env.step(action)
            agent.remember(state, action, reward, next_state, done)
            state = next_state
            total_reward += reward
        
        agent.replay(batch_size)
        total_rewards.append(total_reward)
        train_status.write(f"Episode {episode+1}/{episodes}, Total Reward: {total_reward:.2f}")

    st.success("Training Complete!")
    
    # --- Visualization of Training Progress ---
    st.subheader("Training Progress")
    fig, ax = plt.subplots()
    ax.plot(total_rewards)
    ax.set_title("Total Reward per Episode")
    ax.set_xlabel("Episode")
    ax.set_ylabel("Total Reward")
    st.pyplot(fig)

    # --- Testing ---
    st.subheader("3. Testing the Agent")
    with st.spinner("Simulating a trading session..."):
        test_env = TradingEnvironment(stock_data)
        state = test_env.reset()
        done = False
        
        balance_history = [test_env.initial_balance]
        
        while not done:
            action = agent.act(state)
            next_state, reward, done, _ = test_env.step(action)
            state = next_state if next_state is not None else state
            balance_history.append(test_env.balance)
            
        final_balance = test_env.balance
        profit = final_balance - test_env.initial_balance
        
        st.success("Testing Complete!")
        st.metric(label="Final Balance", value=f"${final_balance:.2f}")
        st.metric(label="Total Profit", value=f"${profit:.2f}")
        
    # --- Visualization of Performance ---
    st.subheader("Trading Performance")
    fig2, ax2 = plt.subplots()
    ax2.plot(balance_history)
    ax2.set_title("Account Balance Over Time")
    ax2.set_xlabel("Time Step")
    ax2.set_ylabel("Balance ($)")
    st.pyplot(fig2)