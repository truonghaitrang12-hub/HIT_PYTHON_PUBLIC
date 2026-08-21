import numpy as np

kills = np.random.randint(5, 31, size=(5, 1))
deaths = np.random.randint(1, 16, size=(5, 1))
assists = np.random.randint(0, 11, size=(5, 1))
combat_score = np.random.randint(100, 401, size=(5, 1))

stats = np.hstack((kills, deaths, assists, combat_score))

print("Bang thong ke 5 tran:")
print(stats)

print("---")

recent_kda = stats[-3:, :3]

print("Bang K-D-A cua 3 tran gan nhat:")
print(recent_kda)

print("---")

kd_ratio = np.round(stats[:, 0] / stats[:, 1], 2)

print("Chi so K/D tung tran:", kd_ratio)

print("---")

print("Kills ky luc:", np.max(stats[:, 0]))
print("Tong Assists:", np.sum(stats[:, 2]))
print("Combat Score thap nhat:", np.min(stats[:, 3]))

print("---")

print("Ma tran sau khi chuyen vi:")
print(stats.T)