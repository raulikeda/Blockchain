from hashcoin import testNonce, mountCoinbase, mountTransaction

# Atencao: abaixo apenas um exemplo

# Exemplo do no 1:
previous = '00000000'
coinbase = mountCoinbase('RI', 200)
transactions = []

# Chute do nonce:
nonce = 1

hash = testNonce(previous, nonce, coinbase, transactions)

# Verifique o numero de zeros a esquerda
print(hash)

###########################################################################

# Exemplo do no 2:

previous = hash
coinbase = mountCoinbase('FR', 200)
transactions = [mountTransaction('RI', 'FR', 150)]

# Chute do nonce:
nonce = 1

hash = testNonce(previous, nonce, coinbase, transactions)

# Verifique o numero de zeros a esquerda
print(hash)

