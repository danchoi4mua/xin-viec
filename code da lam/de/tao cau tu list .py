"""Yêu cầu:

Viết một chương trình để tạo tất cả các câu có chủ ngữ nằm trong ["Anh","Em"], động từ nằm trong ["Chơi","Yêu"] và tân ngữ là ["Bóng đá","Xếp hình"].

Gợi ý:

Sử dụng list[index] để lấy phần tử từ list."""



#bai giai

chu_ngu=["Anh","Em"]
dong_tu=["Chơi","Yêu"]
tan_ngu=["Bóng đá","Xếp hình"]
for i in chu_ngu:
    for j in dong_tu:
        for k in tan_ngu:
            print (i,j,k)