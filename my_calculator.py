import PySimpleGUI as sg

#Configs
buttons = {'size':(3,1), 'font':('Franklin Gothic Book', 24), 'button_color':('gray','#C0C0C0')}
del_ac = {'size': (3,1), 'font':('Franklin Gothic Book', 24), 'button_color':('red', '#FF6666')}
result_bt = {'size':(13,1), 'font':('Franklin Gothic Book', 24), 'button_color':('red', '#FF6666'), 'focus':True}

#LAYOUT
layout = [[sg.Text('Simple Calculator', justification='right', background_color='#333333')],
        [sg.Text('0', size=(19,2), justification='right', background_color='green', text_color='black', font=('Digital-7', 30), relief='sunken', key='_DISPALY_')],
        [sg.Button('7', **buttons), sg.Button('8', **buttons), sg.Button('9', **buttons), sg.Button('DEL', **del_ac), sg.Button('AC', **del_ac)],
        [sg.Button('4', **buttons), sg.Button('5', **buttons), sg.Button('6', **buttons), sg.Button('*', **buttons), sg.Button('/', **buttons)],
        [sg.Button('1', **buttons), sg.Button('2', **buttons), sg.Button('3', **buttons), sg.Button('+', **buttons), sg.Button('-', **buttons)],
        [sg.Button('0', **buttons), sg.Button(',', **buttons), sg.Button('=', **result_bt, bind_return_key=True)]
        ]

#WINDOW
window = sg.Window('Simple Calculator', layout=layout, background_color='#333333', return_keyboard_events=True)

var = {'front':[], 'back':[], 'decimal':False, 'x':0.0, 'y':0.0, 'resp':0.0, 'operator':''}

def formato_num():
    return float(''.join(var['front'])+'.'+''.join(var['back']))

def atualizar_display(valor_display):
    try:
        window['_DISPLAY_'].update(valeu='{:,.4f}'.format(valor_display))
    except:
        window['_DISPLAY_'].update(value=valor_display)

#EVENT

def click_num(event):
    global var
    if var['decimal']:
        var['back'].append(event)
    else:
        var['front'].append(event)
    atualizar_display(formato_num())

def click_operador():
    global var
    var['operator'] = event
    try:
        var['x'] = formato_num()
    except:
        var['x'] = var['resp']
    apagar()

def apagar():
    global var
    var['back'].clear()
    var['front'].clear()
    var['decimal'] = False

def calculando():
    global var
    var['y'] = formato_num()
    try:
        var['resp'] = eval(str(var['x'])+var['operator']+str(var['y']))
        atualizar_display(var['resp'])
        apagar()
    except:
        atualizar_display('ERRO! DIV/0')
        apagar()

while True:
    event, values = window.read()
    print(event)
    if event is None:
        break
    if event is ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
        click_num(event)
    if event is ['DEL', 'AC']:
        apagar()
        atualizar_display(0.0)
        var['resp'] = 0.0
    if event is ['+', '-', '*', '/']:
        click_operador(event)
    if event is ['=']:
        calculando()
    if event == '.':
        var['decimal'] = True
    if event == sg.WIN_CLOSED:
        break
    if event == '7':
        sg.Text('Apenas Teste')
        print('Apenas testes')
window.close()
