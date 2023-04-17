import tkinter as tk

# Initialize an empty dictionary to store players and their points
players = {}

# Function to add a player and their initial point
def add_player():
    player_name = player_entry.get()
    point = point_entry.get()
    players[player_name] = int(point)
    player_entry.delete(0, tk.END)
    point_entry.delete(0, tk.END)
    update_display()

# Function to remove a player from the game
def remove_player():
    player_name = player_entry.get()
    if player_name in players:
        del players[player_name]
        player_entry.delete(0, tk.END)
        point_entry.delete(0, tk.END)
        update_display()

# Function to add points to a player
def add_points():
    player_name = player_entry.get()
    points = int(point_entry.get())
    if player_name in players:
        players[player_name] += points
        if players[player_name] == 50:
            players[player_name] = 25
        elif players[player_name] == 100:
            players[player_name] = 50
        player_entry.delete(0, tk.END)
        point_entry.delete(0, tk.END)
        update_display()


# Function to remove points from a player
def remove_points():
    player_name = player_entry.get()
    points = point_entry.get()
    if player_name in players:
        players[player_name] -= int(points)
        player_entry.delete(0, tk.END)
        point_entry.delete(0, tk.END)
        update_display()
        
# Function to display the current points for each player
def update_display():
    point_list.delete(0, tk.END)
    for player, points in players.items():
        point_list.insert(tk.END, f"{player}: {points}")

# Initialize the Tkinter GUI
root = tk.Tk()
root.title("Yaniv Point Counter")

# Add player label and entry
player_label = tk.Label(root, text="Player Name:")
player_label.grid(row=0, column=0)
player_entry = tk.Entry(root)
player_entry.grid(row=0, column=1)

# Add point label and entry
point_label = tk.Label(root, text="Point:")
point_label.grid(row=1, column=0)
point_entry = tk.Entry(root)
point_entry.grid(row=1, column=1)

# Add buttons for adding and removing players/points
add_player_button = tk.Button(root, text="Add Player", command=add_player)
add_player_button.grid(row=2, column=0)
remove_player_button = tk.Button(root, text="Remove Player", command=remove_player)
remove_player_button.grid(row=2, column=1)
add_point_button = tk.Button(root, text="Add Points", command=add_points)
add_point_button.grid(row=3, column=0)
remove_point_button = tk.Button(root, text="Remove Points", command=remove_points)
remove_point_button.grid(row=3, column=1)

# Add listbox for displaying current points
point_list = tk.Listbox(root)
point_list.grid(row=4, column=0, columnspan=2)

# Call the update_display function to display the current points
update_display()

# Start the Tkinter event loop
root.mainloop()
