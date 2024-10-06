
import streamlit as st
import functon   # Import the functions from function.py


# Fetch todos
todos = functon.get_todos()

def add_todo():
    todo = st.session_state["new_todo"] + "\n"
    todos.append(todo)
    functon.write_todos(todos) 

st.title("My ToDo App")
st.subheader("Schedule your day here")
st.write("Enhance your productivity")

if not todos:
    st.write("No data in the list.")
else:
    # Create checkboxes for each todo       
    for index, todo in enumerate(todos):
      checkbox =  st.checkbox(todo, key=todo)
      if checkbox:
          todos.pop(index)
          functon.write_todos(todos)
          del st.session_state[todo]    
          st.rerun()

new_todo = st.text_input(label=" ", placeholder="Enter todo", on_change = add_todo, key= "new_todo")    

# st.session_state