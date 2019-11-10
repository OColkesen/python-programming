
"""
Creating a list of obeyed comments by Simon

Author: Oğuzhan Çölkesen
"""

def simon_says(instructions):
    """
    Returns the instructions that would be obeyed in a game of Simon Says.

    Parameters:
        instructions - a list of strings, where each element is an instruction
                       issued by Simon.

    Returns:
        A list of strings, containing the instructions that were obeyed.
    """
    obeyed_commands = []
    string_placeholder = ""
    
    for i in instructions:
        words = i.split(" ")
        
        if words[0] == "Simon" and words[1] == "says":
            words = words[2:]
            
            string_placeholder = "" #resetting the string_placeholder to empty string before every loop
            
            for i in words: #the loop adds every word in the list to a string and appends it to a list as one element
                string_placeholder += i
                
                if i != words[-1]: #don't add space if it is the last word
                    string_placeholder += " "
                    
            obeyed_commands.append(string_placeholder)
    
    return obeyed_commands

def main():
    """ Tester function. """
    print("\nTesting Simon Says")
    obeyed = simon_says(["Simon says smile", "Clap your hands",
                         "Simon says jump", "Nod your head"])
    print("Test case 1:", obeyed)

    obeyed = simon_says(["simon says wave", "Simon say jump",
                         "Simon says twist and shout"])
    print("Test case 2:", obeyed)

    obeyed = simon_says(["simon says wave", "simon says jump",
                         "simon says clap"])
    print("Test case 3:", obeyed)

    obeyed = simon_says(["Jump", "Simon says wave"])
    print("Test case 4:", obeyed)
    print()

if __name__ == "__main__":
    main()