while True:
    def multiplicador(multiplicador):
        def multiplicar(numero):
            return numero * multiplicador
        return multiplicar

    nome_funcao_usuario = input("Crie sua função (nome): ").lower()
    multiplicador_usuario = int(input("Crie sua função (multiplicador): "))

    funcao_usuario = multiplicador(multiplicador_usuario)
    numero_usuario = int(input(f"Insira uma numero para ser multiplicado pela sua função {nome_funcao_usuario}(): "))
    executar = funcao_usuario(numero_usuario)

    print(f"{nome_funcao_usuario}({numero_usuario}) = ",executar)