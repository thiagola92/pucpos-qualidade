# Backend
O backend utiliza:
- Package manager: [uv](https://docs.astral.sh/uv/)  
- API framekwork: [FastAPI](https://fastapi.tiangolo.com/)  
- Test framework: [pytest](https://docs.pytest.org/en/stable/)  

# Utilização
> [!WARNING]  
> É preciso ter o package manager uv instalado para seguir as instruções seguintes: https://docs.astral.sh/uv/getting-started/installation/  

> [!NOTE]  
> Os códigos seguintes supões que você está localizado no diretório `backend`.  
> Não confundir com `pucpos-qualidade` (diretório pai) que é apenas responsável por armazenar os diretórios.  

Instalação das dependências:  
```
uv sync
```

Inicializar o backend em development mode:  
```
uv run fastapi dev app.py
```

Após isso o framework irá monitorar mudanças nos arquivos e atualizar o backend quando tiver alterações. Acesse a API pelo seguinte URL: http://127.0.0.1:8000  

Execução dos testes:  
```
python -m pytest
```

# Referências
- https://fastapi.tiangolo.com/
- https://fastapi.tiangolo.com/advanced/additional-status-codes/
- https://docs.pytest.org/en/stable/