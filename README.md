# Lembrete de creatina

Este projeto exibe uma notificação no Windows para lembrar o usuário de tomar creatina.

## Requisitos

- Windows 10 ou 11
- Python 3.12 ou superior
- Acesso ao terminal (PowerShell ou Prompt de Comando)
- Arquivo de imagem `creatina.png` na mesma pasta do script

## Estrutura esperada do projeto

```text
Notification/
├── creatina.png
├── notification.py
└── README.md
```

> Importante: o arquivo `notification.py` deve estar na mesma pasta que a imagem `creatina.png`.

## Como rodar

### 1) Instale o Python

Baixe e instale o Python 3.12 ou superior em:

https://www.python.org/downloads/

Durante a instalação, marque a opção:

- Add Python to PATH

Depois, confirme se o Python está funcionando:

```powershell
python --version
```

Se o comando `python` não funcionar, use o caminho completo do executável do Python, por exemplo:

```powershell
"C:\Users\SeuUsuario\AppData\Local\Programs\Python\Python312\python.exe" --version
```

### 2) Abra o terminal na pasta do projeto

```powershell
cd "C:\caminho\para\pasta\Notification"
```

Exemplo:

```powershell
cd "C:\Users\User\Desktop\Notification"
```

### 3) Crie ou ative um ambiente virtual (opcional, mas recomendado)

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

Se o PowerShell bloquear a ativação do ambiente virtual, execute:

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
.\.venv\Scripts\Activate.ps1
```

### 4) Instale a dependência

```powershell
pip install winotify
```

### 5) Certifique-se de que os arquivos estão corretos

O projeto precisa ter:

- `notification.py`
- `creatina.png`

Se o arquivo estiver com um nome estranho, como `from winotify import notification.py`, renomeie para:

```text
notification.py
```

### 6) Execute a aplicação

```powershell
python .\notification.py
```

Se o comando `python` não existir no seu ambiente, use o caminho completo:

```powershell
& "C:\Users\SeuUsuario\AppData\Local\Programs\Python\Python312\python.exe" .\notification.py
```

## O que acontece ao executar

O script cria uma notificação do Windows com o seguinte texto:

- Título: `Já tomou a creatina?`
- Mensagem: `Não se esqueça de tomar a creatina hoje!`

A notificação aparece na área de notificações do Windows.

## Observações

- Este projeto funciona apenas no Windows.
- A imagem `creatina.png` precisa estar na mesma pasta do arquivo Python.
- Caso a notificação não apareça, verifique se o Python usado para rodar o programa é o mesmo que instalou a dependência `winotify`.

## Solução rápida para quem copiar o projeto

Se você for copiar a pasta para outro lugar, siga exatamente este fluxo:

```powershell
cd "C:\caminho\para\pasta\Notification"
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install winotify
python .\notification.py
```
