#bai1
s = input("Nhập chuỗi: ")
reverse = ""
for i in range(len(s) - 1, -1, -1):
    reverse += s[i]

print("Chuỗi đảo ngược:", reverse)
sorted_string = "".join(sorted(s))
print("Chuỗi sau khi sắp xếp:", sorted_string)
if s == reverse:
    print("Đây là chuỗi đối xứng.")
else:
    print("Đây không phải là chuỗi đối xứng.")
chars = sorted(set(s))   # Loại bỏ ký tự trùng và sắp xếp

max_count = 0
for ch in chars:
    if s.count(ch) > max_count:
        max_count = s.count(ch)

print("Ký tự xuất hiện nhiều nhất:")
for ch in chars:
    if s.count(ch) == max_count:
        print(ch, end=" ")
print()

print("Số lần xuất hiện:", max_count)
vowels = {'a', 'e', 'i', 'o', 'u'}
lower_s = s.lower()

if vowels.issubset(set(lower_s)):
    print("Chuỗi chứa đầy đủ 5 nguyên âm tiếng Anh.")
else:
    print("Chuỗi không chứa đầy đủ 5 nguyên âm tiếng Anh.")

# #bai2
# input_products = input("Nhập các sản phẩm: ")
# check_product = input("Nhập sản phẩm cần kiểm tra: ")
# products = []

# for item in input_products.split(","):
#     item = item.strip().title()
#     products.append(item)
# check_product = check_product.strip().title()
# print("\nDanh sách sản phẩm:")
# print(products)
# print("\nTổng số sản phẩm đã mua:", len(products))
# if len(products) % 2 == 1:
#     middle = len(products) // 2
#     print("\nSản phẩm ở vị trí giữa:", products[middle])
# unique_products = sorted(set(products))

# max_count = 0
# for product in unique_products:
#     if products.count(product) > max_count:
#         max_count = products.count(product)

# print("\nCác sản phẩm được mua nhiều nhất:")
# for product in unique_products:
#     if products.count(product) == max_count:
#         print(product + ":", max_count, "lần")
# count = products.count(check_product)

# if count == 0:
#     print("\n" + check_product, "chưa được mua.")
# else:
#     print("\n" + check_product, "đã được mua", count, "lần.")
# products.insert(0, "Bánh Nabati")
# if "Sữa" in products:
#     products.remove("Sữa")
# print("\nDanh sách sau khi cập nhật:")
# print(products)

# #bai3
# input_a = input("Nhập sở thích của Người A: ")
# input_b = input("Nhập sở thích của Người B: ")
# set_a = set()
# for hobby in input_a.split(","):
#     hobby = hobby.strip().title()
#     if hobby != "":
#         set_a.add(hobby)

# set_b = set()
# for hobby in input_b.split(","):
#     hobby = hobby.strip().title()
#     if hobby != "":
#         set_b.add(hobby)
# print("\nCác sở thích của Người A:")
# print(set_a)

# print("\nCác sở thích của Người B:")
# print(set_b)
# common = set_a & set_b

# print("\nSở thích chung:")
# if len(common) == 0:
#     print("Không có sở thích chung.")
# else:
#     print(common)
# only_a = set_a - set_b

# print("\nSở thích chỉ Người A có:")
# if len(only_a) == 0:
#     print("Không có.")
# else:
#     print(only_a)
# all_hobbies = set_a | set_b

# print("\nTất cả sở thích:")
# print(all_hobbies)
# if len(all_hobbies) == 0:
#     similarity = 0
# else:
#     similarity = len(common) / len(all_hobbies) * 100

# print("\nĐộ tương đồng: {:.2f}%".format(similarity))

# #bai4
# n = int(input("Nhập số lượng khoản chi: "))
# expenses = []
# for i in range(n):
#     data = input(f"Nhập khoản chi {i+1}: ")
#     name, money, category = data.split(",")

#     name = name.strip()
#     money = int(money.strip())
#     category = category.strip()

#     expense = (name, money, category)
#     expenses.append(expense)

# print("\nDanh sách các khoản chi:")
# for expense in expenses:
#     print(expense)
# total = 0
# for expense in expenses:
#     total += expense[1]

# print("\nTổng chi tiêu:", total, "VNĐ")
# print("\nThống kê theo danh mục:")

# stats = {}

# for expense in expenses:
#     category = expense[2]
#     money = expense[1]

#     if category not in stats:
#         stats[category] = [1, money]
#     else:
#         stats[category][0] += 1
#         stats[category][1] += money

# for category in stats:
#     print("\n" + category + ":")
#     print("- Số khoản chi:", stats[category][0])
#     print("- Tổng tiền:", stats[category][1], "VNĐ")
# if total > 5000000:
#     print("\nTổng chi tiêu vượt quá 5.000.000 VNĐ.")
# max_expense = expenses[0]

# for expense in expenses:
#     if expense[1] > max_expense[1]:
#         max_expense = expense

# print("\nKhoản chi có số tiền lớn nhất:")
# print(max_expense)