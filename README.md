# Calculadora Simples em Python

Este é um programa de calculadora simples em Python com uma interface gráfica Tkinter. A calculadora permite a realização de operações matemáticas básicas, como adição, subtração, multiplicação e divisão.
##Estrutura de Arquivos

O projeto é dividido em três arquivos:
### Arquivo "controller.py"

Este arquivo contém a classe Controller, que atua como o controlador da calculadora. Ele lida com a comunicação entre a interface gráfica (View) e a lógica da calculadora (Model).

    __init__(self): Inicializa o controlador, criando instâncias do modelo e da visualização.
    main(self): Inicia a interface gráfica da calculadora.
    on_button_click(self, caption): Manipula eventos de clique nos botões da calculadora e atualiza a exibição dos resultados.

### Arquivo "view.py"

Este arquivo contém a classe View, que representa a interface gráfica da calculadora. Ele cria a janela principal, a entrada de texto e os botões da calculadora.

    __init__(self, controller): Inicializa a interface gráfica, cria a janela principal e os elementos da GUI.
    main(self): Inicia a interface gráfica da calculadora.
    _make_main_frame(self): Cria o quadro principal.
    _make_entry(self): Cria a entrada de texto onde os números e os resultados são exibidos.
    _make_buttons(self): Cria os botões da calculadora e define suas ações.

### Arquivo "model.py"

Este arquivo contém a classe Model, que representa a lógica da calculadora. Ele realiza os cálculos e atualiza o estado da calculadora com base nos botões clicados.

    __init__(self): Inicializa o modelo, configurando variáveis para rastrear os valores, operadores e resultados.
    calculate(self, caption): Realiza cálculos com base no botão clicado e atualiza o estado da calculadora.
    _evaluate(self): Avalia a expressão matemática e retorna o resultado.

## Como Executar

Para executar a calculadora, siga estas etapas:

    Certifique-se de ter o Python instalado em seu sistema.
    Baixe os três arquivos (controller.py, view.py e model.py) do código-fonte da calculadora.
    Navegue até o diretório onde os arquivos estão localizados.
    Execute o arquivo "controller.py" usando o Python.

## Como Usar a Calculadora

    A calculadora oferece botões para números de 0 a 9, operadores (+, -, *, /) e ações especiais (C para limpar, +/- para inverter o sinal, < para apagar um dígito, . para ponto decimal e = para calcular).
    Clique nos botões para inserir números e operadores.
    Use o botão "=" para calcular o resultado.
    O resultado será exibido na entrada de texto na parte superior da calculadora.
    Use o botão "C" para limpar a entrada.
    Você pode inverter o sinal de um número clicando em "+/-".
    Use "<" para apagar um dígito da entrada.

## Créditos

Este projeto foi desenvolvido por Otaviano Silva e é distribuído sob a licença minha licença. Você pode encontrar o código-fonte completo no neste repositório

Aproveite a calculadora!
