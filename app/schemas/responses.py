from pydantic import BaseModel, Field
from typing import Optional, List


class Producao(BaseModel):
    produtor: str = Field(description="Nome do produtor")
    quantidade: float = Field(description="Quantidade produzida")
    ano: int = Field(description="Ano da importação")


class Processamento(BaseModel):
    tipo: str = Field(description="Tipo de processamento")
    quantidade: float = Field(description="Quantidade processada")
    ano: int = Field(description="Ano do processamento")


class Comercializacao(BaseModel):
    produto: str = Field(description="Nome do produto comercializado")
    quantidade: float = Field(description="Quantidade processada")
    ano: int = Field(description="Ano da comercialização")


class Exportacao(BaseModel):
    pais_destino: str = Field(description="País de destino da exportação")
    quantidade: float = Field(description="Quantidade exportada")
    valor: float = Field(description="Valor exportado")
    ano: int = Field(description="Ano da exportação")


class Importacao(BaseModel):
    pais_origem: str = Field(description="País de origem da importação")
    quantidade: float = Field(description="Quantidade importada")
    valor: float = Field(description="Valor importado")
    ano: int = Field(description="Ano da importação")


