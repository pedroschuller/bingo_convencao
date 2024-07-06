import streamlit as st
import random
import pandas as pd

def generate_bingo_board(words, seed):
    random.seed(seed)
    random.shuffle(words)
    return [words[i * 5:(i + 1) * 5] for i in range(5)]

def check_bingo(board, checked):
    # Check rows
    for row in range(5):
        if all(checked[row]):
            return "Linha!"
    # Check columns
    for col in range(5):
        if all(checked[row][col] for row in range(5)):
            return "Linha!"
    # Check for Bingo
    if all(all(row) for row in checked):
        return "BINGO!"
    return ""

def main():
    st.title("Bingo Game")

    words = ["apple", "banana", "cherry", "date", "elderberry", "fig", "grape", "honeydew", 
             "kiwi", "lemon", "mango", "nectarine", "orange", "papaya", "quince", "raspberry",
             "strawberry", "tangerine", "ugli fruit", "vanilla", "watermelon", "xigua", "yam",
             "zucchini", "jackfruit"]

    seed = st.number_input("Enter a numeric seed (1-10000):", min_value=1, max_value=10000, value=1)
    
    board = generate_bingo_board(words, seed)
    
    checked = [[False] * 5 for _ in range(5)]
    cols = st.columns(5)
    
    for i in range(5):
        for j in range(5):
            if cols[j].checkbox(board[i][j], key=f"{i}-{j}"):
                checked[i][j] = True

    result = check_bingo(board, checked)
    if result:
        st.success(result)

if __name__ == "__main__":
    main()
