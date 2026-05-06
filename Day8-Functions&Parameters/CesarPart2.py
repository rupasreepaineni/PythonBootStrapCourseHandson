#if we're using something then add inside function like modified_text,%= should be together

alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
direction = input("Enter the direction you want to decode or encode: \n").lower()
shift = int(input("Type the shift number: \n"))

# creating function for shifting the letters
text = input("Enter the text \n").lower()
def encrypt(original_text,shift_amount):
    modified_text=""
    for letter in original_text:
        shifted_by = alphabets.index(letter)+shift_amount
        shifted_by %= len(alphabets)
        modified_text += alphabets[shifted_by]
    print(f"Here is the encoded text: {modified_text}")


#here we're decoding the text by shifting the letters in opposite direction
def decrypt(original_text,shift_amount):
    dec_text = ""
    for letter in original_text:
        shift = alphabets.index(letter) - shift_amount
        shift %= len(alphabets)
        dec_text += alphabets[shift]
    print(f"Here is the decoded text: {dec_text}")




# creating function for shifting the letters
encrypt(original_text = text, shift_amount = shift)

