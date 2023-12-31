# Imports
import os
import get_acceptable_triples
import check_good_grids
import get_good_grids
import generate_string_grid
import mapping

grid = mapping.default_grid  # Set default grid

IS_TESTING = False  # True to use pre-made grid from testing.py, False to ask the user to fill the grid


# Get words from words.txt
words_raw = open("words.txt", "r")
words = []

for i in range(2315):
    words.append(words_raw.readline()[0:5])


if IS_TESTING:  # Solve pre-made grid
    import testing

    # Solve
    (
        good_triples,
        good_letters,
        good_words,
    ) = get_acceptable_triples.get_acceptable_triples(testing.test_grid, words)

    good_grids = get_good_grids.get_good_grids(good_triples, good_letters, good_words)

    solution_grids = check_good_grids.check_good_grids(testing.test_grid, good_grids)

    # Visualise solved grids
    for solution_grid in solution_grids:
        print("\n")

        # Create default grid object to modify
        complete_grid = mapping.default_grid
        for i in complete_grid.keys():
            # Avoid blank letters
            if complete_grid[i] != "BLANK":
                # Update grid dictionary to match grid solution tuple
                complete_grid[i]["letter"] = solution_grid[mapping.grid_mapping[i][0]][
                    mapping.grid_mapping[i][1]
                ][mapping.grid_mapping[i][2]]

        # Visualise solved grid
        print(generate_string_grid.generate_string_grid(complete_grid))
        print("\n")


else:  # Solve grid made by user
    for i in grid.keys():
        # Clear terminal and print grid
        if grid[i] == "BLANK":
            continue
        os.system("cls||clear")
        grid[i]["letter"] = "■"
        print(generate_string_grid.generate_string_grid(grid))

        # Ask the user for a letter
        letter = ""
        while letter not in [
            "a",
            "b",
            "c",
            "d",
            "e",
            "f",
            "g",
            "h",
            "i",
            "j",
            "k",
            "l",
            "m",
            "n",
            "o",
            "p",
            "q",
            "r",
            "s",
            "t",
            "u",
            "v",
            "w",
            "x",
            "y",
            "z",
        ]:
            letter = input(f"Please input a letter in cell {i}: ").lower()

        # Ask the user for the type of the letter
        type_letter = ""
        while type_letter != "g" and type_letter != "w" and type_letter != "y":
            type_letter = input(
                "Please enter the type of that cell (G/g for green, Y/y for yellow, W/w for white): "
            ).lower()
        grid[i]["type"] = type_letter
        grid[i]["letter"] = letter

    # Clear terminal and print final grid
    os.system("cls||clear")
    print(generate_string_grid.generate_string_grid(grid))
    print("Solving...")

    # Solve
    (
        good_triples,
        good_letters,
        good_words,
    ) = get_acceptable_triples.get_acceptable_triples(grid, words)

    good_grids = get_good_grids.get_good_grids(good_triples, good_letters, good_words)

    solution_grids = check_good_grids.check_good_grids(grid, good_grids)

    # Visualise solved grids
    for solution_grid in solution_grids:
        print("\n")

        # Create default grid object to modify
        complete_grid = mapping.default_grid
        for i in complete_grid.keys():
            # Avoid blank letters
            if complete_grid[i] != "BLANK":
                # Update grid dictionary to match grid solution tuple
                complete_grid[i]["letter"] = solution_grid[mapping.grid_mapping[i][0]][
                    mapping.grid_mapping[i][1]
                ][mapping.grid_mapping[i][2]]

        # Visualise solved grid
        print(generate_string_grid.generate_string_grid(complete_grid))
        print("\n")
