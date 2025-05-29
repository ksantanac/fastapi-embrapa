import os
import requests
from bs4 import BeautifulSoup

class VitiBrasilScraper:
    def __init__(self):
        # Configurações
        self.base_url = "http://vitibrasil.cnpuv.embrapa.br/index.php"
        self.download_base = "http://vitibrasil.cnpuv.embrapa.br/"
        self.data_dir = "data"
        
        os.makedirs(self.data_dir, exist_ok=True)
        
        self.main_page_soup = None

    def get_main_page(self):
        """Obtém e armazena a página principal"""
        print("Acessando página principal...")
        response = requests.get(self.base_url)
        response.raise_for_status()
        self.main_page_soup = BeautifulSoup(response.text, 'html.parser')

    def download_file(self, url, subfolder, filename):
        """Baixa um arquivo e salva na subpasta correspondente"""
        # Criar subpasta se não existir
        subfolder_path = os.path.join(self.data_dir, subfolder)
        os.makedirs(subfolder_path, exist_ok=True)
        
        filepath = os.path.join(subfolder_path, filename)
        with requests.get(url, stream=True) as r:
            r.raise_for_status()
            with open(filepath, 'wb') as f:
                for chunk in r.iter_content(chunk_size=8192):
                    f.write(chunk)
        print(f"Arquivo salvo em: {filepath}")
        return filepath

    def process_option(self, option_value, option_name=None):
        """Processa uma opção principal, com ou sem subopções"""
        print(f"\n=== Processando {option_name or option_value} ===")
        
        # Acessar página da opção
        option_url = f"{self.base_url}?opcao={option_value}"
        option_resp = requests.get(option_url)
        option_resp.raise_for_status()
        option_soup = BeautifulSoup(option_resp.text, 'html.parser')

        # Verificar se existem subopções
        suboptions = option_soup.find_all('button', {'name': 'subopcao'})
        
        if suboptions:
            print(f"Encontradas {len(suboptions)} subopções:")
            self.process_suboptions(option_value, option_name, suboptions, option_soup)
        else:
            # Se não houver subopções, tentar baixar diretamente
            download_link = option_soup.find('a', {'class': 'footer_content', 'href': True})
            if download_link:
                download_url = self.download_base + download_link['href']
                filename = f"{option_name or option_value}.csv"
                print(f"Baixando arquivo principal: {download_url}")
                self.download_file(download_url, option_name or option_value, filename)
            else:
                print(f"AVISO: Nenhum link de download encontrado para {option_name or option_value}")

    def process_suboptions(self, main_option_value, main_option_name, suboptions, option_soup):
        """Processa todas as subopções de uma opção principal"""
        for suboption in suboptions:
            suboption_name = suboption.text.strip()
            suboption_value = suboption['value']
            print(f"\n- Subopção: {suboption_name} ({suboption_value})")
            
            # Acessar página da subopção
            suboption_url = f"{self.base_url}?opcao={main_option_value}&subopcao={suboption_value}"
            suboption_resp = requests.get(suboption_url)
            suboption_resp.raise_for_status()
            suboption_soup = BeautifulSoup(suboption_resp.text, 'html.parser')
            
            # Encontrar link de download
            download_link = suboption_soup.find('a', {'class': 'footer_content', 'href': True})
            if download_link:
                download_url = self.download_base + download_link['href']
                filename = f"{suboption_name}.csv".replace(" ", "_")
                print(f"Baixando: {download_url}")
                self.download_file(download_url, main_option_name or main_option_value, filename)
            else:
                print(f"AVISO: Link de download não encontrado para {suboption_name}")

    def scrape_all(self):
        """Executa o scraping completo para todas as opções conhecidas"""
        self.get_main_page()
        
        # Opções sem subopções
        simple_options = [
            {'value': 'opt_02', 'name': 'Producao'},
            {'value': 'opt_04', 'name': 'Comercializacao'}
        ]
        
        # Opções com subopções
        complex_options = [
            {'value': 'opt_03', 'name': 'Processamento'},
            {'value': 'opt_05', 'name': 'Importacao'},
            {'value': 'opt_06', 'name': 'Exportacao'}
        ]
        
        # Processar todas as opções
        for option in simple_options + complex_options:
            self.process_option(option['value'], option['name'])
        
        print("\nProcesso concluído com sucesso!")


