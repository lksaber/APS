from cx_Freeze import setup, Executable
import mysql.connector
from des import des
# coding: utf-8


apsDB = mysql.connector.connect(
    host="aurorahorizon.ddns.net",
    user="lucas",
    password="teste123456789",
    database="aps"
    )

apscursor = apsDB.cursor()
insert = "INSERT INTO aps.aps_table (login, senha) VALUES (%s, %s)"

if __name__ == '__main__':

    inputkey = open("key.txt", 'r')
    key = inputkey.read()
    confirm = 0
    confirm1 = 0

    print("\nEscolha o que deseja fazer")
    while confirm == 0:

        print("\n[1]Login\n[2]Criar um usuario\n[3]Decifrar mensagem\n[4]Sair")

        escolha = int(input("\nDigite sua escolha: "))
        if escolha == 1:
            print("Você escolheu fazer login")
            confirm = 1
            user = input("Digite seu usuário: ")
            textin= input("Digite sua mensagem de 8 digitos: ")
            d = des()
            r = d.encrypt(key,textin)
            senhah = ("( r)",  r)
            passDB ="""SELECT senha FROM aps_table WHERE login = '%s' """ (user)
            apscursor.execute(passDB)
            senhadb = apscursor.fetchone()

            if str(senhadb) == str(senhah):
                print("Login feito com sucesso!")
                print("Sua senha cifrada é: ", senhah)
                d = des()
                r = d.encrypt(key,textin)
                r2 = d.decrypt(key,r)
                print("Sua mensagem decifrada é: ", r2)

            else:
                print("Usuário ou senha incorretos!")




        elif escolha == 2:
            confirm = 1
            user = input("Digite seu usuário: ")
            textin= input("digite a mensagem cifrada: ")
            d = des()
            r = d.encrypt(key,textin)
            r2 = d.decrypt(key,r)
            passDB = """SELECT senha FROM aps_table WHERE login = '%s' """ % (user)
            apscursor.execute(passDB)
            senhadb = apscursor.fetchone()

            print("Sua mensagem decifrada é: ", r2)

        elif escolha == 3:
            print("Você escolheu cria uma nova conta")
            newuser = input("Digite seu usuário: ")
            while confirm1 == 0:
                text= input("Digite sua senha de 8 digitos: ")
                textconfirm= input("Digite sua senha de 8 digitos novamente: ")
                if text == textconfirm:
                    d = des()
                    r = d.encrypt(key,text)
                    crypt = r
                    confirm1 = 1
                    insert = "INSERT INTO aps_table (login, senha) VALUES (%s, %s)"
                    val = (newuser, crypt)
                    apscursor.execute(insert, val)
                    apsDB.commit()
                    print(apscursor.rowcount, "usuário criado com sucesso!.")
                else:
                    print("As senhas não correspondem")

        elif escolha == 4:
            print("Você escolheu sair do programa.\nObrigado por usar!")
            confirm = 1
        else:
            print("Digite uma opção válida")
            confirm = 0



