# Complete the function below.


def  condenseString( str):
    word_list, freq_list = [], []
    curr_char, curr_freq = str[0], 1
    for char in str[1:]:
        if char == curr_char:
            curr_freq += 1
        else:
            word_list.append(curr_char)
            freq_list.append(curr_freq)
            curr_char, curr_freq = char, 1
    cond_str = ''
    for i in range(len(word_list)):
        if freq_list[i] > 2:
            cond_str += str(freq_list[i]) + '@' + word_list[i]
        else:
            cond_str += word_list[i] * freq_list[i]
    return cond_str
        
_str = raw_input()

res = condenseString(_str);
print res