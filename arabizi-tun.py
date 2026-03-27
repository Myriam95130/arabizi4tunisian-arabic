dico_arabizi = {'a':'ا', 'b':'ب', 't': 'ت', 'j':'ج', '7':'ح', '5': 'خ', 'kh' :'خ', 'd':'د', 'dh':'ذ', 'r':'ر', 'z': 'ز', 's':'س', 'ch': 'ش', 'sh': 'ش', '3':'ع', '8':'غ', 'gh':'غ', 'f':'ف', '9':'ق', 'q':'ق', 'k':'ك', 'l':'ل', 'm':'م', 'n':'ن', 'h':'ه','ou':'و', 'u':'و', 'i':'ي', '2': 'ء'
                 }

def conv_lett(mot):
    mot_arabe = []
    for ch in mot:
        if ch in dico_arabizi.keys():
            ch = dico_arabizi[ch]
            mot_arabe.append(ch)
        elif ch not in dico_arabizi:
            mot_arabe.append(ch)
    return ''.join(mot_arabe)

print(conv_lett("khouya"))