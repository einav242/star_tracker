import os

from main import find_matching_stars, show_stars

file1 = "fr1.jpg"
file1 = os.path.join("data_test", file1)
file2 = "fr2.jpg"
file2 = os.path.join("data_test", file2)
file3 = "ST_db1.jpg"
file3 = os.path.join("data_test", file3)
file4 = "ST_db2.jpg"
file4 = os.path.join("data_test", file4)

filename1 = "%s_processed.jpg" % file1
filename2 = "%s_processed.jpg" % file2
filename3 = "%s_processed.jpg" % file3
filename4 = "%s_processed.jpg" % file4

output = "output_fr1_fr2.txt"
output = os.path.join("result", output)
temp_list = find_matching_stars(file1, file2, output)
output_img = "output_fr1_fr2.jpg"
output_img = os.path.join("result", output_img)
show_stars(filename1, filename2, temp_list, output_img)
tmp = [(m[0].id, m[1].id) for m in temp_list]
print(file1, "vs.", file2, "= ", tmp)

output = "output_fr1_ST_db1.txt"
output = os.path.join("result", output)
temp_list = find_matching_stars(file1, file3, output)
output_img = "output_fr1_ST_db1.jpg"
output_img = os.path.join("result", output_img)
show_stars(filename1, filename3, temp_list, output_img)
tmp = [(m[0].id, m[1].id) for m in temp_list]
print(file1, "vs.", file3, "= ", tmp)

output = "output_fr1_ST_db2.txt"
output = os.path.join("result", output)
temp_list = find_matching_stars(file1, file4, output)
output_img = "output_fr1_ST_db2.jpg"
output_img = os.path.join("result", output_img)
show_stars(filename1, filename4, temp_list, output_img)
tmp = [(m[0].id, m[1].id) for m in temp_list]
print(file1, "vs.", file4, "= ", tmp)

output = "output_fr2_fr1.txt"
output = os.path.join("result", output)
temp_list = find_matching_stars(file2, file1, output)
output_img = "output_fr2_fr1.jpg"
output_img = os.path.join("result", output_img)
show_stars(filename2, filename1, temp_list, output_img)
tmp = [(m[0].id, m[1].id) for m in temp_list]
print(file2, "vs.", file1, "= ", tmp)

output = "output_fr2_ST_db1.txt"
output = os.path.join("result", output)
temp_list = find_matching_stars(file2, file3, output)
output_img = "output_fr2_ST_db1.jpg"
output_img = os.path.join("result", output_img)
show_stars(filename2, filename3, temp_list, output_img)
tmp = [(m[0].id, m[1].id) for m in temp_list]
print(file2, "vs.", file3, "= ", tmp)

output = "output_fr2_ST_db2.txt"
output = os.path.join("result", output)
temp_list = find_matching_stars(file2, file4, output)
output_img = "output_fr2_ST_db2.jpg"
output_img = os.path.join("result", output_img)
show_stars(filename2, filename4, temp_list, output_img)
tmp = [(m[0].id, m[1].id) for m in temp_list]
print(file2, "vs.", file4, "= ", tmp)

output = "output_ST_db1_fr1.txt"
output = os.path.join("result", output)
temp_list = find_matching_stars(file3, file1, output)
output_img = "output_ST_db1_fr1.jpg"
output_img = os.path.join("result", output_img)
show_stars(filename3, filename1, temp_list, output_img)
tmp = [(m[0].id, m[1].id) for m in temp_list]
print(file3, "vs.", file1, "= ", tmp)

output = "output_ST_db1_fr2.txt"
output = os.path.join("result", output)
temp_list = find_matching_stars(file3, file2, output)
output_img = "output_ST_db1_fr2.jpg"
output_img = os.path.join("result", output_img)
show_stars(filename3, filename2, temp_list, output_img)
tmp = [(m[0].id, m[1].id) for m in temp_list]
print(file3, "vs.", file2, "= ", tmp)

output = "output_ST_db1_ST_db2.txt"
output = os.path.join("result", output)
temp_list = find_matching_stars(file3, file4, output)
output_img = "output_ST_db1_ST_db2.jpg"
output_img = os.path.join("result", output_img)
show_stars(filename3, filename4, temp_list, output_img)
tmp = [(m[0].id, m[1].id) for m in temp_list]
print(file3, "vs.", file4, "= ", tmp)

output = "output_ST_db2_fr1.txt"
output = os.path.join("result", output)
temp_list = find_matching_stars(file4, file1, output)
output_img = "output_ST_db2_fr1.jpg"
output_img = os.path.join("result", output_img)
show_stars(filename4, filename1, temp_list, output_img)
tmp = [(m[0].id, m[1].id) for m in temp_list]
print(file4, "vs.", file1, "= ", tmp)

output = "output_ST_db2_fr2.txt"
output = os.path.join("result", output)
temp_list = find_matching_stars(file4, file2, output)
output_img = "output_ST_db2_fr2.jpg"
output_img = os.path.join("result", output_img)
show_stars(filename4, filename2, temp_list, output_img)
tmp = [(m[0].id, m[1].id) for m in temp_list]
print(file4, "vs.", file2, "= ", tmp)

output = "output_ST_db2_ST_db1.txt"
output = os.path.join("result", output)
temp_list = find_matching_stars(file4, file3, output)
output_img = "output_ST_db2_ST_db1.jpg"
output_img = os.path.join("result", output_img)
show_stars(filename4, filename3, temp_list, output_img)
tmp = [(m[0].id, m[1].id) for m in temp_list]
print(file4, "vs.", file3, "= ", tmp)