from PySimpleGUI import PySimpleGUI as sg


#Funções
def CheckPassword(user, password):
    return user == 'admin' and password == 'admin'


#Janelas
def janela_login():
    # Layout
    sg.theme("Reddit")
    layoutLogin = [
        [sg.Text('Usuário\t'), sg.Input(key='usuario',size=(20,1))],
        [sg.Text('Senha\t'), sg.Input(key='senha', password_char='*',size=(20,1))],
        [sg.Checkbox('Salvar o login?')],
        [sg.Button('Entrar', key='entrar')]
    ]
    # Janela
    return sg.Window('Tela de Login', layoutLogin, finalize=True)

def janela_menu_principal():
    layoutMenuPrincipal = [
        [sg.Text('Sistema de Gerenciamento Empresarial',)],
        [sg.Button('Empregados')],
        [sg.Button('Sindicato')],
        [sg.Button('Pagamentos')],
        [sg.Text('Dia 08 de Outubro de 2020')]
    ]
    return sg.Window('Menu Principal', layoutMenuPrincipal, finalize=True)

def janela_menu_empregados():
    layoutMenuEmpregados = [
        [sg.Text('Gerenciamento de Empregados')],
        [sg.Button('Adicionar Empregado')],
        [sg.Button('Remover Empregado')],
        [sg.Button('Cartão de Ponto')],
        [sg.Button('Resultado de Venda')],
        [sg.Button('Editar Detalhes do Empregado')],
        [sg.Button('Voltar')]
    ]
    return sg.Window('Menu de Empregados', layoutMenuEmpregados, finalize=True)

def janela_menu_sindicato():
    layoutMenuSindicato = [
        [sg.Text('Gerenciamento do Sindicato')],
        [sg.Button('Taxa de Serviço', key='taxa')],
        [sg.Button('Lista de Afiliados', key='lista')],
        [sg.Button('Voltar')]
    ]
    return sg.Window('Menu do Sindicato', layoutMenuSindicato, finalize=True)

def janela_menu_pagamento():
    layoutMenuPagamento = [
        [sg.Text('Folha de Pagamento')],
        [sg.Button('Rodar Pagamento', key='pagamento')],
        [sg.Button('Agendas de Pagamento', key='agendas')],
        [sg.Button('Voltar')]
    ]
    return sg.Window('Menu de Pagamento', layoutMenuPagamento, finalize=True)

janelaLogin = janela_login()
janelaMenuPrincipal = None
janelaMenuEmpregado = None
janelaMenuSindicato = None
janelaMenuPagamento = None

# Eventos

while True:
    janela, evento, valores = sg.read_all_windows()
    print(janela,'|',evento,'|',valores)
# FECHAR JANELA
    if evento == sg.WIN_CLOSED:
        break
# TELA DE LOGIN
    if janela == janelaLogin:
        if evento == 'entrar':
            if CheckPassword(valores['usuario'], valores['senha']):
                janela.close()
                janelaMenuPrincipal = janela_menu_principal()
            else:
                sg.popup('Usuário ou senha incorretos',title='Erro no Login')

#######################################################################################################

# MENU PRINCIPAL
    if janela == janelaMenuPrincipal:
        if evento == 'Empregados':
            janela.close()
            janelaMenuEmpregado = janela_menu_empregados()

        elif evento == 'Sindicato':
            janela.close()
            janelaMenuSindicato = janela_menu_sindicato()

        elif evento == 'Pagamentos':
            janela.close()
            janelaMenuPagamento = janela_menu_pagamento()



#######################################################################################################

# MENU EMPREGADOS
    if janela == janelaMenuEmpregado:
        if evento == 'Voltar':
            janela.close()
            janelaMenuPrincipal = janela_menu_principal()


#######################################################################################################

# MENU SINDICATO
    if janela == janelaMenuSindicato:
        if evento == 'Voltar':
            janela.close()
            janelaMenuPrincipal = janela_menu_principal()
            

#######################################################################################################

# MENU PAGAMENTO
    if janela == janelaMenuPagamento:
        if evento == 'Voltar':
            janela.close()
            janelaMenuPagamento = janela_menu_principal()
