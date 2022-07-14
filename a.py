import hashlib

my_str = 'some long string'

# ✅ encode str to bytes
my_hash = hashlib.sha256(my_str.encode('utf-8')).hexdigest()

# 👇️ 884b1cd6959c81bc443b50a6cb38813ecb21e20d05690aa2109014e5f8ecb8f6
print(my_hash)