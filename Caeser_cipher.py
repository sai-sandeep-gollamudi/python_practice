alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
            'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def encode(message,shift):
    result = ""
    for i in message:
        if i in alphabet:
            ind_num = alphabet.index(i)
            c = ind_num+shift
            if(c<26):
                result += alphabet[c]
            else:
                result += alphabet[(c-26)]
        else:
            result += i
    return result

def decode(message,shift):
    result = ""
    for i in message:
        if i in alphabet:
            ind_num = alphabet.index(i)
            c = ind_num - shift
            if (c < 26):
                result += alphabet[c]
            else:
                result += alphabet[(c-26)]
        else:
            result += i
    return result


while(True):
    user_choice = input("Type 'encode' to encrypt or type 'decode' to decrypt: ").lower()
    message=input("Enter the message: ").lower()
    shift = int(input("Enter the shift number: "))
    if(shift>26):
        shift = shift%26

    if(user_choice == "encode"):
         output = encode(message,shift)
         print(f"The encryption for '{message}' will be '{output}'.")

    elif(user_choice == "decode"):
        output = decode(message,shift)
        print(f"The decryption for '{message}' will be '{output}'.")

    else:
        print("Invalid choice.")

    ra = input("Do you want to encode/decode again? Type yes or no: ")
    if(ra not in ['yes','YES','Yes']):
        print("See you again!")
        break

