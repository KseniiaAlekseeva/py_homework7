input = "1=hi 2=hello 3=morning 4=afternoon"
tp = tuple(map(lambda x: tuple(x.split('=')), input.split()))
print(tp)
