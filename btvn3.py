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