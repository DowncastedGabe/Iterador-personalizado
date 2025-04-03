from typing import Iterator, Dict, Any

class Containerador:
    def __init__(self, contas: list[Dict[str, Any]]):
        """
        Inicializa o iterador com a lista de contas bancárias.
        
        Args:
            contas: Lista de dicionários contendo informações das contas
                   Cada conta deve ter pelo menos:
                   - 'numero': str (número da conta)
                   - 'saldo': float
                   - 'titular': str (nome do titular)
        """
        self.contas = contas
        self._index = 0  # Índice para controle da iteração

    def __iter__(self) -> Iterator[Dict[str, Any]]:
        """Retorna o próprio objeto como iterador."""
        self._index = 0  # Reinicia o índice a cada nova iteração
        return self

    def __next__(self) -> Dict[str, Any]:
        """Retorna a próxima conta da lista."""
        if self._index < len(self.contas):
            conta = self.contas[self._index]
            self._index += 1
            return {
                'numero': conta['numero'],
                'saldo': conta['saldo'],
                'titular': conta['titular']
                # Adicione outros campos conforme necessário
            }
        raise StopIteration  # Finaliza a iteração quando não há mais contas
    

# Exemplo de dados de contas bancárias
contas_banco = [
    {'numero': '12345-6', 'saldo': 1500.0, 'titular': 'João Silva'},
    {'numero': '78901-2', 'saldo': 3200.5, 'titular': 'Maria Souza'},
    {'numero': '34567-8', 'saldo': 500.0, 'titular': 'Carlos Oliveira'}
]

# Criar o iterador
iterador_contas = Containerador(contas_banco)

# Iterar sobre todas as contas
print("Contas do banco:")
for conta in iterador_contas:
    print(f"Número: {conta['numero']}")
    print(f"Titular: {conta['titular']}")
    print(f"Saldo: R${conta['saldo']:.2f}")
    print("-" * 30)