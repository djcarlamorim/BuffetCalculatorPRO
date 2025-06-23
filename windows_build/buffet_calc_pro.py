import tkinter as tk
from tkinter import ttk, messagebox, filedialog
from tkinter.scrolledtext import ScrolledText
from datetime import datetime
from fpdf import FPDF
import webbrowser
import sys

class BuffetCalculatorPro:
    def __init__(self, root):
        self.root = root
        self.root.title("Buffet Calculator PRO - Sistema de Cálculo para Eventos")
        self.root.geometry("1200x800")
        self.root.configure(bg="#f5f5f5")
        
        try:
            # Configurações de estilo
            self.style = ttk.Style()
            self.style.configure('TFrame', background='#f5f5f5')
            self.style.configure('TLabel', background='#f5f5f5', font=('Helvetica', 10))
            self.style.configure('TButton', font=('Helvetica', 10, 'bold'))
            self.style.configure('Header.TLabel', font=('Helvetica', 16, 'bold'), foreground='#333333')
            self.style.configure('Copyright.TLabel', font=('Helvetica', 8), foreground='#666666')
            
            # Variáveis
            self.client_name = tk.StringVar()
            self.event_date = tk.StringVar()
            self.event_type = tk.StringVar()
            self.event_option = tk.StringVar()
            self.guests = tk.IntVar(value=100)
            self.event_hours = tk.StringVar(value="4")
            self.adults = tk.IntVar(value=0)
            self.children = tk.IntVar(value=0)
            self.include_alcohol = tk.BooleanVar(value=False)
            self.include_non_alcohol = tk.BooleanVar(value=True)
            self.include_utensils = tk.BooleanVar(value=True)
            self.include_furniture = tk.BooleanVar(value=False)
            
            # Dados dos eventos
            self.event_data = {
                "Coquetel": {
                    "Simples": {"Mini Salgados": 15},
                    "+ 1 Prato quente": {"Mini Salgados": 12},
                    "Seguido de Almoço/Jantar": {"Mini Salgados": 8}
                },
                "Almoço": {
                    "Arroz (cru)": 0.05,
                    "Frutas e Vegetais": 0.12,
                    "Carne ou Peixe": 0.15,
                    "Massa (Prato Principal)": 0.1,
                    "Massa (Acompanhamento)": 0.08
                },
                "Jantar": {
                    "Arroz (cru)": 0.05,
                    "Frutas e Vegetais": 0.12,
                    "Carne ou Peixe": 0.15,
                    "Massa (Prato Principal)": 0.1,
                    "Massa (Acompanhamento)": 0.08
                },
                "Churrasco": {
                    "Arroz (cru)": 0.05,
                    "Frutas e Vegetais": 0.12,
                    "Carnes e Peixe": 0.3,
                    "Mini Pães": 0.03,
                    "Vinagrete": 0.05,
                    "Maionese/Salpicão": 0.05
                },
                "Feijoada": {
                    "Feijão Preto": 0.08,
                    "Arroz": 0.06,
                    "Couve": 0.02,
                    "Farofa": 0.04,
                    "Vinagrete": 0.03,
                    "Laranja": 0.5,
                    "Carne Sem Osso": 0.1,
                    "Carne Com Osso": 0.15
                },
                "Sobremesas": {
                    "Doces": {"quantidade": 4, "unidade": "Unidades"},
                    "Bolo": {"quantidade": 0.08, "unidade": "Kg"},
                    "Sorvete": {"quantidade": 0.12, "unidade": "Kg"},
                    "Torta": {"quantidade": 1, "unidade": "Kg/10p"}
                },
                "Bebidas Não Alcoólicas": {
                    "Água Mineral": 0.4,
                    "Suco": 0.25,
                    "Refrigerante": 0.8,
                    "Café": 0.05
                },
                "Bebidas Alcoólicas": {
                    "Cerveja (única bebida)": 1,
                    "Cerveja (com outras)": 0.75,
                    "Coquetel de Frutas/Batidas": 0.06
                },
                "Festa Infantil": {
                    "Sucos/Refrigerantes (Adultos)": 0.6,
                    "Sucos/Refrigerantes (Crianças)": 0.3,
                    "Café (Adultos)": 0.05,
                    "Saladas (Adultos)": 0.045,
                    "Saladas (Crianças)": 0.015,
                    "Mini Sanduíches (Adultos)": 4,
                    "Mini Sanduíches (Crianças)": 2,
                    "Salgadinhos (Adultos)": 7,
                    "Salgadinhos (Crianças)": 3,
                    "Frutas (Adultos)": 0.05,
                    "Frutas (Crianças)": 0.05,
                    "Bolo (Adultos)": 0.1,
                    "Bolo (Crianças)": 0.05,
                    "Docinho (Adultos)": 5,
                    "Docinho (Crianças)": 2,
                    "Pipoca (Adultos)": 0.02,
                    "Pipoca (Crianças)": 0.01
                },
                "Café da Manhã": {
                    "Água Mineral": 0.25,
                    "Café": 0.07,
                    "Leite": 0.05,
                    "Chá": 0.05,
                    "Suco": 0.15,
                    "Iogurte": 0.07,
                    "Cereais": 0.02,
                    "Salada de Frutas": 0.05,
                    "Mini Pães": 2,
                    "Geléia/Pastas": 0.01,
                    "Frios": 0.03,
                    "Ovos Mexidos": 1,
                    "Pão de Queijo": 3,
                    "Mini Salgados Assados": 2,
                    "Bolo Doce/Mini Cupcake": 2
                },
                "Coffee Break": {
                    "Água Mineral": 0.25,
                    "Café": 0.07,
                    "Leite": 0.05,
                    "Chá": 0.05,
                    "Suco": 0.15,
                    "Mini Sanduíches": 2.5,
                    "Mini Salgados": 2,
                    "Bolo Doce/Mini Cupcake": 1,
                    "Mini Tortinha/Docinho": 2
                },
                "Brunch": {
                    "Água Mineral": 0.25,
                    "Suco": 0.4,
                    "Mini Pães": 2,
                    "Pastas (2-3 Tipos)": 0.01,
                    "Salada de Folhas Verdes": 0.045,
                    "Tábua de Frios": 0.03,
                    "Tortas Salgadas": 0.15,
                    "Tortas Doces": 0.1
                },
                "Utensílios": {
                    "Copos de Vidro": 2,
                    "Copos Descartáveis": 5,
                    "Taças": 1,
                    "Xícaras (à la carte)": 1,
                    "Xícaras (buffet)": 0.5,
                    "Copos de Isopor": 2,
                    "Pratos (Principal)": 1,
                    "Pratos (Sobremesa)": 1,
                    "Colheres": 1,
                    "Colheres (Sobremesa)": 1,
                    "Garfos": 1,
                    "Garfos (Sobremesa)": 1,
                    "Facas": 1
                },
                "Mobiliário": {
                    "Cadeiras": 1,
                    "Mesas (4 lugares)": 0.25,
                    "Mesas (6 lugares)": 0.1667,
                    "Mesas (8 lugares)": 0.125,
                    "Mesas (10 lugares)": 0.1,
                    "Pranchão": 0.025
                }
            }
            
            # Criar interface
            self.create_widgets()
            
        except Exception as e:
            messagebox.showerror("Erro Inicial", f"Erro ao iniciar aplicação: {str(e)}")
            self.root.destroy()
            sys.exit(1)

    def create_widgets(self):
        # Cabeçalho com copyright
        header_frame = ttk.Frame(self.root, style='TFrame')
        header_frame.pack(fill='x', padx=10, pady=(10,0))
        
        ttk.Label(header_frame, text="Buffet Calculator PRO", style='Header.TLabel').pack(side='left')
        ttk.Label(header_frame, text="© 2025 Eventos PRO - Todos os direitos reservados - Versão 2.0", 
                 style='Copyright.TLabel').pack(side='right')
        
        # Frame principal
        main_frame = ttk.Frame(self.root, style='TFrame')
        main_frame.pack(fill='both', expand=True, padx=10, pady=5)
        
        # Frame de entrada de dados
        input_frame = ttk.LabelFrame(main_frame, text="Dados do Evento", padding=10)
        input_frame.grid(row=0, column=0, sticky='nsew', padx=5, pady=5)
        
        # Frame de opções
        options_frame = ttk.LabelFrame(main_frame, text="Opções do Evento", padding=10)
        options_frame.grid(row=0, column=1, sticky='nsew', padx=5, pady=5)
        
        # Frame de resultados
        result_frame = ttk.LabelFrame(main_frame, text="Resultados", padding=10)
        result_frame.grid(row=1, column=0, columnspan=2, sticky='nsew', padx=5, pady=5)
        
        # Configurar pesos
        main_frame.columnconfigure(0, weight=1)
        main_frame.columnconfigure(1, weight=1)
        main_frame.rowconfigure(1, weight=1)
        
        # Widgets de entrada
        ttk.Label(input_frame, text="Nome do Cliente:").grid(row=0, column=0, sticky='e', padx=5, pady=5)
        ttk.Entry(input_frame, textvariable=self.client_name, width=30).grid(row=0, column=1, sticky='w', padx=5, pady=5)
        
        ttk.Label(input_frame, text="Data do Evento:").grid(row=1, column=0, sticky='e', padx=5, pady=5)
        ttk.Entry(input_frame, textvariable=self.event_date, width=30).grid(row=1, column=1, sticky='w', padx=5, pady=5)
        
        ttk.Label(input_frame, text="Tipo de Evento:").grid(row=2, column=0, sticky='e', padx=5, pady=5)
        event_types = ['Aniversário', 'Casamento', 'Corporativo', 'Formatura', 'Confraternização', 'Outros']
        ttk.Combobox(input_frame, textvariable=self.event_type, values=event_types, state="readonly").grid(row=2, column=1, sticky='w', padx=5, pady=5)
        
        ttk.Label(input_frame, text="Opção de Evento:").grid(row=3, column=0, sticky='e', padx=5, pady=5)
        event_options = ['Coquetel', 'Almoço', 'Jantar', 'Churrasco', 'Feijoada', 'Festa Infantil', 
                        'Café da Manhã', 'Coffee Break', 'Brunch', 'Mobiliário']
        self.event_option_cb = ttk.Combobox(input_frame, textvariable=self.event_option, values=event_options, state="readonly")
        self.event_option_cb.grid(row=3, column=1, sticky='w', padx=5, pady=5)
        
        ttk.Label(input_frame, text="Número de Convidados:").grid(row=4, column=0, sticky='e', padx=5, pady=5)
        ttk.Entry(input_frame, textvariable=self.guests, width=10).grid(row=4, column=1, sticky='w', padx=5, pady=5)
        
        ttk.Label(input_frame, text="Duração (horas):").grid(row=5, column=0, sticky='e', padx=5, pady=5)
        ttk.Combobox(input_frame, textvariable=self.event_hours, values=('4', '5', '6'), state="readonly", width=5).grid(row=5, column=1, sticky='w', padx=5, pady=5)
        
        # Campos para Festa Infantil
        self.child_frame = ttk.Frame(input_frame)
        ttk.Label(self.child_frame, text="Adultos:").grid(row=0, column=0, padx=5, pady=5)
        ttk.Entry(self.child_frame, textvariable=self.adults, width=5).grid(row=0, column=1, padx=5, pady=5)
        ttk.Label(self.child_frame, text="Crianças (3-12 anos):").grid(row=0, column=2, padx=5, pady=5)
        ttk.Entry(self.child_frame, textvariable=self.children, width=5).grid(row=0, column=3, padx=5, pady=5)
        
        # Opções adicionais
        ttk.Checkbutton(options_frame, text="Incluir Bebidas Não Alcoólicas", variable=self.include_non_alcohol).grid(row=0, column=0, sticky='w', padx=5, pady=2)
        ttk.Checkbutton(options_frame, text="Incluir Bebidas Alcoólicas", variable=self.include_alcohol).grid(row=1, column=0, sticky='w', padx=5, pady=2)
        ttk.Checkbutton(options_frame, text="Incluir Utensílios (copos, pratos, talheres)", variable=self.include_utensils).grid(row=2, column=0, sticky='w', padx=5, pady=2)
        ttk.Checkbutton(options_frame, text="Incluir Mobiliário (mesas e cadeiras)", variable=self.include_furniture).grid(row=3, column=0, sticky='w', padx=5, pady=2)
        
        # Botões
        btn_frame = ttk.Frame(input_frame)
        btn_frame.grid(row=7, column=0, columnspan=2, pady=10)
        
        ttk.Button(btn_frame, text="Calcular", command=self.calculate, style='TButton').pack(side='left', padx=5)
        ttk.Button(btn_frame, text="Imprimir Relatório", command=self.generate_pdf, style='TButton').pack(side='left', padx=5)
        ttk.Button(btn_frame, text="Limpar", command=self.clear_fields, style='TButton').pack(side='left', padx=5)
        
        # Área de resultados
        self.result_text = ScrolledText(result_frame, wrap=tk.WORD, font=('Courier', 10))
        self.result_text.pack(fill='both', expand=True, padx=5, pady=5)
        
        self.event_option.trace_add('write', self.update_child_fields)
    
    def update_child_fields(self, *args):
        if self.event_option.get() == 'Festa Infantil':
            self.child_frame.grid(row=6, column=0, columnspan=2, pady=5)
        else:
            self.child_frame.grid_forget()
    
    def calculate(self):
        try:
            if not all([self.client_name.get(), self.event_date.get(), self.event_type.get(), self.event_option.get()]):
                messagebox.showerror("Erro", "Por favor, preencha todos os campos obrigatórios.")
                return
                
            if self.event_option.get() == 'Festa Infantil':
                if not (self.adults.get() >= 0 and self.children.get() >= 0):
                    messagebox.showerror("Erro", "Para Festa Infantil, preencha valores válidos para adultos e crianças.")
                    return
                total_guests = self.adults.get() + self.children.get()
                self.guests.set(total_guests)
            else:
                if not self.guests.get() > 0:
                    messagebox.showerror("Erro", "Por favor, informe um número válido de convidados.")
                    return
                total_guests = self.guests.get()
            
            horas_evento = int(self.event_hours.get())
            
            # Fatores de aumento (5h = +8%, 6h = +15%)
            if horas_evento == 5:
                food_factor = 1.08
                beverage_factor = 1.08
            elif horas_evento == 6:
                food_factor = 1.15
                beverage_factor = 1.15
            else:
                food_factor = 1.0
                beverage_factor = 1.0
            
            self.result_text.delete(1.0, tk.END)
            
            # Cabeçalho
            self.result_text.insert(tk.END, f"{'='*70}\n")
            self.result_text.insert(tk.END, f"{'ORÇAMENTO PARA EVENTO - BUFFET CALCULATOR PRO':^70}\n")
            self.result_text.insert(tk.END, f"{'='*70}\n\n")
            
            self.result_text.insert(tk.END, f"{'Cliente:':<20}{self.client_name.get()}\n")
            self.result_text.insert(tk.END, f"{'Data do Evento:':<20}{self.event_date.get()}\n")
            self.result_text.insert(tk.END, f"{'Tipo de Evento:':<20}{self.event_type.get()}\n")
            self.result_text.insert(tk.END, f"{'Opção de Evento:':<20}{self.event_option.get()}\n")
            self.result_text.insert(tk.END, f"{'Total Convidados:':<20}{total_guests}\n")
            
            if self.event_option.get() == 'Festa Infantil':
                self.result_text.insert(tk.END, f"{'Adultos:':<20}{self.adults.get()}\n")
                self.result_text.insert(tk.END, f"{'Crianças:':<20}{self.children.get()}\n")
            
            self.result_text.insert(tk.END, f"{'Duração:':<20}{horas_evento} horas\n")
            self.result_text.insert(tk.END, f"\n{'='*70}\n")
            self.result_text.insert(tk.END, f"{'ITENS NECESSÁRIOS':^70}\n")
            self.result_text.insert(tk.END, f"{'='*70}\n\n")
            
            # Calcular itens principais
            option = self.event_option.get()
            if option in self.event_data:
                self.result_text.insert(tk.END, f"\n{option.upper()}\n")
                self.result_text.insert(tk.END, f"{'-'*70}\n")
                
                if option == 'Festa Infantil':
                    self.calculate_child_party(total_guests, food_factor)
                elif option == 'Coquetel':
                    self.calculate_coquetel(total_guests, food_factor)
                else:
                    self.calculate_standard_event(option, total_guests, food_factor)
            
            # Bebidas
            if self.include_non_alcohol.get():
                self.result_text.insert(tk.END, f"\nBEBIDAS NÃO ALCOÓLICAS\n")
                self.result_text.insert(tk.END, f"{'-'*70}\n")
                self.calculate_beverages('Bebidas Não Alcoólicas', total_guests, beverage_factor)
            
            if self.include_alcohol.get():
                self.result_text.insert(tk.END, f"\nBEBIDAS ALCOÓLICAS\n")
                self.result_text.insert(tk.END, f"{'-'*70}\n")
                self.calculate_beverages('Bebidas Alcoólicas', total_guests, beverage_factor)
            
            # Utensílios
            if self.include_utensils.get():
                self.result_text.insert(tk.END, f"\nUTENSÍLIOS\n")
                self.result_text.insert(tk.END, f"{'-'*70}\n")
                self.calculate_utensils(total_guests)
            
            # Mobiliário
            if self.include_furniture.get():
                self.result_text.insert(tk.END, f"\nMOBILIÁRIO\n")
                self.result_text.insert(tk.END, f"{'-'*70}\n")
                self.calculate_furniture(total_guests)
            
            # Pessoal
            self.result_text.insert(tk.END, f"\nPESSOAL NECESSÁRIO\n")
            self.result_text.insert(tk.END, f"{'-'*70}\n")
            self.calculate_staff(total_guests)
            
            messagebox.showinfo("Sucesso", "Cálculos concluídos com sucesso!")
            
        except ValueError:
            messagebox.showerror("Erro", "Por favor, insira valores numéricos válidos.")
        except Exception as e:
            messagebox.showerror("Erro", f"Ocorreu um erro inesperado: {e}")
    
    def calculate_standard_event(self, event_type, guests, factor):
        data = self.event_data[event_type]
        
        for item, value in data.items():
            if isinstance(value, dict):
                quant = value['quantidade']
                unit = value['unidade']
                total = quant * guests
                self.result_text.insert(tk.END, f"- {item}: {quant} {unit}/pessoa → Total: {total:.2f} {unit}\n")
            else:
                if "ou" in item.lower():
                    self.result_text.insert(tk.END, f"- {item}\n")
                else:
                    quant = value
                    total = quant * guests * factor
                    unit = "Kg" if quant < 1 else "Unidades"
                    self.result_text.insert(tk.END, f"- {item}: {quant} {unit}/pessoa → Total: {total:.2f} {unit}\n")
    
    def calculate_child_party(self, total_guests, factor):
        adults = self.adults.get()
        children = self.children.get()
        
        data = self.event_data['Festa Infantil']
        
        items = {
            "Bebidas": ["Sucos/Refrigerantes (Adultos)", "Sucos/Refrigerantes (Crianças)", "Café (Adultos)"],
            "Salgados": ["Mini Sanduíches (Adultos)", "Mini Sanduíches (Crianças)", "Salgadinhos (Adultos)", "Salgadinhos (Crianças)"],
            "Outros": ["Saladas (Adultos)", "Saladas (Crianças)", "Frutas (Adultos)", "Frutas (Crianças)", 
                      "Bolo (Adultos)", "Bolo (Crianças)", "Docinho (Adultos)", "Docinho (Crianças)", 
                      "Pipoca (Adultos)", "Pipoca (Crianças)"]
        }
        
        for category, item_list in items.items():
            self.result_text.insert(tk.END, f"\n{category.upper()}:\n")
            for item in item_list:
                quant = data[item]
                if "(Adultos)" in item:
                    total = quant * adults * factor
                else:
                    total = quant * children * factor
                
                if any(x in item.lower() for x in ['suco', 'refrigerante', 'café']):
                    unit = "Litros"
                elif any(x in item.lower() for x in ['sanduíches', 'salgadinhos', 'docinho']):
                    unit = "Unidades"
                else:
                    unit = "Kg"
                
                display_item = item.replace("(Adultos)", "").replace("(Crianças)", "").strip()
                self.result_text.insert(tk.END, f"- {display_item}: {quant} {unit}/pessoa → Total: {total:.2f} {unit}\n")
    
    def calculate_coquetel(self, guests, factor):
        option = self.event_option.get()
        
        self.result_text.insert(tk.END, "Escolha uma das opções de coquetel:\n")
        
        for coq_type, items in self.event_data[option].items():
            self.result_text.insert(tk.END, f"\n{coq_type}:\n")
            for item, quant in items.items():
                total = quant * guests * factor
                self.result_text.insert(tk.END, f"- {item}: {quant} Unidades/pessoa → Total: {total:.0f} Unidades\n")
    
    def calculate_beverages(self, beverage_type, guests, factor):
        data = self.event_data[beverage_type]
        
        for item, quant in data.items():
            total = quant * guests * factor
            unit = "Litros" if quant < 1 else "Garrafas"
            self.result_text.insert(tk.END, f"- {item}: {quant} {unit}/pessoa → Total: {total:.2f} {unit}\n")
    
    def calculate_utensils(self, guests):
        data = self.event_data['Utensílios']
        
        for item, quant in data.items():
            total = quant * guests
            unit = "Unidades"
            if "Xícaras (buffet)" in item:
                total = total / 2
            self.result_text.insert(tk.END, f"- {item}: {quant} {unit}/pessoa → Total: {total:.0f} {unit}\n")
    
    def calculate_furniture(self, guests):
        data = self.event_data['Mobiliário']
        
        for item, quant in data.items():
            total = quant * guests
            if "Mesas" in item:
                total = round(total)
            self.result_text.insert(tk.END, f"- {item}: {total:.0f} {'Unidades' if quant < 1 else 'Conjuntos'}\n")
    
    def calculate_staff(self, guests):
        waiters = (guests // 20) + (1 if guests % 20 > 0 else 0)
        self.result_text.insert(tk.END, f"- Garçons: 1 para cada 20 convidados → Total: {waiters}\n")
        
        cooks = (guests // 50) + (1 if guests % 50 > 0 else 0)
        self.result_text.insert(tk.END, f"- Cozinheiros: 1 para cada 50 convidados → Total: {cooks}\n")
    
    def generate_pdf(self):
        try:
            if not self.result_text.get(1.0, tk.END).strip():
                messagebox.showerror("Erro", "Nenhum resultado para gerar PDF. Execute os cálculos primeiro.")
                return
                
            # Configurar PDF com encoding correto
            pdf = FPDF()
            pdf.add_page()
            pdf.set_auto_page_break(auto=True, margin=15)
            
            # Adicionar cabeçalho com copyright
            pdf.set_font("Arial", 'B', 16)
            pdf.cell(0, 10, "ORÇAMENTO PARA EVENTO - BUFFET CALCULATOR PRO", 0, 1, 'C')
            pdf.set_font("Arial", '', 8)
            pdf.cell(0, 5, "© 2025 Eventos PRO - Todos os direitos reservados - Versão 2.0", 0, 1, 'C')
            pdf.ln(5)
            
            # Informações do evento
            pdf.set_font("Arial", 'B', 12)
            pdf.cell(0, 10, "Informações do Evento", 0, 1)
            pdf.set_font("Arial", size=12)
            
            # Função para garantir encoding correto
            def safe_text(text):
                return text.encode('latin-1', 'replace').decode('latin-1')
            
            pdf.cell(50, 10, "Cliente:", 0, 0)
            pdf.cell(0, 10, safe_text(self.client_name.get()), 0, 1)
            
            pdf.cell(50, 10, "Data do Evento:", 0, 0)
            pdf.cell(0, 10, safe_text(self.event_date.get()), 0, 1)
            
            pdf.cell(50, 10, "Tipo de Evento:", 0, 0)
            pdf.cell(0, 10, safe_text(self.event_type.get()), 0, 1)
            
            pdf.cell(50, 10, "Opção de Evento:", 0, 0)
            pdf.cell(0, 10, safe_text(self.event_option.get()), 0, 1)
            
            pdf.cell(50, 10, "Total Convidados:", 0, 0)
            pdf.cell(0, 10, str(self.guests.get()), 0, 1)
            
            if self.event_option.get() == 'Festa Infantil':
                pdf.cell(50, 10, "Adultos:", 0, 0)
                pdf.cell(0, 10, str(self.adults.get()), 0, 1)
                
                pdf.cell(50, 10, "Crianças:", 0, 0)
                pdf.cell(0, 10, str(self.children.get()), 0, 1)
            
            pdf.cell(50, 10, "Duração:", 0, 0)
            pdf.cell(0, 10, f"{self.event_hours.get()} horas", 0, 1)
            
            pdf.ln(10)
            
            # Adicionar conteúdo do texto
            pdf.set_font("Arial", 'B', 14)
            pdf.cell(0, 10, "ITENS NECESSÁRIOS", 0, 1)
            pdf.set_font("Courier", size=10)
            
            for line in self.result_text.get(1.0, tk.END).split('\n'):
                if line.strip():
                    if line.startswith("=") or line.startswith("-") or any(x in line for x in ["ORÇAMENTO", "ITENS NECESSÁRIOS", "BEBIDAS", "UTENSÍLIOS", "PESSOAL"]):
                        pdf.set_font("Courier", 'B', 10)
                        pdf.cell(0, 10, safe_text(line), 0, 1)
                        pdf.set_font("Courier", size=10)
                    else:
                        pdf.cell(0, 10, safe_text(line), 0, 1)
            
            # Salvar PDF
            default_filename = f"Orcamento_{safe_text(self.client_name.get())}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.pdf"
            filepath = filedialog.asksaveasfilename(
                defaultextension=".pdf",
                initialfile=default_filename,
                filetypes=[("PDF Files", "*.pdf")]
            )
            
            if filepath:
                pdf.output(filepath)
                webbrowser.open(filepath)
                messagebox.showinfo("Sucesso", f"Relatório salvo com sucesso:\n{filepath}")
        
        except Exception as e:
            messagebox.showerror("Erro", f"Falha ao gerar PDF: {str(e)}")
    
    def clear_fields(self):
        self.client_name.set("")
        self.event_date.set("")
        self.event_type.set("")
        self.event_option.set("")
        self.guests.set(100)
        self.event_hours.set("4")
        self.adults.set(0)
        self.children.set(0)
        self.include_alcohol.set(False)
        self.include_non_alcohol.set(True)
        self.include_utensils.set(True)
        self.include_furniture.set(False)
        self.result_text.delete(1.0, tk.END)

if __name__ == "__main__":
    try:
        root = tk.Tk()
        app = BuffetCalculatorPro(root)
        root.mainloop()
    except Exception as e:
        messagebox.showerror("Erro Fatal", f"A aplicação encontrou um erro e precisa ser fechada: {str(e)}")