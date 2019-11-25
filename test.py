from des import des
from code import apsDB



apscursor = apsDB.cursor()
insert = "INSERT INTO aps.aps_table (login, senha) VALUES (%s, %s)"

if __name__ == '__main__':
     inputkey = open("key.txt", 'r')
     key = inputkey.read()
     user = input("Digite seu usuário: ")
     textin= input("Digite sua mensagem de 8 digitos: ")
     d = des()
     r = d.encrypt(key,textin)
     senhah = ("(r)", r)
     passDB = """SELECT senha FROM aps_table WHERE login = '%s' """  (user)
     apscursor.execute(passDB)
     senhadb = apscursor.fetchone()

    if str(senhadb) == str(senhah):
        print("Login feito com sucesso!")
        print("Sua senha cifrada é: ", senhah)
        d = des()
        r = d.encrypt(key,textin)
        r2 = d.decrypt(key,r)
        print("Sua mensagem decifrada é: ", r2)
