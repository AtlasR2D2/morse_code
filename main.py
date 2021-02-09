import time as t

# Text to Morse Code Convertor

# Morse Code Graphic
morse_code_graphic = """ 
    #                                                
   # #   #    # ###### #####  #  ####    ##   #    # 
  #   #  ##  ## #      #    # # #    #  #  #  ##   # 
 #     # # ## # #####  #    # # #      #    # # #  # 
 ####### #    # #      #####  # #      ###### #  # # 
 #     # #    # #      #   #  # #    # #    # #   ## 
 #     # #    # ###### #    # #  ####  #    # #    # 
                                                     
 #     #                                 #####                       
 ##   ##  ####  #####   ####  ######    #     #  ####  #####  ###### 
 # # # # #    # #    # #      #         #       #    # #    # #      
 #  #  # #    # #    #  ####  #####     #       #    # #    # #####  
 #     # #    # #####       # #         #       #    # #    # #      
 #     # #    # #   #  #    # #         #     # #    # #    # #      
 #     #  ####  #    #  ####  ######     #####   ####  #####  ###### 
                                                                     
                                                                     """


# Construct morse dictionary
letters = [
    'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W',
    'X', 'Y', 'Z', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0'
]
letters_morse = [
    '.-', '-...', '.. .', '-..', '.', '.-.', '--.', '....', '..', '-.-.', '-.-', '⸺', '--', '-.', '. .', '.....',
    '..-.', '. ..', '...', '-', '..-', '...-', '.--', '.-..', '.. ..', '... .', '.--.', '..-..', '...-.', '....-',
    '---', '......', '--..',
    '-....', '-..-', '⸻'
]
punctuation = [
    '.', ',', ':', '?', '\'', '-', '/', '(', ')', '"', '&', '!', ';'
]

punctuation_morse = [
    '..--..', '.-.-', '-.- . .', '-..-.', '..-. .-..', '... .-..', '..- -', '..... -.', '..... .. ..', '..-. -.',
    '. ...', '---.', '... ..'
]

morse_dict = {**dict(zip(letters, letters_morse)), **dict(zip(punctuation, punctuation_morse))}


# Standard timing on the word "PARIS " as the standard word
STANDARD_TIMING_KEYWORD = "PARIS"
STANDARD_WORDS_PER_MINUTE = 20
SPACE = " "
SPACE_ALT = "/"
INTRA_SPACE = "   "
# Initially stores units
timing_units_dict = {
    ".": 1,
    "-": 3,
    " ": 1,
    "intra": 1,
    "inter": 3,
    "SPACE": 7
}


def convert_text_to_morse(text_msg: str):
    """Converts a string text message into morse code"""
    morse_code = []
    for char in text_msg:
        if char in morse_dict:
            morse_code.append(morse_dict[char])
        elif char == SPACE:
            morse_code.append(SPACE_ALT)
    return morse_code


def determine_message_units(morse_cde):
    """determines how many units are in the morse code"""
    message_units = 0
    for elem in standard_timing_keyword_morse:
        if elem != SPACE_ALT:
            for char in elem:
                message_units += timing_units_dict[char]
                if char != " ":
                    # Add an intra unit allocation between dit/dahs
                    message_units += timing_units_dict["intra"]
                else:
                    # Add a SPACE unit allocation
                    message_units += timing_units_dict[" "]
                # Add a inter unit allocation between letters
                message_units += timing_units_dict["inter"]
        else:
            # Add a SPACE unit allocation
            message_units += timing_units_dict["SPACE"]
    return message_units


# ----------------------------------------------------------------------------------------------------------------------------
# Store Standard timing keyword details | Non-operational as need to identify how to elongate units being typed
standard_timing_keyword_morse = convert_text_to_morse(STANDARD_TIMING_KEYWORD)

standard_timing_units = determine_message_units(standard_timing_keyword_morse)

# print(standard_timing_units)
standard_unit_time = round(1/(standard_timing_units*STANDARD_WORDS_PER_MINUTE)*60, 4)
# print(f"STANDARD_WORDS_PER_MINUTE: {STANDARD_WORDS_PER_MINUTE}, using {STANDARD_TIMING_KEYWORD} equates to {standard_unit_time} seconds per unit")
# ----------------------------------------------------------------------------------------------------------------------------

# Record input_message, convert to upper and strip any trailing spaces
print(morse_code_graphic)
input_message = input("Input your standard message: ").upper().strip()

# Construct morse code
output_morse = convert_text_to_morse(input_message)

# Output Message
blnMessage_Written = False
while not blnMessage_Written:
    print("Original Message")
    print(input_message)
    print("Morse Code")
    print(INTRA_SPACE.join(output_morse))
    blnMessage_Written = True

print("Message encoded to morse code!")


