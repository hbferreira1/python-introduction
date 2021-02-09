import PySimpleGUI as sg
import sqlite3
from sqlite3 import Error


######criar conexão######
def ConexaoBanco():
    caminho="../Desktop/urna.sql"
    con = None
    try:
        conn= sqlite3.connect(caminho)
    except Error as ex:
        print(ex)
    return con

vcon = ConexaoBanco()            


######criando a janela######

class TelaPython:
    def __init__(self):
        sg.change_look_and_feel('DarkBlack')

        layout = [
            [sg.Text('Nome do candidato', size= (10,0)), sg.Input(size=(15,0), key='nome_candidato')],
            [sg.Text('código do candidato', size=(10,0)), sg.Input(size=(5,0), key= 'cod_candidato')],
            [sg.Text('codigo do cargo', size=(10,0)), sg.Input(size=(8,0), key= 'cod_carg')],
            [sg.Text('código do partido', size=(10,0)), sg.Input(size=(8,0), key= 'cod_partido')],
            [sg.Button('Cadastrar')],
            [sg.Output(size=(30,20))]
        ]

        self.janela = sg.Window('Cadastro de candidatos').layout(layout)

    def Iniciar(self):
        while True:
            self.button, self.values = self.janela.Read()
            nome_candidato = self.values['nome_candidato']
            cod_candidato = self.values['cod_candidato']
            cod_carg = self.values['cod_carg']
            cod_partido = self.values['cod_partido']
            print(f'nome_candidato: {nome_candidato}')
            print(f'cod_candidato: {cod_candidato}')
            print(f'cod_carg: {cod_carg}')
            print(f'cod_partido: {cod_partido}')

vsql="""INSERT INTO candidato 
            (nome_candidato, cod_candidato,cod_carg, cod_partido)"
        VALUES('nome_candidato', 'cod_candidato','cod_carg', 'cod_partido')"""

cursor.execute(vsql)

def inserir(conexao,sql):
    try:
        c=conexao.cursor()
        c.execute(sql)
        conexao.commit()
        print("Registro do candidato inserido")

    except Error as ex:
        print(ex)

inserir(vcon,vsql) 


conector.commit()
cursor.close()
conector.close()


tela = TelaPython()
tela.Iniciar()