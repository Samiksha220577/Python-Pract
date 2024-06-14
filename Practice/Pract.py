def count_triangles(adj_matrix):
    n = len(adj_matrix)
    count = 0

    # Calculate A^3 (matrix multiplication)
    A3 = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                A3[i][j] += adj_matrix[i][k] * adj_matrix[k][j]

    # Count triangles
    for i in range(n):
        count += A3[i][i] // 2  # Each triangle is counted 6 times

    return count

# Example usage
edges = [(1, 2), (2, 3), (3, 1), (4, 5), (5, 6), (6, 4)]
n = 6
adj_matrix = [[0] * n for _ in range(n)]

for u, v in edges:
    adj_matrix[u - 1][v - 1] = 1
    adj_matrix[v - 1][u - 1] = 1

triangles = count_triangles(adj_matrix)
print(f"Number of triangles: {triangles}")
