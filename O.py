def restore_access(file_permissions, queries):
    access = {}
    for file, permissions in file_permissions.items():
        access[file] = set(permissions)

    results = []
    for query in queries:
        operation, file = query.split()
        if operation in access.get(file, set()):
            results.append("OK")
        else:
            results.append("Access denied")
    return results

# Вхідні дані
N = int(input())  # кількість файлів
file_permissions = {}
for _ in range(N):
    file, permissions = input().split(maxsplit=1)
    file_permissions[file] = permissions.split()

M = int(input())  # кількість запитів
queries = [input() for _ in range(M)]

# Результат
results = restore_access(file_permissions, queries)
for result in results:
    print(result)
