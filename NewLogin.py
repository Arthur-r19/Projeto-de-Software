from PySimpleGUI import PySimpleGUI as sg


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
        [sg.Button('Adicionar Empregado')],
        [sg.Button('Remover Empregado')],
        [sg.Button('Cartão de Ponto')],
        [sg.Button('Resultado de Venda')],
        [sg.Button('Editar Detalhes do Empregado')],
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
    layoutFinal = [
        [
            sg.Column(layoutMenuPrincipal, key='-LayoutMenuPrincipal-', visible=True),
            sg.Column(layoutMenuEmpregados, key='-LayoutMenuEmpregados-', visible=False),
            sg.Column(layoutMenuSindicato, key='-LayoutMenuSindicato-', visible=False),
            sg.Column(layoutMenuPagamento, key='-LayoutMenuPagamento-', visible=False)
        ]
    ]

    return sg.Window('Menu de Pagamento', layoutFinal, finalize=True)

janelaLogin = janela_login()
janelaPrincipal = None
lc = LayoutController('-LayoutMenuPrincipal-')

# Eventos

while True:
    janela, evento, valores = sg.read_all_windows()
    print(janela,'|',evento,'|',valores)
# FECHAR JANELA
    if evento == sg.WIN_CLOSED:
        janela.close()
        break
# TELA DE LOGIN
    if janela == janelaLogin:
        if evento == 'entrar':
            if CheckPassword(valores['usuario'], valores['senha']):
                janela.close()
                janelaPrincipal = janela_principal()
            else:
                sg.popup('Usuário ou senha incorretos',title='Erro no Login')

#######################################################################################################

# MENU PRINCIPAL
    if janela == janelaPrincipal and lc.is_layout_active('-LayoutMenuPrincipal-'):
        if evento == 'Empregados':
            lc.update_window_layout(janela,'-LayoutMenuEmpregados-')

        elif evento == 'Sindicato':
            lc.update_window_layout(janela,'-LayoutMenuSindicato-')

        elif evento == 'Pagamentos':
            lc.update_window_layout(janela,'-LayoutMenuPagamento-')
            


#######################################################################################################

# MENU EMPREGADOS
    if janela == janelaPrincipal and lc.is_layout_active('-LayoutMenuEmpregados-'):
        if evento[0:6] == 'voltar':
            lc.update_window_layout(janela, '-LayoutMenuPrincipal-')


#######################################################################################################

# MENU SINDICATO
    if janela == janelaPrincipal and lc.is_layout_active('-LayoutMenuSindicato-'):
        if evento[0:6] == 'voltar':
            lc.update_window_layout(janela, '-LayoutMenuPrincipal-')


#######################################################################################################

# MENU PAGAMENTO
    if janela == janelaPrincipal and lc.is_layout_active('-LayoutMenuPagamento-'):
        if evento[0:6] == 'voltar':
            lc.update_window_layout(janela, '-LayoutMenuPrincipal-')