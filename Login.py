from PySimpleGUI import PySimpleGUI as sg
from datetime import datetime as dt
from company import Company as company
from syndicate import Syndicate as syndicate
from employee import Employee, HoulyEmployee as Hemployee, SalaryEmployee as Semployee, CommissionedEmployee as Cemployee
import re

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

    def reset_employee_menu(self, keyprefix) -> None:
        janela[keyprefix+'-NOME'].update('')
        janela[keyprefix+'-ENDERECO'].update('')
        janela[keyprefix+'-TIPODECONTRATO'].update('Assalariado')
        janela[keyprefix+'-SINDICATO'].update(False)
        janela[keyprefix+'-VALORSINDICATO'].update('')
        janela[keyprefix+'-VALORSINDICATO'].update(disabled=True)
        janela[keyprefix+'-VALORSALARIO'].update('')
        janela[keyprefix+'-VALORCOMISSAO'].update('')
        janela[keyprefix+'-VALORCOMISSAO'].update(disabled=True)
    
    def import_employee_menu(self, employee):
        janela['MEE-NOME'].update(employee.name)
        janela['MEE-ENDERECO'].update(employee.adress)
        janela['MEE-TIPODECONTRATO'].update(employee.category)
        janela['MEE-VALORCOMISSAO'].update('')
        janela['MEE-VALORCOMISSAO'].update(disabled=True)
        janela['MEE-TEXTOSALARIO'].update('Salário Mensal')

        if employee.category == 'Assalariado':
            janela['MEE-VALORSALARIO'].update(employee.salary)

        elif employee.category == 'Comissionado':
            janela['MEE-VALORSALARIO'].update(employee.salary)
            janela['MEE-VALORCOMISSAO'].update(employee.commission)
            janela['MEE-VALORCOMISSAO'].update(disabled=False)

        elif employee.category == 'Horista':
            janela['MEE-TEXTOSALARIO'].update('Valor da Hora')
            janela['MEE-VALORSALARIO'].update(employee.wage)

        if employee.sid == -1:
            janela['MEE-SINDICATO'].update(False)
            janela['MEE-VALORSINDICATO'].update('')
            janela['MEE-VALORSINDICATO'].update(disabled=True)
        else:
            janela['MEE-SINDICATO'].update(True)
            janela['MEE-VALORSINDICATO'].update(employee.mfee)
            janela['MEE-VALORSINDICATO'].update(disabled=False)





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
    data = dt.now()
    layoutMenuPrincipal = [
        [sg.Text('Sistema de Gerenciamento Empresarial', justification='center')],
        [sg.Button('Empregados')],
        [sg.Button('Sindicato')],
        [sg.Button('Pagamentos')],
        [sg.Text(f'Hoje é {data.day}/{data.month}/{data.year}', justification='center')]
    ]
    layoutMenuEmpregados = [
        [sg.Text('Gerenciamento de Empregados', justification='center')],
        [sg.Button('Adicionar Empregado', key='ME-ADICIONAR')],
        #[sg.Button('Remover Empregado', key='ME-REMOVER')],
        [sg.Button('Cartão de Ponto', key='ME-PONTO')],
        [sg.Button('Resultado de Venda', key='ME-VENDA')],
        [sg.Button('Lista de Empregados', key='ME-LISTA')],
        [sg.Button('Voltar', key='voltar')]
    ]
    layoutMenuSindicato = [
        [sg.Text('Gerenciamento do Sindicato', justification='center')],
        [sg.Button('Taxa de Serviço', key='MS-TAXA')],
        [sg.Button('Lista de Afiliados', key='MS-LISTA')],
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
        [sg.Frame('Detalhes do Contrato', [[sg.Column([ [sg.Combo(values=('Horista', 'Assalariado', 'Comissionado'), default_value='Assalariado', readonly=True, key='MAE-TIPODECONTRATO',enable_events=True)],
                                                        [sg.Text(text='Salário Mensal', key='MAE-TEXTOSALARIO')],
                                                        [sg.Text('Comissão')],
                                                        [sg.Text('Tarifa Sindical')]
                                                        ]),
                                            sg.Column([ [sg.Checkbox('Afiliado ao Sindicato', default=False, key='MAE-SINDICATO', enable_events=True)],
                                                        [sg.Input(size=(20,1),key='MAE-VALORSALARIO')],
                                                        [sg.Input(size=(20,1),key='MAE-VALORCOMISSAO', disabled=True)],
                                                        [sg.Input(size=(20,1),key='MAE-VALORSINDICATO', disabled=True)]
                                                        ])]])
        ],
        [sg.Button('Cancelar', key='MAE-CANCELAR'), sg.Button('Confirmar', key='MAE-CONFIRMAR')]
                                ]
    layoutEditarEmpregado = [
        [sg.Frame('Dados Pessoais', [
                                    [sg.Column([[sg.Text('Nome')],
                                                [sg.Text('Endereço')]]),
                                    sg.Column([ [sg.Input(size=(30,1), key='MEE-NOME',)],
                                                [sg.Input(size=(30,1), key='MEE-ENDERECO')]])]
                                    ])
        ],
        [sg.Frame('Detalhes do Contrato', [[sg.Column([ [sg.Combo(values=('Horista', 'Assalariado', 'Comissionado'), default_value='Assalariado', readonly=True, key='MEE-TIPODECONTRATO',enable_events=True)],
                                                        [sg.Text(text='Salário Mensal', key='MEE-TEXTOSALARIO')],
                                                        [sg.Text('Comissão')],
                                                        [sg.Text('Tarifa Sindical')]
                                                        ]),
                                            sg.Column([ [sg.Checkbox('Afiliado ao Sindicato', default=False, key='MEE-SINDICATO', enable_events=True)],
                                                        [sg.Input(size=(20,1),key='MEE-VALORSALARIO')],
                                                        [sg.Input(size=(20,1),key='MEE-VALORCOMISSAO', disabled=True)],
                                                        [sg.Input(size=(20,1),key='MEE-VALORSINDICATO', disabled=True)]
                                                        ])]])
        ],
        [sg.Button('Cancelar', key='MEE-CANCELAR'), sg.Button('Confirmar', key='MEE-CONFIRMAR')]
                                ]
    layoutFinal = [
        [
            sg.Column(layoutMenuPrincipal, key='-LayoutMenuPrincipal-', visible=True),
            sg.Column(layoutMenuEmpregados, key='-LayoutMenuEmpregados-', visible=False),
            sg.Column(layoutMenuSindicato, key='-LayoutMenuSindicato-', visible=False),
            sg.Column(layoutMenuPagamento, key='-LayoutMenuPagamento-', visible=False),
            sg.Column(layoutAdicionarEmpregado, key='-LayoutAdicionarEmpregado-', visible=False),
            sg.Column(layoutEditarEmpregado, key='-LayoutEditarEmpregado-', visible=False)
        ]
    ]

    return sg.Window('Software Empresarial', layoutFinal, finalize=True)

def janela_lista(titulo,dicionario: dict):
    lista = []
    id = -1
    for key, employee in dicionario.items():
        lista.append(f'{key}\t: {employee.name}')
    layout = [
        [sg.Listbox(values= lista, size=(30,12),key='L-LISTA', enable_events=True),
        sg.Button('Editar\nDetalhes do\nEmpregado', key='L-EDITAR', size=(12,3)),
        sg.Button('Demitir\nEmpregado', key='L-REMOVER', size=(12,3))],
        [sg.Button('Voltar', key='L-VOLTAR')]
    ]
    window = sg.Window(titulo, layout=layout, modal=True)
    while True:
        evento, valores = window.read()
        if evento == "Exit" or evento == sg.WIN_CLOSED or evento == 'L-VOLTAR':
            id = -1
            break
        
        elif evento == 'L-EDITAR' or evento == 'L-REMOVER':
            if len(valores['L-LISTA']) != 0:
                id = re.findall('\d+', valores['L-LISTA'][0])[0]
                break
            else:
                sg.popup('Nenhum empregado selecionado.', title='')

    window.close()
    return (int(id), evento)


###############################################################################

# Ready

janelaLogin = janela_login()
janelaPrincipal = None
lc = LayoutController(None)
Empresa = company()
Sindicato = syndicate()
selectedId = -1
selectedSid = -1
# Eventos
while True:
    janela, evento, valores = sg.read_all_windows()
    print(janela==janelaPrincipal,'|',evento)
# FECHAR JANELA
    if evento == "Exit" or evento == sg.WIN_CLOSED:
        print(f'Fechando janela {janela}')
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

        elif evento == 'ME-LISTA':
            selectedId, chave = janela_lista('Lista de Empregados', Empresa.employeesList)
            if selectedId != -1 and chave == 'L-EDITAR':
                selectedEmployee = Empresa.employeesList.get(selectedId)
                selectedSid = selectedEmployee.sid
                lc.import_employee_menu(selectedEmployee)
                lc.update_window_layout(janela, '-LayoutEditarEmpregado-')
            elif selectedId != -1 and chave == 'L-REMOVER':
                selectedEmployee = Empresa.employeesList.get(selectedId)
                selectedSid = selectedEmployee.sid
                Empresa.remove_employee(selectedId)
                if selectedSid != -1:
                    Sindicato.remove_affiliate(selectedSid)
                sg.popup(f'Empregado {selectedEmployee.name} demitido!')
            else:
                pass
            continue

        elif evento[0:6] == 'voltar':
            lc.update_window_layout(janela, '-LayoutMenuPrincipal-')



#######################################################################################################

## SUB MENU ADICIONAR EMPREGADO
    elif janela == janelaPrincipal and lc.is_layout_active('-LayoutAdicionarEmpregado-'):
        if evento == 'MAE-TIPODECONTRATO':
            if valores['MAE-TIPODECONTRATO'] == 'Comissionado':
                janela['MAE-TEXTOSALARIO'].update('Salário Mensal')
                janela['MAE-VALORCOMISSAO'].update(disabled=False)
            
            elif valores['MAE-TIPODECONTRATO'] == 'Horista':
                janela['MAE-TEXTOSALARIO'].update('Valor da Hora')
                janela['MAE-VALORCOMISSAO'].update('')
                janela['MAE-VALORCOMISSAO'].update(disabled=True)
            else:
                janela['MAE-TEXTOSALARIO'].update('Salário Mensal')
                janela['MAE-VALORCOMISSAO'].update('')
                janela['MAE-VALORCOMISSAO'].update(disabled=True)

        elif evento == 'MAE-SINDICATO':
            if valores['MAE-SINDICATO']:
                janela['MAE-VALORSINDICATO'].update(disabled=False)
            else:
                janela['MAE-VALORSINDICATO'].update('')
                janela['MAE-VALORSINDICATO'].update(disabled=True)

        elif evento == 'MAE-CONFIRMAR':
            #verificar se os campos estão preenchidos
            if valores['MAE-NOME'] == '' or valores['MAE-ENDERECO'] == '':
                sg.popup('Preencha todos os Dados Pessoais!', title='Dados Incompletos')
            
            elif valores['MAE-VALORSALARIO'] == '':
                sg.popup('Preencha todos os Detalhes do Contrato!', title='Dados Incompletos')

            elif valores['MAE-TIPODECONTRATO'] == 'Comissionado' and valores['MAE-VALORCOMISSAO'] == '':
                sg.popup('Preencha todos os Detalhes do Contrato!', title='Dados Incompletos')

            elif valores['MAE-SINDICATO'] and valores['MAE-VALORSINDICATO'] == '':
                sg.popup('Preencha todos os Detalhes do Contrato!', title='Dados Incompletos')

            else:
                if valores['MAE-TIPODECONTRATO'] == 'Horista':
                    newemployee = Hemployee(valores['MAE-NOME'], valores['MAE-ENDERECO'], valores['MAE-TIPODECONTRATO'], valores['MAE-VALORSALARIO'])
                elif valores['MAE-TIPODECONTRATO'] == 'Assalariado':
                    newemployee = Semployee(valores['MAE-NOME'], valores['MAE-ENDERECO'], valores['MAE-TIPODECONTRATO'], valores['MAE-VALORSALARIO'])
                elif valores['MAE-TIPODECONTRATO'] == 'Comissionado':  
                    newemployee = Cemployee(valores['MAE-NOME'], valores['MAE-ENDERECO'], valores['MAE-TIPODECONTRATO'], valores['MAE-VALORSALARIO'], valores['MAE-VALORCOMISSAO'])
                
                Empresa.add_employee(newemployee)
                if valores['MAE-SINDICATO']:
                    newemployee.mfee = int(valores['MAE-VALORSINDICATO'])
                    Sindicato.add_affiliate(newemployee)
                
                sg.popup(f"Funcionário {valores['MAE-NOME']} adicionado com sucesso!\nID: {newemployee.id}", title='Cadastro Concluído')
                lc.reset_employee_menu('MAE')
                lc.update_window_layout(janela, '-LayoutMenuEmpregados-')


        elif evento == 'MAE-CANCELAR':
            lc.reset_employee_menu('MAE')
            lc.update_window_layout(janela, '-LayoutMenuEmpregados-')

#######################################################################################################

## SUB MENU EDITAR EMPREGADO

    elif janela == janelaPrincipal and lc.is_layout_active('-LayoutEditarEmpregado-'):
        if evento == 'MEE-TIPODECONTRATO':
            if valores['MEE-TIPODECONTRATO'] == 'Comissionado':
                janela['MEE-TEXTOSALARIO'].update('Salário Mensal')
                janela['MEE-VALORCOMISSAO'].update(disabled=False)
            
            elif valores['MEE-TIPODECONTRATO'] == 'Horista':
                janela['MEE-TEXTOSALARIO'].update('Valor da Hora')
                janela['MEE-VALORCOMISSAO'].update('')
                janela['MEE-VALORCOMISSAO'].update(disabled=True)
            else:
                janela['MEE-TEXTOSALARIO'].update('Salário Mensal')
                janela['MEE-VALORCOMISSAO'].update('')
                janela['MEE-VALORCOMISSAO'].update(disabled=True)

        elif evento == 'MEE-SINDICATO':
            if valores['MEE-SINDICATO']:
                janela['MEE-VALORSINDICATO'].update(disabled=False)
            else:
                janela['MEE-VALORSINDICATO'].update('')
                janela['MEE-VALORSINDICATO'].update(disabled=True)

        elif evento == 'MEE-CONFIRMAR':
            #verificar se os campos estão preenchidos
            if valores['MEE-NOME'] == '' or valores['MEE-ENDERECO'] == '':
                sg.popup('Preencha todos os Dados Pessoais!', title='Dados Incompletos')
            
            elif valores['MEE-VALORSALARIO'] == '':
                sg.popup('Preencha todos os Detalhes do Contrato!', title='Dados Incompletos')

            elif valores['MEE-TIPODECONTRATO'] == 'Comissionado' and valores['MEE-VALORCOMISSAO'] == '':
                sg.popup('Preencha todos os Detalhes do Contrato!', title='Dados Incompletos')

            elif valores['MEE-SINDICATO'] and valores['MEE-VALORSINDICATO'] == '':
                sg.popup('Preencha todos os Detalhes do Contrato!', title='Dados Incompletos')


            else:
                print('apertei confirmar?')
                print(f'id:{selectedId} sid:{selectedSid}')
                if valores['MEE-TIPODECONTRATO'] == 'Horista':
                    editemployee = Hemployee(valores['MEE-NOME'], valores['MEE-ENDERECO'], valores['MEE-TIPODECONTRATO'], valores['MEE-VALORSALARIO'])
                    editemployee.workedtime = Empresa.employeesList.get(selectedId).workedtime

                elif valores['MEE-TIPODECONTRATO'] == 'Assalariado':
                    editemployee = Semployee(valores['MEE-NOME'], valores['MEE-ENDERECO'], valores['MEE-TIPODECONTRATO'], valores['MEE-VALORSALARIO'])

                elif valores['MEE-TIPODECONTRATO'] == 'Comissionado': 
                    editemployee = Cemployee(valores['MEE-NOME'], valores['MEE-ENDERECO'], valores['MEE-TIPODECONTRATO'], valores['MEE-VALORSALARIO'], valores['MEE-VALORCOMISSAO'])

                editemployee.id = selectedId
                Empresa.edit_employee(selectedId, editemployee)
                if valores['MEE-SINDICATO'] and selectedSid != -1:
                    editemployee.sid = selectedSid
                    editemployee.mfee = int(valores['MEE-VALORSINDICATO'])
                    Sindicato.edit_affiliate(selectedSid, editemployee)

                elif valores['MEE-SINDICATO'] and selectedSid == -1:
                    editemployee.mfee = int(valores['MEE-VALORSINDICATO'])
                    Sindicato.add_affiliate(editemployee)
                
                elif not valores['MEE-SINDICATO'] and selectedSid != -1:
                    Sindicato.remove_affiliate(selectedSid)
                
                else:
                    pass
                
                print(editemployee)
                
                sg.popup(f"Funcionário alterado para {editemployee.name} com sucesso!\nID: {editemployee.id}", title='Edição Concluído')
                selectedId = -1
                selectedSid = -1
                lc.reset_employee_menu('MEE')
                lc.update_window_layout(janela, '-LayoutMenuEmpregados-')


        elif evento == 'MEE-CANCELAR':
            sg.popup('Nenhum detalhe foi alterado.', title='')
            selectedId = -1
            selectedSid = -1
            lc.reset_employee_menu('MEE')
            lc.update_window_layout(janela, '-LayoutMenuEmpregados-')


#######################################################################################################

# MENU SINDICATO
    elif janela == janelaPrincipal and lc.is_layout_active('-LayoutMenuSindicato-'):
        
        if evento == 'MS-LISTA':
            listaf = 'SID:\t NOME\n'
            for key, employee in Sindicato.affiliatesList.items():
                listaf = listaf + f'{key}\t: {employee}' + '\n'
            sg.popup(listaf)
        
        
        elif evento[0:6] == 'voltar':
            lc.update_window_layout(janela, '-LayoutMenuPrincipal-')





#######################################################################################################

# MENU PAGAMENTO
    elif janela == janelaPrincipal and lc.is_layout_active('-LayoutMenuPagamento-'):
        if evento[0:6] == 'voltar':
            lc.update_window_layout(janela, '-LayoutMenuPrincipal-')