from app.services.embrapa import model


PRODUCAO_URL: str = "http://vitibrasil.cnpuv.embrapa.br/download/Producao.csv"
PROCESSAMENTO_VINIFERAS_URL: str = "http://vitibrasil.cnpuv.embrapa.br/download/ProcessaViniferas.csv"
PROCESSAMENTO_AMERICANAS_URL: str = "http://vitibrasil.cnpuv.embrapa.br/download/ProcessaAmericanas.csv"
PROCESSAMENTO_UVAS_MESA_URL: str = "http://vitibrasil.cnpuv.embrapa.br/download/ProcessaMesa.csv"
PROCESSAMENTO_SEM_CLASSIFICACAO_URL: str = "http://vitibrasil.cnpuv.embrapa.br/download/ProcessaSemclass.csv"
COMERCIALIZACAO_URL: str = "http://vitibrasil.cnpuv.embrapa.br/download/Comercio.csv"
IMPORTACAO_VINHO_MESA_URL: str = "http://vitibrasil.cnpuv.embrapa.br/download/ImpVinhos.csv"
IMPORTACAO_ESPUMANTES_URL: str = "http://vitibrasil.cnpuv.embrapa.br/download/ImpEspumantes.csv"
IMPORTACAO_UVAS_FRESCAS_URL: str = "http://vitibrasil.cnpuv.embrapa.br/download/ImpFrescas.csv"
IMPORTACAO_UVAS_PASSAS_URL: str = "http://vitibrasil.cnpuv.embrapa.br/download/ImpPassas.csv"
IMPORTACAO_SUCO_DE_UVA_URL: str = "http://vitibrasil.cnpuv.embrapa.br/download/ImpSuco.csv"
EXPORTACAO_VINHO_MESA_URL: str = "http://vitibrasil.cnpuv.embrapa.br/download/ExpVinho.csv"
EXPORTACAO_ESPUMANTES_URL: str = "http://vitibrasil.cnpuv.embrapa.br/download/ExpEspumantes.csv"
EXPORTACAO_UVAS_FRESCAS_URL: str = "http://vitibrasil.cnpuv.embrapa.br/download/ExpUva.csv"
EXPORTACAO_SUCO_DE_UVA_URL: str = "http://vitibrasil.cnpuv.embrapa.br/download/ExpSuco.csv"


data_sources = [
    {
        "source": "Producao",
        "target": "stg_producao",
        "url": PRODUCAO_URL,
        "delimiter": ";",
        "has_header": True,
        "schema": model.producao_schema,
        "tag": "PRODUCAO",
    },
    {
        "source": "Processamento Viniferas",
        "target": "stg_processamento",
        "url": PROCESSAMENTO_VINIFERAS_URL,
        "delimiter": ";",
        "has_header": True,
        "schema": model.processamento_schema,
        "tag": "VINIFERAS",
    },
    {
        "source": "Processamento Americanas",
        "target": "stg_processamento",
        "url": PROCESSAMENTO_AMERICANAS_URL,
        "delimiter": "\t",
        "has_header": True,
        "schema": model.processamento_schema,
        "tag": "AMERICANAS",
    },
    {
        "source": "Processamento Uvas Mesa",
        "target": "stg_processamento",
        "url": PROCESSAMENTO_UVAS_MESA_URL,
        "delimiter": "\t",
        "has_header": True,
        "schema": model.processamento_schema,
        "tag": "UVAS_MESA",
    },
    {
        "source": "Processamento Sem Classificacao",
        "target": "stg_processamento",
        "url": PROCESSAMENTO_SEM_CLASSIFICACAO_URL,
        "delimiter": "\t",
        "has_header": True,
        "schema": model.processamento_schema,
        "tag": "SEM_CLASSIFICACAO",
    },
    {
        "source": "Comercializacao",
        "target": "stg_comercializacao",
        "url": COMERCIALIZACAO_URL,
        "delimiter": ";",
        "has_header": True,
        "schema": model.comercializacao_schema,
        "tag": "COMERCIALIZACAO",
    },
    {
        "source": "Importacao Vinho Mesa",
        "target": "stg_importacao",
        "url": IMPORTACAO_VINHO_MESA_URL,
        "delimiter": "\t",
        "has_header": True,
        "schema": model.importacao_exportacao_schema,
        "tag": "VINHO_MESA",
    },
    {
        "source": "Importacao Espumantes",
        "target": "stg_importacao",
        "url": IMPORTACAO_ESPUMANTES_URL,
        "delimiter": "\t",
        "has_header": True,
        "schema": model.importacao_exportacao_schema,
        "tag": "ESPUMANTES",
    },
    {
        "source": "Importacao Uvas Frescas",
        "target": "stg_importacao",
        "url": IMPORTACAO_UVAS_FRESCAS_URL,
        "delimiter": "\t",
        "has_header": True,
        "schema": model.importacao_exportacao_schema,
        "tag": "UVAS_FRESCAS",
    },
    {
        "source": "Importacao Uvas Passas",
        "target": "stg_importacao",
        "url": IMPORTACAO_UVAS_PASSAS_URL,
        "delimiter": "\t",
        "has_header": True,
        "schema": model.importacao_exportacao_schema,
        "tag": "UVAS_PASSAS",
    },
    {
        "source": "Importacao Suco de Uva",
        "target": "stg_importacao",
        "url": IMPORTACAO_SUCO_DE_UVA_URL,
        "delimiter": ";",
        "has_header": True,
        "schema": model.importacao_exportacao_schema,
        "tag": "SUCO_DE_UVA",
    },
    {
        "source": "Exportacao Vinho Mesa",
        "target": "stg_exportacao",
        "url": EXPORTACAO_VINHO_MESA_URL,
        "delimiter": "\t",
        "has_header": True,
        "schema": model.importacao_exportacao_schema,
        "tag": "VINHO_MESA",
    },
    {
        "source": "Exportacao Espumantes",
        "target": "stg_exportacao",
        "url": EXPORTACAO_ESPUMANTES_URL,
        "delimiter": "\t",
        "has_header": True,
        "schema": model.importacao_exportacao_schema,
        "tag": "ESPUMANTES",
    },
    {
        "source": "Exportacao Uvas Frescas",
        "target": "stg_exportacao",
        "url": EXPORTACAO_UVAS_FRESCAS_URL,
        "delimiter": "\t",
        "has_header": True,
        "schema": model.importacao_exportacao_schema,
        "tag": "UVAS_FRESCAS",
    },
    {
        "source": "Exportacao Suco de Uva",
        "target": "stg_exportacao",
        "url": EXPORTACAO_SUCO_DE_UVA_URL,
        "delimiter": "\t",
        "has_header": True,
        "schema": model.importacao_exportacao_schema,
        "tag": "SUCO_DE_UVA",
    },
]
