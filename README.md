# Arquitetura padrão para API's v2.1


## Início 
Padrão deve ser utilizado na construção das API's python de forma a padronizar entradas, saídas, logs, excessões... entre outros, quaisquer sujestões de mudanças ou bugs encontrados devem ser reportados para atualizações futuras.


### Pré-requisitos
Todo o projeto foi adaptado para rodar em _containers_ do Docker. Então, para levantar a aplicação localmente é necessário ter instalado o [docker](https://docs.docker.com/install/) e o [docker-compose](https://docs.docker.com/compose/install/).  
```sh
user@usuer:/$ docker -v
Docker version 18.09.7, build 2d0083d

user@usuer:/$ docker-compose -v
docker-compose version 1.24.1, build 4667896b
```
Depois de instalado é necessário construir as imagens docker das API's do projeto.
```sh
user@usuer:$ docker-compose build
```

## Iniciar a aplicação
Para o projeto funcionar, é necessário que todas as suas APIs estejam de pé. Para isso, basta levantar todos os containers através do ``docker-compose up``.
```sh
user@usuer:/$ docker-compose up
```

## Utilização
É necessário a utilização:
- Objeto ControllResponse, que se encontra em projeto.utils.Response na resposta de saída da api, sendo sucesso ou erro.
- Objeto ControllLog, que se encontra em projeto.utils.Logger para padronização dos logs da api, obs.: em cada metodo está documentado sobre quando utilizar cada tipo.
```
        try:
            teste = request_data["teste"]

        except KeyError as error:
            response = objResponse.send_exception(objError=error, messages=Message.ERROR_BO, status=CodeHttp.ERROR_500)
            objLogger.error(message=Message.ERROR_BO)

        else:
            response = objResponse.send_success(messages=Message.SUCESS_EXEMPLO, status=CodeHttp.SUCCESS_200, data=teste)
            objLogger.success(messages=Message.SUCESS_EXEMPLO)
```

## Variáveis de ambiente
A nova api está seguindo o padrão do Banco do Brasil na utilização das variáveis de ambiente para facilitar o processo de Deploy.
Apenas serão declaradas como variáveis de ambiente os hiperparâmetros, PATH's, Rotas e Endpoints. IMPORTANTE: fique ciente todas as variáveis declaradas nas variáveis de ambiente será automaticamente convertidas para STRING pelo proprio sistema, no arquivo não há necessidade da utilização de aspas. 

- enviroment
```
FLASK_HOST=0.0.0.0
FLASK_PORT=5000
FLASK_URL_FIX=/api

ROUTE=/teste
ENDPOINTS=endpoint
PATH_LOG=./log_project_name
```
- settings.py

```
FLASK_DEBUG = True  # Do not use debug mode in production
FLASK_SERVER_NAME = None
RESTPLUS_VALIDATE = True
RESTPLUS_MASK_SWAGGER = False
RESTPLUS_SWAGGER_UI_DOC_EXPANSION = list
RESTPLUS_ERROR_404_HELP = False

FLASK_HOST = os.environ.get('FLASK_HOST')
FLASK_PORT = os.environ.get('FLASK_PORT')

FLASK_URL_FIX = os.environ.get("FLASK_URL_FIX")
ROUTE = os.environ.get("ROUTE")
ENDPOINTS = os.environ.get("ENDPOINTS")

PATH_LOG = os.environ.get("PATH_LOG")
```


