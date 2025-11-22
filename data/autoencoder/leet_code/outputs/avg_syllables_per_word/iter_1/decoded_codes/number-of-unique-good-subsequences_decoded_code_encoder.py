MOD = 10**9 + 7
end0, end1 = 0, 0
has0 = ('0' in binary)

for bit in binary:
    if bit == '1':
        end1 = (end0 + end1 + 1) % MOD
    else:
        end0 = (end0 + end1) % MOD

return (end0 + end1 + has0) % MOD