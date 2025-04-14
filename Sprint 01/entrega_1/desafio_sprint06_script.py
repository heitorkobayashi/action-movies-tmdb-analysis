import boto3
from datetime import datetime

#Configurações do bucket
bucket = 'data-lake-heitor-ana'
storage = 'Raw'
source = 'Local'
file = 'CSV'

#Caminhos locais dos arquivos
local_path = {
    'movies': '/desafio/entrega_1/movies.csv',
    'series': '/desafio/entrega_1/series.csv'
}

#Subdiretórios no S3
categoria_paths = {
    'movies': 'Movies',
    'series': 'Series'
}

#Data atual
hoje = datetime.now()
data_path = f"{hoje.year}/{hoje.month:02}/{hoje.day:02}"

#Função de upload dos arquivos para o S3
def upload_arquivos(s3_client, file_path, s3_path):
    try:
        s3_client.upload_file(file_path, bucket, s3_path)
        print(f'Upload de {file_path} para {s3_path} realizada com sucesso.')
    except Exception as e:
        print(f'Falha no upload de {file_path}: {str(e)}.')

#Função principal para upload dos arquivos csv
def main():

    s3_client = boto3.client(
        's3',
    )
    
    #Upload dos arquivos
    for file_key, file_path in local_path.items():
        s3_path = f"{storage}/{source}/{file}/{categoria_paths[file_key]}/{data_path}/{file_key}.csv"
        upload_arquivos(s3_client, file_path, s3_path)

#Executar o script
if __name__ == "__main__":
    main()
