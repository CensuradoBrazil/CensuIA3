from modules.expansion import CensuradoIAExpansion

expansion = CensuradoIAExpansion()

text = 'a handsome man'

for i in range(64):
    print(expansion(text, seed=i))
