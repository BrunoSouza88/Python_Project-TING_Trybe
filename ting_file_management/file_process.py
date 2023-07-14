import sys


def process(path_file, instance):
    for item in instance.queue:
        if item['nome_do_arquivo'] == path_file:
            return

    with open(path_file, 'r') as f:
        lines = [line.rstrip('\n') for line in f]

    data = {
        'nome_do_arquivo': path_file,
        'qtd_linhas': len(lines),
        'linhas_do_arquivo': lines
    }

    instance.enqueue(data)

    print(data)


def remove(instance):
    try:
        data = instance.dequeue()
        print(f"Arquivo {data['nome_do_arquivo']} removido com sucesso")
    except IndexError:
        print("Não há elementos")


def file_metadata(instance, position):
    try:
        data = instance.search(position)
        print(data)
    except IndexError:
        sys.stderr.write("Posição inválida")
