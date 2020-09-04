import sys
from binarytree import build


class huffman:
    def __init__(self,string):
        self.string = string
    
    def __repr__(self):
        return "%s" % (self.string)

class huffman_dict:
    def __init__(self, dictionary):
        self.dictionary = dictionary

    def __iter__(self):
        return iter(self.dictionary.items())

    def items(self):
        return (self.dictionary.keys(), self.dictionary.values())
    def __repr__(self):
        return "%s" % (self.dictionary)



class Node:
    def __init__(self, left=None, right = None):
        self.left = left
        self.right = right

    def children(self):
        return (self.left, self.right)

    def __repr__(self):
        return "%s--%s" % (self.left, self.right)


def huffman_enc(values, left = True, code = ""):
    if type(values) !=Node:
        return {values : code}

    left, right = values.children()

    enc = {}
    
    enc.update(huffman_enc(left, True, code+"0"))
    enc.update(huffman_enc(right, False, code+"1"))

    return enc


def encode_dict(input):
    if type(input) != str:
        raise ValueError("The input is not of string type")
    freq = {}
    for i in input:
        if i in freq:
            freq[i] += 1
        else:
            freq[i] = 1

    freq = sorted(freq.items(),key = lambda x: x[1])
    values = freq.copy()
    # hist = []

    while len(values)>1:
        (v1, f1) = values.pop(0)
        (v2, f2) = values.pop(0)

        value = Node((v1), (v2))
        values.append((value, f1+f2))
        values = sorted(values,key = lambda x: x[1])

    enc = huffman_enc(values[0][0])
    enc = huffman_dict(enc)
    
    prob = {}
    l = len(input)
    for i in range(len(freq)):
        prob[freq[i][0]] = int(freq[i][1]) / l

    prob = huffman_dict(prob)
    return prob, enc

def encode(msg, dictionary):
    if msg == "":
        raise ValueError("The string is empty")
    if type(msg) != str:
        raise TypeError("The input is not of string type")
    if type(dictionary) != huffman_dict:
        raise TypeError("The input is not of huffman dictionary type")
    if dictionary.dictionary == {}:
        raise ValueError("The dictionary is empty")


    string = ""
    for e in msg:
        string+=dictionary.dictionary[e]
        string+=" "
    string = string[:-1]
    return string

def decode(enc_msg, dictionary):
    if enc_msg == "":
        raise ValueError("The string is empty")
    if type(enc_msg) != str:
        raise TypeError("The input is not of string type")
    if type(dictionary) != huffman_dict:
        raise TypeError("The input is not of huffman dictionary type")
    if dictionary.dictionary == {}:
        raise ValueError("The dictionary is empty")


    string = ""
    message = enc_msg.split(" ")
    key_list = list(dictionary.dictionary.keys())
    val_list = list(dictionary.dictionary.values())
    for i in message:
        string += key_list[val_list.index(i)]

    return string

def size_saved(dictionary, msg, enc_msg):
    if enc_msg == "" or msg == "": 
        raise ValueError("The string is empty")
    if type(enc_msg) != str or type(msg)!=str:
        raise TypeError("The input is not of string type")
    if type(dictionary) != huffman_dict:
        raise TypeError("The input is not of huffman dictionary type")
    if dictionary.dictionary == {}:
        raise ValueError("The dictionary is empty")

    msg_size = len(msg) * 8
    dict_size = 0
    for i in dictionary.dictionary:
        dict_size += 8
        dict_size += len(dictionary.dictionary[i])
    enc_msg_size = len(enc_msg) * 8

    space_saved = msg_size - dict_size - enc_msg_size

    print("****  all characters are assumed to take 8bits of space ****")
    print("Total space before encoding : ", msg_size)
    print("Total space after encoding : ", dict_size + enc_msg_size)
    print("space saved : ", space_saved, "(", round((space_saved/msg_size)*100,2),"%)", end = "\n\n")
    

def remove_spl_ch(string):
    if string == "":
        raise ValueError("The string is empty")
    if type(string) != str:
        raise TypeError("The input is not of string type")

    return "".join([e for e in string if e.isalnum()])


if __name__ == "__main__":
    input_str = str(input("enter the string to be encoded : "))
    enc_dict = encode_dict(input_str)
    enc_msg = encode(input_str, enc_dict)