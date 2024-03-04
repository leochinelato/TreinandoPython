import requests


def pegar_carro(veiculos, marca):
    url = f'https://parallelum.com.br/fipe/api/v1/{veiculos}/marcas'
    response = requests.get(url)
    if response.status_code == 200:
        dados = response.json()
        # Preciso dizer a marca do carro que quero, ou seja, o value da key nome dentro da lista dados
        for d in dados:
            if d['nome'] == marca:
                marca_response = requests.get(f'https://parallelum.com.br/fipe/api/v1/carros/marcas/{d['codigo']}/modelos/')
                dados_marca = marca_response.json()
                return dados_marca
    else:
        return None


def main():
    carros_bmw = pegar_carro('carros','BMW')
    print(carros_bmw)

if __name__ == '__main__':
    main()