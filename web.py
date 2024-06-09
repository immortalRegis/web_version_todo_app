import streamlit as st
import functions

todos = functions.get_todos()
def add_todo():
    todo = st.session_state["new_todo"] + "\n"
    todos.append(todo)
    functions.write_todos(todos)


st.title("The Todo App")
st.subheader("Web Version.")
st.write("This app is going into the cloud!")


for index, todo in enumerate(todos):
   box = st.checkbox(todo, key=todo)
   if box:
       todos.pop(index)
       functions.write_todos(todos)
       del st.session_state[todo]
       st.rerun()

st.text_input(label="Add a new todo", placeholder="Add a new todo...",
              on_change=add_todo, key="new_todo")
