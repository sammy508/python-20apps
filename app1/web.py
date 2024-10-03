

import streamlit as st
from functon import get_todos  # Import the functions from function.py

# Fetch todos
todos = get_todos()
print(f"Fetched todos: {todos}")  # Debug print

st.title("My ToDo App")
st.subheader("Schedule your day here")
st.write("Enhance your productivity")

if not todos:
    st.write("No data in the list.")
else:
    # Create checkboxes for each todo
    for i, todo in enumerate(todos):
        st.checkbox(todo, key=i)
    

new_todo = st.text_input(label=" ", placeholder="Enter todo")    

