from hashcoin import testNonce, mountCoinbase, mountTransaction

# Atencao: abaixo apenas um exemplo

# Exemplo: 
#
# previous = '00000000'
# coinbase = mountCoinbase('A', 200)
# transactions = [mountTransaction('B', 'C', 50)]

previous = ''
coinbase = mountCoinbase('', 200)
transactions = []

# Chute do nonce:
nonce = 1 # Variar o chute até achar o padrão solicitado

hash = testNonce(previous, nonce, coinbase, transactions)
print(hash)

# Verifique o numero de zeros a esquerda
if hash[:4] == '0000': # Por exemplo 4 zeros à esquerda
    print('OK!')
else:
    print('Not Ok')
