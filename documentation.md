## 27-03-2026 -- premiers jets de code

Avant de commencer à coder, nous avons repéré les principaux problèmes que pourraient poser certaines lettres au moment de la conversion. Un problème auquel j'ai pensé mais que je n'ai pas réussi à anticiper dans le code : les digrammes.

Nous avons écrit un premier script pour essayer de convertir les caractères, en omettant les complexités linguistiques qui nous préoccuperont à des stades plus évolués du projet. 

**Le code :**

## Version 1 — conversion lettre par lettre
```python
dico_arabizi = {'a':'ا', 'b':'ب', 't': 'ت', 'j':'ج', '7':'ح', '5': 'خ', 'kh' :'خ', 'd':'د', 'dh':'ذ', 'r':'ر', 'z': 'ز', 's':'س', 'ch': 'ش', 'sh': 'ش', '3':'ع', '8':'غ', 'gh':'غ', 'f':'ف', '9':'ق', 'q':'ق', 'k':'ك', 'l':'ل', 'm':'م', 'n':'ن', 'h':'ه','ou':'و', 'u':'و', 'i':'ي', '2': 'ء'}

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
```
*Résultat du print :* ```كهoوyا```

**Problème identifié** : les digrammes (`kh`, `gh`, `sh`, `ch`, `dh`) sont traités comme deux caractères séparés au lieu d'un seul son.
