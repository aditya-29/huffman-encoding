# huffman-encoding
This repository contains code for basics of huffman encoding, decoding.


## functions:
- encode_dict
- encode
- decode
- size_saved

### encode_dict:
#### Usage : 
import huffman as h

freq_of_characters, enc_dict = h.encode_dict(input = string)
######
(type of enc_dict is "huffman_dict")

### encode:
#### Usage :
message = "huffman is awesome" 
###### 
enc_msg = h.encode(msg = message, dictionary = enc_dict)
######
(type of enc_msg is string)

### decode:
#### Usage :
dec_msg = h.decode(enc_msg = enc_msg, dictionary = enc_dict)
######
(type of dec_msg is string)

### size_saved:
#### Usage : 
h.size_saved(dictionary = enc_dict, msg = string, enc_msg = enc_string)

