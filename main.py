from matplotlib import pyplot as plt
from math import pi


def print_array(a: list):
    for elem in a:
        print(f"{elem:.3f} ", end=" ")
    print()


def get_b(n: int, l: float, i: float) -> float:
    return (4 * pi * 10 ** -7) * ((n * i) / l)


N = 2700
L = 0.167
H = 0.0002


I_n1 = 1.0
delta_fi_0_1 = 0.4
I_i_1 = [-5.0, -4.0, -3.0, -2.0, -1.0, 1.0, 2.0, 3.0, 4.0, 5.0]
delta_fi_i_1 = [0.0, 0.1, 0.2, 0.2, 0.3, 0.5, 0.6, 0.7, 0.8, 0.9]


I_n2 = 2.5
delta_fi_0_2 = 0.9
I_i_2 = [-7.0, -6.0, -5.0, -4.0, -2.5, 2.5, 4.0, 5.0, 6.0, 7.0]
delta_fi_i_2 = [0.0, 0.3, 0.6, 0.9, 1.5, 1.5, 1.9, 2.1, 2.4, 2.6]


I_n3 = 3.5
delta_fi_0_3 = 1.3
I_i_3 = [-8.0, -7.0, -6.0, -5.0, -3.5, 3.5, 5.0, 6.0, 7.0, 8.0]
delta_fi_i_3 = [-0.3, 0.0, 0.1, 0.6, 1.1, 2.4, 2.9, 3.3, 3.5, 3.9]


print("I:")
print_array(I_i_1)
print_array(I_i_2)
print_array(I_i_3)


print()


B1 = [get_b(N, L, x) for x in I_i_1]
B2 = [get_b(N, L, x) for x in I_i_2]
B3 = [get_b(N, L, x) for x in I_i_3]

print("B:")
print_array(B1)
print_array(B2)
print_array(B3)


x_y_value_1 = [B1[i] * delta_fi_i_1[i] for i in range(len(B1))]
x_square_1 = [B1[i] * B1[i] for i in range(len(B1))]
A1 = sum(x_y_value_1) / sum(x_square_1)
C1 = (sum(x_square_1) * sum(delta_fi_i_1) - sum(B1) * sum(x_y_value_1)) / (len(B1) * sum(x_square_1) - ((sum(B1)) ** 2))

x_y_value_2 = [B2[i] * delta_fi_i_2[i] for i in range(len(B2))]
x_square_2 = [B2[i] * B2[i] for i in range(len(B2))]
A2 = sum(x_y_value_2) / sum(x_square_2)
C2 = (sum(x_square_2) * sum(delta_fi_i_2) - sum(B2) * sum(x_y_value_2)) / (len(B2) * sum(x_square_2) - ((sum(B2)) ** 2))

x_y_value_3 = [B3[i] * delta_fi_i_3[i] for i in range(len(B3))]
x_square_3 = [B3[i] * B3[i] for i in range(len(B3))]
A3 = sum(x_y_value_3) / sum(x_square_3)
C3 = (sum(x_square_3) * sum(delta_fi_i_3) - sum(B3) * sum(x_y_value_3)) / (len(B3) * sum(x_square_3) - ((sum(B3)) ** 2))

print()
print(f"A1: {A1:.3f}, A2: {A2:.3f}, A3: {A3:.3f}")
print()

x_value = [x / 100 for x in range(-17, 17, 1)]


A1_value = [A1 * x for x in x_value]
A2_value = [A2 * x for x in x_value]
A3_value = [A3 * x for x in x_value]


# определение Холла
I = [I_n1, I_n2, I_n3]
A = [A1, A2, A3]

x_y_i_multi = [I[i] * A[i] for i in range(len(I))]
x_i_square = [I[i] ** 2 for i in range(len(I))]

A_for_Hola = sum(x_y_i_multi) / sum(x_i_square)
C_for_Hola = (sum(x_i_square) * sum(A) - sum(I) * sum(x_y_i_multi)) / (len(I) * sum(x_i_square) - ((sum(I)) ** 2))


print(f"A Hola: {A_for_Hola:.3f}, C Hola: {C_for_Hola - 0.4:.3f}")
print()

x_i_value = [x / 10 for x in range(0, 45, 1)]
y_i_value = [A_for_Hola * x_i_value[i] + C_for_Hola - 0.4 for i in range(len(x_i_value))]


R = [A[i] * H for i in range(len(A))]

avg_R = sum(R) / len(R)
variance_R = sum((R[i] - avg_R)**2 for i in range(len(R)))
standart_variance_R = variance_R ** 0.5

print(f"avenger R: {avg_R}")
print(f"standart variance: {standart_variance_R}")
print()

print(f"<{avg_R}> +- {standart_variance_R}")


plt.plot(I, A)
plt.scatter(I, A)

plt.plot(x_i_value, y_i_value)

plt.xlabel("I - сила тока в мА (мили Ампер)")
plt.ylabel("A - угловой коэффициент (безразмерная величина)")

plt.show()


plt.plot(B1, delta_fi_i_1, color="red")
plt.scatter(B1, delta_fi_i_1, color="red")

plt.plot(B2, delta_fi_i_2, color="green")
plt.scatter(B2, delta_fi_i_2, color="green")

plt.plot(B3, delta_fi_i_3, color="blue")
plt.scatter(B3, delta_fi_i_3, color="blue")

plt.plot(x_value, A1_value, color="red")
plt.plot(x_value, A2_value, color="green")
plt.plot(x_value, A3_value, color="blue")

plt.xlabel("B - магнитная индукция в мТЛ (мили Тесла)")
plt.ylabel("Дельта фи в мВ (мили Вольт)")

plt.axhline(0, color="black", linestyle="--")
plt.axvline(0, color="black", linestyle="--")

plt.show()
