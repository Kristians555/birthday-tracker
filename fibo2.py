# def fib(n: int) -> int:
#     if n<=1: return 0
#     if n== 2: return 1
#     a, b = 0, 1
#     for i in range(n-2):
#         a, b = b, a+b
#     return b

# for i in range(1,500):
#     print(fib(i))

yield = return bet nebeidz funkciju
def fib(n: int) -> int:
    yield 0 
    if n>=2: yield 1
    a, b = 0, 1
    for i in range(n-2):
        a, b = b, a+b
        yield b

for i in fib(50):
    print(x)




from sys import getsizeof

def compress(gene: str)->int:
    res = 1
    for c in gene.upper():
        res <<= 2
        if c=='A':
            res |= 0b00
        elif c=='C':
            res |= 0b01
        elif c=='G':
            res |= 0b10
        else:
            res |= 0b11 # T
    return res

gene = 'ACGTAGCTGATCGTAGCTAGTCGAACAGCTGATGCTAGTCGATGCTAG'
print(getsizeof(gene))
c_gene = compress(gene)
print("c_gene:", c_gene)
print(getsizeof(c_gene))

#huffman coding !!!!!!{}{}{}{}{}{}{
# }{}{}{}{}{}{}{}{}{}{}[][][][][][]
# [][][][][][][][][][][][]][][][][]
# [][][][][][][][][][][][][][][][]{
    #python svgwrite
    # ][][][][][][][][][][
    #][][][]
    #####apla S - pi, r kvadrata