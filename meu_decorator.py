def decorator(func):
    def wraper(nome):
        nome = "".join(reversed(nome))
        result = func(nome)
        result = result.upper()
        return result
    return wraper

@decorator
def meu_nome(nome):
    return f"Meu nome é {nome}"

print(meu_nome("Daniel"))
