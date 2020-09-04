# huffman-encoding
This repository contains code for basics of huffman encoding, decoding.


## functions:
- remove_spl_ch
- encode_dict
- encode
- decode
- size_saved



### remove_spl_ch:
#### Usage : 
import huffman as h\
string = "message@123"\
string = h.remove_spl_ch(string)\
(returns "message123")

### encode_dict:
#### Usage : 

prob_of_characters, enc_dict = h.encode_dict(input = string)
######
prob_of_characters is the probability map
######
(type of prob_of_characters and enc_dict is "huffman_dict")

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

