from dataclasses import dataclass, field
from typing import *

@dataclass
class IMOVEL: #Cria um registro para oos Imovéis
    codigoImovel: int = 0 #código de cada imovel para caso o proprietário ou o Corretor queira acessalo
    tipo: str = ''
    rua: str = ''
    setor: str = ''
    NCasa: str = ''
    tamanho: float = 0
    quarto: int = 0
    tamanhoQuarto: list = field(default_factory=list)
    banheiro: int = 0
    tamanhoBanheiro: list = field(default_factory=list)
    status: str = ''

@dataclass
class CLIENTE: #Cria um registro para o Cliente
    nome: str = ''
    cpf: str = ''
    rg: str = 0

@dataclass
class CORRETOR: #Cria um registro para o Corretor
    cod: str = 0
    imovelRegistrado: list = field(default_factory=list)
    nome: str = ''
    cpf: str = ''
    rg: str = 0

@dataclass
class PROPRIETARIO: #Cria um registro para o Proprietário
    cod: str = 0
    nome: str = ''
    cpf: str = ''
    rg: str = 0
    imovelPossuido: list = field(default_factory=list)