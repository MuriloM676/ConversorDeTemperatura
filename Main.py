import PySimpleGUI

class TelaPython:
    def __init__(self):
        # Layout
        layout = [
            [PySimpleGUI.Text('Temperatura em °C',size=(17,0)),PySimpleGUI.Input(size=(15,0),key='tempC')],
            [PySimpleGUI.Text('Converter para:',size=(15,0))],
            [PySimpleGUI.Radio('Fahrenheit', 'temp',key='fah'),PySimpleGUI.Radio('Kelvin', 'temp',key='kel')],
            [PySimpleGUI.Button('Converter')],
            [PySimpleGUI.Output(size=(30,2))]
        ]
        self.janela = PySimpleGUI.Window("Conversor").layout(layout)

    def Iniciar(self):
        while True:
            # Extrair dados da tela
            self.button, self.values = self.janela.Read()
            tempC = float(self.values['tempC'])
            fah = self.values['fah']
            kel = self.values['kel']

            if (fah == True):
                F = tempC * (9 / 5) + 32               
                print('Valor em Fahrenheit: {0}°F'.format(F))

            if (kel == True):
                K = tempC + 273.15
                print('Valor em Kelvin: {0}°K.'.format(K))
tela = TelaPython()
tela.Iniciar()