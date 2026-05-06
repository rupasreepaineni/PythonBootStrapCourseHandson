alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
direction = input("Enter the direction you want to decode or encode: \n").lower()
shift = int(input("Type the shift number: \n"))

# creating function for shifting the letters
text = input("Enter the text \n").lower()
def caesar(original_text,shift_amount,direction):
    output_text =""
    for letter in original_text:
       if letter not in alphabets:
              output_text += letter
       else:
            if direction == "decode":
                shift_amount *= -1
                shifted_by = alphabets.index(letter) + shift_amount
                shifted_by %= len(alphabets)
                output_text += alphabets[shifted_by]
    print(f"Here is the {direction} text: {output_text}")
