vendas = 1000
meta = 500

# metodo tradicional

if vendas > 500:
    bonus = 30
else:
    bonus = 0

# Com  ternary operator >>
bonus = 30 if vendas >= 500 else 0
