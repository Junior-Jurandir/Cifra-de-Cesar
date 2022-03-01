MODE_ENCRYPT = 1
MODE_DECRYPT = 0

#Está é a função responsavel por efetuar a encriptção e a decriptação.
def caesar(data, key, mode):
    #Declaramos a constante correspondente ao alfabeto e a variavel que irá receber a nova mensagem gerada através da encriptação e decriptação.
    alphabet = 'abcdefghijklmnopqrstuvwxyzàáãâéêóôõíúçABCDEFGHIJKLMNOPQRSTUVWXYZÀÁÃÂÉÊÓÔÕÍÚÇ'
    new_data = ''
    #A variavel c neste for representa cada caractere da mensagem que será lido e localizado pela função alphabet.find(c) e depois passara pelo processo selecionado pelo usuario.
    for c in data:
        index = alphabet.find(c)
        #caso o caractere seja uma pontuação ou um espaço ele sera mantido e inserido na nova mensagem
        if index == -1:
            new_data += c
        else:
            new_index = index + key if mode == MODE_ENCRYPT else index - key
            #A linha seguinte cuida para que caso após processo a nova localização esteja fora do alfabeto ela seja reencaminhada para dentro na localização correta e a seguinte adiciona o caractere correspondente à nova mensagem.
            new_index = new_index % len(alphabet)
            new_data += alphabet[new_index:new_index+1]
    return new_data

#Entradas
op = input ('Você deseja cifrar ou decifrar a mensagem? ')
key = int (input('Insira a chave: '))
if_file = input('Deseja inserir a mensagem através de um arquivo? ')
if if_file == 's' or if_file == 'sim':
    file1 = input('Digite o arquivo desejado (ele deve estar na mesma pasta que este): ')
    with open(str(file1), 'r', encoding = "utf-8") as arquivo:
        original = arquivo.read()
else:
    original = input('Digite a mensagem aqui: ')
#De acordo com a operação selecionada pelo usuario serão direcionados para a função caesar os dados necessarios para efetuar o processo selcionado e devolcver o resultado a ser apresentado. 
if (op == 'c') or (op == 'cifrar'):
    print('\n Original:', original)
    ciphered = caesar(original, key, MODE_ENCRYPT)
    print('\n Encriptada:', ciphered)
    print(' A mensagem cifrada será entregue no arquivo ciphered.txt')
    with open('ciphered.txt', 'a', encoding = 'utf-8') as arquivo:
        arquivo.write(ciphered)
        arquivo.write('\n')
elif (op == 'd') or (op == 'decifrar'):
    plain = caesar(original, key, MODE_DECRYPT)
    print('\n Decriptada:', plain)
    print(' A mensagem cifrada será entregue no arquivo deciphered.txt')
    with open('deciphered.txt', 'a', encoding = 'utf-8') as arquivo:
        arquivo.write(plain)
        arquivo.write('\n')
else:
    print ("Opção invalida\n por favor digite:\n 'cifrar' ou 'c' para cifrar\n ou 'decifrar' ou 'd' para decifrar")