import PySimpleGUI as sg


layout = [[
    sg.Frame('Dados Pessoais', 
    [[sg.Column([[sg.Text('Nome')],[sg.Text('Endereço')]]), 
    sg.Column([[sg.Input(size=(30,1), key='MAE-NOME')],[sg.Input(size=(30,1), key='MAE-ENDERECO')]])]]
    )
]]


sg.Window('test', layout, finalize=True)






[
                                            [,
                                            ], 
                                            [, ],
                                            [, ]
                                            ]