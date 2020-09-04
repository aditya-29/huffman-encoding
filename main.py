import os
import huffman as h


# to convert the text file into string format
string = ""
file_name = "./sample.txt"
if not os.path.exists(file_name):
    print("the given file doesn't exist")
with open("sample.txt", "rb") as fil:
    string+=str(fil.read())



# custom message to be encoded (optional)
message = "huffman123.234  456"


#removing all special characters (optional)
string = h.remove_spl_ch(string)
message = h.remove_spl_ch(message)



# to create the huffman map
prob_of_characters, enc_dict = h.encode_dict(input = string)

print("\nencoded dictionary  : ", end = "\n\n")

for key, value in enc_dict:
    print(key, " : ",value)

print("\n\n")
print("probability of characters : ", end = "\n\n")
for key, value in prob_of_characters:
    print(key, " : ",value)
print("\n\n")


# to encode the message(custom) using the huffman map
enc_msg = h.encode(msg = message, dictionary = enc_dict)
print("encoded message : ", enc_msg, end = "\n\n")


# to encode the original string using huffman map
enc_string = h.encode(msg = message, dictionary = enc_dict)

# to decode the encoded message using huffman map
dec_msg = h.decode(enc_msg = enc_msg, dictionary = enc_dict)
print("decoded message : ", dec_msg, end = "\n\n")

# to get information about the space saved
h.size_saved(dictionary = enc_dict, msg = string, enc_msg = enc_string)






    