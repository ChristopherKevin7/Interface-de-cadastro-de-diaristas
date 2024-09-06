from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import Diarista
from .models import Empresa
from datetime import datetime, timedelta, date
from PyPDF2 import PdfReader, PdfWriter
import os
from num2words import num2words
import subprocess


def home(request):
    return render(request,'diaristas/home.html')

def home_empresa(request):
    return render(request,'diaristas/home_empresa.html')

def read(request):
    return redirect('listagem_diaristas')

def read_empresa(request):
    return redirect('listagem_empresas')

def diaristas(request):
    
    if request.method == 'POST':
        #Salvar as informações no banco de dados
        novo_diarista = Diarista()
        novo_diarista.nome = request.POST.get('nome')
        novo_diarista.setor = request.POST.get('setor')
        novo_diarista.rg = request.POST.get('rg')
        novo_diarista.cpf = request.POST.get('cpf')
        novo_diarista.email = request.POST.get('email')
        novo_diarista.telefone = request.POST.get('telefone')
        novo_diarista.pix = request.POST.get('pix')

        novo_diarista.save()
    
    #Exibir todos os diaristas já cadastrados em uma nova pagina
    diaristas = {
        'diaristas': Diarista.objects.all()
    }
    
    #Retorna os dados para a pagina de listagem de diaristas
    return render(request, 'diaristas/diaristas.html', diaristas)

def empresas(request):
    
    if request.method == 'POST':
        #Salvar as informações no banco de dados
        novo_empresa = Empresa()
        novo_empresa.nome_empresa = request.POST.get('nome_empresa')
        novo_empresa.cnpj = request.POST.get('cnpj')
        novo_empresa.estado = request.POST.get('estado')
        novo_empresa.cidade = request.POST.get('cidade')
        novo_empresa.rua = request.POST.get('rua')
        novo_empresa.bairro = request.POST.get('bairro')
        novo_empresa.numero = request.POST.get('numero')
        novo_empresa.cep = request.POST.get('cep')
        novo_empresa.email = request.POST.get('email')

        novo_empresa.save()
    
    #Exibir todos os empresas já cadastrados em uma nova pagina
    empresas = {
        'empresas': Empresa.objects.all()
    }
    
    #Retorna os dados para a pagina de listagem de empresas
    return render(request, 'diaristas/empresas.html', empresas)

def editar(request, id_diarista):
    diarista = Diarista.objects.get(id_diarista=id_diarista)
    return render(request, 'diaristas/editar.html', {"diarista": diarista})

def editar_empresa(request, id_empresa):
    empresa = Empresa.objects.get(id_empresa=id_empresa)
    return render(request, 'diaristas/editar_empresa.html', {"empresa": empresa})

def update(request, id_diarista):
    diarista = Diarista.objects.get(id_diarista=id_diarista)
    diarista.nome = request.POST.get('nome')
    diarista.setor = request.POST.get('setor')
    diarista.rg = request.POST.get('rg')
    diarista.cpf = request.POST.get('cpf')
    diarista.email = request.POST.get('email')
    diarista.telefone = request.POST.get('telefone')
    diarista.pix = request.POST.get('pix')
    diarista.save()
    return redirect(read)

def update_empresa(request, id_empresa):
    empresa = Empresa.objects.get(id_empresa=id_empresa)
    empresa.nome_empresa = request.POST.get('nome_empresa')
    empresa.cnpj = request.POST.get('cnpj')
    empresa.cep = request.POST.get('cep')
    empresa.estado = request.POST.get('estado')
    empresa.cidade = request.POST.get('cidade')
    empresa.bairro = request.POST.get('bairro')
    empresa.rua = request.POST.get('rua')
    empresa.numero = request.POST.get('numero')
    empresa.email = request.POST.get('email')
    empresa.save()
    return redirect(read_empresa)

def excluir_item(request, id_diarista):
    if request.method == 'POST':
        diarista = Diarista.objects.get(pk=id_diarista)
        diarista.delete()
        return render(request, 'diaristas/excluir.html')
    else:
        return JsonResponse({'status': 'error', 'message': 'Método inválido'})
    
def excluir_item_empresa(request, id_empresa):
    if request.method == 'POST':
        empresa = Empresa.objects.get(pk=id_empresa)
        empresa.delete()
        return render(request, 'diaristas/excluir_empresa.html')
    else:
        return JsonResponse({'status': 'error', 'message': 'Método inválido'})
    
def recibo(request, id_diarista):
    diarista = Diarista.objects.get(id_diarista=id_diarista)
    empresas = Empresa.objects.all()
    return render(request, 'diaristas/recibo.html', {"diarista": diarista, "empresas": empresas})

def emitir_recibo(request, id_diarista, id_empresa):

    diarista = Diarista.objects.get(id_diarista = id_diarista)
    empresa = Empresa.objects.get(id_empresa = id_empresa)
    
    hor_ent = request.POST.get('hor_ent')
 
    if id_diarista and id_empresa and hor_ent is not None:

        horario_entrada = datetime.strptime(request.POST.get('hor_ent'), '%H:%M').time()
        horario_init_alm = datetime.strptime(request.POST.get('hor_alm_ini'), '%H:%M').time()
        horario_ret_alm = datetime.strptime(request.POST.get('hor_alm_ret'), '%H:%M').time()
        horario_saida = datetime.strptime(request.POST.get('hor_saida'), '%H:%M').time()

        data = request.POST.get('data', None)  # O segundo argumento para 'get' é o valor padrão se a chave não existir.
        if data:
            data_formatada = datetime.strptime(data, '%Y-%m-%d').date()
        else:
            data_formatada = None  # Ou qualquer outra ação ou valor padrão que você deseja aplicar quando não houver data fornecida.

# Agora você pode usar 'data_formatada' no restante do seu código.
        
        # Converter os horários para minutos
        entrada_minutes = horario_entrada.hour * 60 + horario_entrada.minute 
        almoco_ini_minutes = horario_init_alm.hour * 60+ horario_init_alm.minute 
        almoco_ret_minutes = horario_ret_alm.hour * 60 + horario_ret_alm.minute 
        saida_minutes = horario_saida.hour * 60 + horario_saida.minute 
        
        horas_int = ((almoco_ini_minutes - entrada_minutes)+(saida_minutes - almoco_ret_minutes))/60
        
        if data_formatada is None:
            data_hj = datetime.now()
        else:
            data_hj = data_formatada

        data_hj_sem = data_hj.strftime("%A")
        
        if data_hj_sem == 'sunday':
            valor_hr = 15
            
        elif data_hj_sem == 'saturday':
            valor_hr = 12
        
        else:
            valor_hr = 10
        
        valor_dia = (horas_int * valor_hr) + 10
        
        emitir_pdf(id_diarista, id_empresa, valor_dia, data_hj)

        return JsonResponse({'success': True})
    
    else:
        return render(request, 'diaristas/emitir_recibo.html', {"diarista": diarista, "empresa": empresa})


def emitir_pdf(id_diarista, id_empresa, valor_dia, data_hj):

    diarista = Diarista.objects.get(id_diarista=id_diarista)
    empresa = Empresa.objects.get(id_empresa = id_empresa)

    dia = data_hj.day
    mes = data_hj.month
    ano = data_hj.year
    data = data_hj
    mes_ext = data.strftime('%B')
    valor_dia = int(valor_dia)
    valor_extenso = int_para_extenso(valor_dia)

    if dia <= 9:
        dia = '0' + str(dia)

    if mes <= 9:
        mes = '0' + str(mes)

    # Dicionário de tradução de meses
    meses = {
        'January': 'Janeiro',
        'February': 'Fevereiro',
        'March': 'Março',
        'April': 'Abril',
        'May': 'Maio',
        'June': 'Junho',
        'July': 'Julho',
        'August': 'Agosto',
        'September': 'Setembro',
        'October': 'Outubro',
        'November': 'Novembro',
        'December': 'Dezembro'
    }

    mes_traduzido = meses.get(mes_ext, 'Mês Inválido')

    dados = {
        'nome': diarista.nome,
        'cpf': diarista.cpf,
        'rg': diarista.rg,
        'nome_empresa': empresa.nome_empresa,
        'cnpj' : empresa.cnpj,
        'valor': str(valor_dia) + ',00',
        'valor_extenso': valor_extenso + ' reais',
        'dia': str(dia),
        'mes': str(mes),
        'ano': str(ano),
        'dia2': str(dia),
        'mes_extenso': mes_traduzido,
        'ano2': str(ano),
    }

    output_dir = "Recibos"
    os.makedirs(output_dir, exist_ok=True)

    # Abrir o PDF original para leitura
    with open("PDF_Modelo/modelo.pdf", "rb") as infile:
        reader = PdfReader(infile)

        # Criar um novo PDF para escrita
        with open(os.path.join(output_dir, f"Recibo-ID{diarista.id_diarista}-{dia}-{mes}-{ano}.pdf"), "wb") as output_stream:
            writer = PdfWriter()

            # Copiar todas as páginas do PDF original para o novo PDF
            for page in reader.pages:
                writer.add_page(page)

            # Atualizar os campos do formulário do novo PDF
            writer.update_page_form_field_values(
                writer.pages[0],
                dados,
            )

            writer.write(output_stream)
            print("PDF gerado com sucesso!")

            abrir_pdf(os.path.join(output_dir, f"Recibo-ID{diarista.id_diarista}-{dia}-{mes}-{ano}.pdf"))
    
    

def int_para_extenso(numero):
    return num2words(numero, lang='pt_BR')

def abrir_pdf(caminho_pdf):
    # Tente abrir o arquivo PDF com o programa padrão associado
    try:
        subprocess.Popen([caminho_pdf], shell=True)
        print("PDF aberto com sucesso!")
    except Exception as e:
        print(f"Erro ao abrir o PDF: {e}")