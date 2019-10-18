# Python 3.8+ only

a = [1, 2, 3]

# Avoid calling len() twice
if (n := len(a)) > 10:
    print(f"List is too long ({n} elements, expected <= 10)")


# n = len(a)
# if n > 10:
#     print(n)
#
# if len(a) > 10:
#     print(len(a))


f = open('/tmp/tmp.txt')

# Loop over fixed length blocks
while (block := f.read(256)) != '':
    process(block)


block = f.read(256)
while block != '':
    process(block)
    block = f.read(256)
#
while True:
    block = f.read(256)
    if not block:
        break

    process(block)
