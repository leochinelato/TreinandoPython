import requests

lista = []

def pegar_carro(veiculos, marca):
    url = f'https://parallelum.com.br/fipe/api/v1/{veiculos}/marcas'
    response = requests.get(url)
    if response.status_code == 200:
        dados = response.json()
        for d in dados:
            print(d['nome'])
            if d.get('nome') == marca:
                marca_response = requests.get(f'https://parallelum.com.br/fipe/api/v1/carros/marcas/{d['codigo']}/modelos/')
                dados_marca = marca_response.json()
                return dados_marca
    return None
    

def pegar_tipo(categoria):
    url = f'https://parallelum.com.br/fipe/api/v1/{categoria}/marcas'
    response = requests.get(url)
    if response.status_code == 200:
        dados = response.json()
        for d in dados:
            lista.append(d['nome'])
        lista_nao_duplicada = (list(set(lista)))
        return sorted(lista_nao_duplicada)
    return 'teste'


if __name__ == '__main__':
    carros = pegar_tipo('carros')
    print(carros)
