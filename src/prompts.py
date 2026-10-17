# prompts.py

def browse_file_prompt():
    """
    Prompt user for either: 
    * browsing image directory
    * image filename
    """
    
    while True:
        # user input
        user_option = input(
            "[1] Browse images\n"
            "[2] Enter image filename\n"
            "Select an option: "
        ).strip()

        # validate
        if user_option in ("1", "2"):
            break

        # retry
        print("\nInvalid choice. Try again.\n")

    return user_option

if __name__ == "__main__":
    browse_file_prompt()