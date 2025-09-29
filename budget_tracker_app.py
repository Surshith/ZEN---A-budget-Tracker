import streamlit as st

# Initialize session state for expenses
if 'expenses' not in st.session_state:
    st.session_state.expenses = {
        "Food": 0,
        "Transport": 0,
        "Entertainment": 0,
        "Others": 0
    }

st.title("💰 Budget Tracker App")

# Expense Section
st.header("Add a New Expense")

amount = st.number_input("Enter Amount (₹):", min_value=0.0, step=0.01)
category = st.selectbox("Select Category:", ["Food", "Transport", "Entertainment", "Others"])
description = st.text_input("Description (optional):")

if st.button("Add Expense"):
    if amount <= 0:
        st.error("Please enter a valid amount!")
    else:
        st.session_state.expenses[category] += amount
        st.success(f"Added ₹{amount:.2f} to {category}")

# Summary Section
st.header("📊 Expense Summary")

total = sum(st.session_state.expenses.values())
st.write(f"**Total Spending:** ₹{total:.2f}")

st.subheader("Category-wise Spending")
for cat, amt in st.session_state.expenses.items():
    st.write(f"{cat}: ₹{amt:.2f}")

#  To Show a pie chart
st.subheader("Visual Representation")
st.bar_chart(st.session_state.expenses)

