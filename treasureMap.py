# 🚨 Don't change the code below 👇
row1 = ["🟦 ","️🟦 ","️🟦 "]
row2 = ["🟦 ","🟦 ","️🟦 "]
row3 = ["🟦 ","🟦 ","🟦 "]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")
# 🚨 Don't change the code above 👆

#Write your code below this row 👇
col = int(position[0]) - 1
row = int(position[1]) - 1

# if col == 0 and row == 0:
#     row1[0] = 'X'
# elif col == 0 and row == 1:
#     row2[0] = 'X'
# elif col == 0 and row == 2:
#     row3[0] = 'x'
# elif col == 1 and row == 0:
#     row1[1] = 'X'
# elif col == 1 and row == 1:
#     row2[1] = 'X'
# elif col == 1 and row == 2:
#     row3[1] = 'X'
# elif col == 2 and row == 0:
#     row1[2] = 'X'
# elif col == 2 and row == 1:
#     row2[2] = 'X'
# elif col == 2 and row == 2:
#     row3[2] = 'X'

selected_row = map[row]
selected_row[col] = "X"

#Write your code above this row 👆

# 🚨 Don't change the code below 👇
print(f"{row1}\n{row2}\n{row3}")

