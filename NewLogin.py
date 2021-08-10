from PySimpleGUI import PySimpleGUI as sg
from datetime import datetime as dt

#Classes
class LayoutController:
    def __init__(self, layout) -> None:
        self.LayoutAtivo = layout

    def get_layout(self) -> str:
        return self.LayoutAtivo
        
    def set_layout(self, layout) -> None:
        self.LayoutAtivo = layout

    def is_layout_active(self, layout) -> bool:
        return self.LayoutAtivo == layout
    
    def update_window_layout(self, janela, layoutNovo) -> None:
        janela[self.get_layout()].update(visible=False)
        self.set_layout(layoutNovo)
        janela[layoutNovo].update(visible=True)

    def reset_employee_menu(self) -> None:
        janela['MAE-NOME'].update('')
        janela['MAE-ENDERECO'].update('')
        janela['MAE-TIPODECONTRATO'].update('Assalariado')
        janela['MAE-SINDICATO'].update(False)
        janela['MAE-VALORSALARIO'].update('')
        janela['MAE-VALORCOMISSAO'].update('')
        lc.update_window_layout(janela, '-LayoutMenuEmpregados-')


#Funções
def CheckPassword(user, password):
    return user == 'admin' and password == 'admin'


#Janelas
def janela_login():
    #Theme
    sg.theme("Reddit")
    # Layout
    layoutLogin = [
        [sg.Text('Usuário\t'), sg.Input(key='usuario',size=(20,1))],
        [sg.Text('Senha\t'), sg.Input(key='senha', password_char='*',size=(20,1))],
        [sg.Checkbox('Salvar o login?')],
        [sg.Button('Entrar', key='entrar')]
    ]
    # Janela
    return sg.Window('Tela de Login', layoutLogin, finalize=True)

def janela_principal():
    layoutMenuPrincipal = [
        [sg.Text('Sistema de Gerenciamento Empresarial', justification='center')],
        [sg.Button('Empregados')],
        [sg.Button('Sindicato')],
        [sg.Button('Pagamentos')],
        [sg.Text('Dia 08 de Outubro de 2020', justification='center')]
    ]
    layoutMenuEmpregados = [
        [sg.Text('Gerenciamento de Empregados', justification='center')],
        [sg.Button('Adicionar Empregado', key='ME-ADICIONAR')],
        [sg.Button('Remover Empregado', key='ME-REMOVER')],
        [sg.Button('Cartão de Ponto', key='ME-PONTO')],
        [sg.Button('Resultado de Venda', key='ME-VENDA')],
        [sg.Button('Editar Detalhes do Empregado', key='ME-EDITAR')],
        [sg.Button('Voltar', key='voltar')]
    ]
    layoutMenuSindicato = [
        [sg.Text('Gerenciamento do Sindicato', justification='center')],
        [sg.Button('Taxa de Serviço', key='taxa')],
        [sg.Button('Lista de Afiliados', key='lista')],
        [sg.Button('Voltar', key='voltar')]
    ]
    layoutMenuPagamento = [
        [sg.Text('Folha de Pagamento', justification='center')],
        [sg.Button('Rodar Pagamento', key='pagamento')],
        [sg.Button('Agendas de Pagamento', key='agendas')],
        [sg.Button('Voltar', key='voltar')]
    ]
    layoutAdicionarEmpregado = [
        [sg.Frame('Dados Pessoais', [
                                    [sg.Column([[sg.Text('Nome')],
                                                [sg.Text('Endereço')]]),
                                    sg.Column([ [sg.Input(size=(30,1), key='MAE-NOME',)],
                                                [sg.Input(size=(30,1), key='MAE-ENDERECO')]])]
                                    ])
        ],
        [sg.Frame('Detalhes do Contrato', [[sg.Column([ [sg.Combo(values=('Por Hora', 'Assalariado', 'Comissionado'), default_value='Assalariado', readonly=True, key='MAE-TIPODECONTRATO',enable_events=True)],
                                                        [sg.Text('Salário', key='MAE-TEXTOSALARIO')],
                                                        [sg.Text('Comissão')]]),
                                            sg.Column([ [sg.Checkbox('Afiliado ao Sindicato', default=False, key='MAE-SINDICATO')],
                                                        [sg.Input(size=(20,1),key='MAE-VALORSALARIO')],
                                                        [sg.Input(size=(20,1),key='MAE-VALORCOMISSAO', disabled=True)]])]])
        ],
        [sg.Button('Cancelar', key='MAE-CANCELAR'), sg.Button('Confirmar', key='MAE-CONFIRMAR', )]
                                ]
    layoutFinal = [
        [
            sg.Column(layoutMenuPrincipal, key='-LayoutMenuPrincipal-', visible=True),
            sg.Column(layoutMenuEmpregados, key='-LayoutMenuEmpregados-', visible=False),
            sg.Column(layoutMenuSindicato, key='-LayoutMenuSindicato-', visible=False),
            sg.Column(layoutMenuPagamento, key='-LayoutMenuPagamento-', visible=False),
            sg.Column(layoutAdicionarEmpregado, key='-LayoutAdicionarEmpregado-', visible=False)
        ]
    ]

    return sg.Window('Software Empresarial', layoutFinal, finalize=True)

janelaLogin = janela_login()
janelaPrincipal = None
lc = LayoutController(None)

# Eventos

while True:
    janela, evento, valores = sg.read_all_windows()
    print(janela==janelaPrincipal,'|',evento,'|',valores)
# FECHAR JANELA
    if evento == sg.WIN_CLOSED:
        janela.close()
        break
# TELA DE LOGIN
    elif janela == janelaLogin:
        if evento == 'entrar':
            if CheckPassword(valores['usuario'], valores['senha']):
                janela.close()
                janelaPrincipal = janela_principal()
                lc.set_layout('-LayoutMenuPrincipal-')
            else:
                sg.popup('Usuário ou senha incorretos',title='Erro no Login')

#######################################################################################################

# MENU PRINCIPAL
    elif janela == janelaPrincipal and lc.is_layout_active('-LayoutMenuPrincipal-'):
        if evento == 'Empregados':
            lc.update_window_layout(janela,'-LayoutMenuEmpregados-')

        elif evento == 'Sindicato':
            lc.update_window_layout(janela,'-LayoutMenuSindicato-')

        elif evento == 'Pagamentos':
            lc.update_window_layout(janela,'-LayoutMenuPagamento-')
            


#######################################################################################################

# MENU EMPREGADOS
    elif janela == janelaPrincipal and lc.is_layout_active('-LayoutMenuEmpregados-'):
        if evento == 'ME-ADICIONAR':
            lc.update_window_layout(janela, '-LayoutAdicionarEmpregado-')

        elif evento[0:6] == 'voltar':
            lc.update_window_layout(janela, '-LayoutMenuPrincipal-')



#######################################################################################################

## SUB MENU ADICIONAR EMPREGADO
    elif janela == janelaPrincipal and lc.is_layout_active('-LayoutAdicionarEmpregado-'):
        if evento == 'MAE-TIPODECONTRATO':
            if valores['MAE-TIPODECONTRATO'] == 'Comissionado':
                janela['MAE-TEXTOSALARIO'].update(text='Salário Mensal')
                janela['MAE-VALORCOMISSAO'].update(disabled=False)
            
            elif valores['MAE-TIPODECONTRATO'] == 'Por Hora':
                janela['MAE-TEXTOSALARIO'].update(text='Valor da Hora\nde Trabalho')
                janela['MAE-VALORCOMISSAO'].update('')
            else:
                janela['MAE-TEXTOSALARIO'].update(text='Salário Mensal')
                janela['MAE-VALORCOMISSAO'].update('')
                janela['MAE-VALORCOMISSAO'].update(disabled=True)


        elif evento == 'MAE-CONFIRMAR':
            sg.popup(f"Funcionário {valores['MAE-NOME']} adicionado com sucesso!\nID: 001", title='')
            lc.reset_employee_menu()



        elif evento == 'MAE-CANCELAR':
            lc.reset_employee_menu()
        













#######################################################################################################

# MENU SINDICATO
    elif janela == janelaPrincipal and lc.is_layout_active('-LayoutMenuSindicato-'):
        if evento[0:6] == 'voltar':
            lc.update_window_layout(janela, '-LayoutMenuPrincipal-')


#######################################################################################################

# MENU PAGAMENTO
    elif janela == janelaPrincipal and lc.is_layout_active('-LayoutMenuPagamento-'):
        if evento[0:6] == 'voltar':
            lc.update_window_layout(janela, '-LayoutMenuPrincipal-')