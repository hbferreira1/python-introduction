import PySimpleGUI as sg

class TelaPython:
    def __init__(self):
        sg.change_look_and_feel('DarkBlack')

        layout = [
            [sg.Text('Título de eleitor', size= (10,0)), sg.Input(size=(15,0), key='tit_eleitor')],
            [sg.Text('Voto para presidente', size=(10,0)), sg.Input(size=(5,0), key= 'presidente')],
            [sg.Text('Voto para governador', size=(10,0)), sg.Input(size=(8,0), key= 'governador')],
            [sg.Text('Voto para Deputado Federal', size=(10,0)), sg.Input(size=(8,0), key= 'deputado_federal')],
            [sg.Text('Voto para Deputado Estadual', size=(10,0)), sg.Input(size=(8,0), key = 'deputado_estadual')],
            [sg.Text('Voto para Senador', size=(10,0)), sg.Input(size=(8,0), key = 'senador')],
            [sg.Button('Finalizar')],
            [sg.Output(size=(40,20))]
        ]

        self.janela = sg.Window('Urna eletrônica').layout(layout)

    def Iniciar(self):
        while True:
            self.button, self.values = self.janela.Read()
            tit_eleitor = self.values['tit_eleitor']
            voto_presidente = self.values['presidente']
            voto_governador = self.values['governador']
            voto_depfe = self.values['depfe']
            voto_depes = self.values['depes']
            voto_senador = self.values['senador']
            print(f'tit_eleitor: {tit_eleitor}')
            print(f'voto_presidente: {voto_presidente}')
            print(f'voto_presidente: {voto_presidente}')
            print(f'voto_governador: {voto_governador}')
            print(f'voto_depfe: {voto_depfe}')
            print(f'voto_depes: {voto_depes}')
            print(f'voto_senador: {voto_senador}')


tela = TelaPython()
tela.Iniciar()