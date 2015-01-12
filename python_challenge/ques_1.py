import string


def main():
    # string = """g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle 
    #          gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle 
    #          qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj"""
    cipher_text = """g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq 
                    ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle 
                    qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."""

    apply_shift(cipher_text)



def apply_shift(cipher_text):
    dict_sub = {}
    for i in range(26):
        dict_sub[string.ascii_lowercase[i]] = string.ascii_lowercase[(i+2)%26]

    dict_sub_trans = str.maketrans(dict_sub)
    
    #dict_sub_trans = dict((k*2, v) for k,v in dict_sub_trans.items())
    # print(dict_sub_trans)

    print("\ncipher text: ")
    print (cipher_text)

    plain_text = cipher_text.translate(dict_sub_trans)

    print("\nplain text(?): ")
    print(plain_text)



if __name__ == '__main__':
	main()