import numpy as np

revenue = np.array([35, 42, 89, 125, 50, 80, 120, 200, 150, 220, 300, 450])

quarters = revenue.reshape(4, 3)

print("Cau truc moi:")
print("Shape:", quarters.shape)
print("Ndim:", quarters.ndim)

print("\nBao cao theo Quy:")

avg_revenue = np.mean(quarters, axis=1)
max_revenue = np.max(quarters, axis=1)

print("Doanh thu trung binh moi Quy:", avg_revenue)
print("Thang cao nhat trong moi Quy:", max_revenue)

print("\nCac thang thoa man dieu kien (80 < x <= 200):")

filtered = revenue[(revenue > 80) & (revenue <= 200)]
print(filtered)

marketing = np.array([[10], [15], [20], [30]])

report = np.hstack((quarters, marketing))

print("\nBang bao cao sau khi tich hop chi phi Marketing:")
print(report)