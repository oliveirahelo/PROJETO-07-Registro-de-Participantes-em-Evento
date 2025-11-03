# PROJETO 07 — Registro de Participantes em Evento
# Autor: Professor Ricardo Rodrigues Lima
# Linguagem: Python 3

def linha():
    print("-" * 60)

def main():
    print("=" * 60)
    print("🎟️  SISTEMA DE REGISTRO DE PARTICIPANTES EM EVENTO")
    print("=" * 60)

    participantes = []

    while True:
        nome = input("\nDigite o nome do participante (ou 'sair' para encerrar): ").strip()
        if nome.lower() == "sair":
            break

        email = input("Digite o e-mail: ").strip()
        cpf = input("Digite o CPF: ").strip()

        participante = {
            "nome": nome,
            "email": email,
            "cpf": cpf
        }

        participantes.append(participante)
        print(f"✅ Participante '{nome}' cadastrado com sucesso!")

    linha()
    print("📋 LISTA FINAL DE PARTICIPANTES")
    linha()

    if not participantes:
        print("⚠️ Nenhum participante cadastrado.")
    else:
        print(f"{'NOME':<20}{'E-MAIL':<25}{'CPF':<15}")
        linha()
        for p in participantes:
            print(f"{p['nome']:<20}{p['email']:<25}{p['cpf']:<15}")
        linha()
        print(f"👥 Total de inscritos: {len(participantes)}")

    linha()
    print("✅ Encerrando o sistema. Até a próxima!")

if __name__ == "__main__":
    main()