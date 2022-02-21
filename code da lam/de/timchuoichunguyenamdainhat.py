def findSubstring(s, k):
    trum=""
    sotrum=0
    chu_nguyen_am_dem_duoc=0
    thong_tin_chuoi={}
    for so_dem in range(len(s)):
        if so_dem+k>len(s):
            break
        else:
            chuoi_duoc_cat=s[so_dem:so_dem+k]
            chu_nguyen_am_dem_duoc=chu_nguyen_am_dem_duoc+chuoi_duoc_cat.count("a")
            chu_nguyen_am_dem_duoc=chu_nguyen_am_dem_duoc+chuoi_duoc_cat.count("i")
            chu_nguyen_am_dem_duoc=chu_nguyen_am_dem_duoc+chuoi_duoc_cat.count("e")
            chu_nguyen_am_dem_duoc=chu_nguyen_am_dem_duoc+chuoi_duoc_cat.count("o")
            chu_nguyen_am_dem_duoc=chu_nguyen_am_dem_duoc+chuoi_duoc_cat.count("u")
            
            thong_tin_chuoi[chuoi_duoc_cat]=chu_nguyen_am_dem_duoc
            chu_nguyen_am_dem_duoc=0
    for key,valua in thong_tin_chuoi.items():
        if valua>sotrum:
            trum=key
    return trum
    
    

            
        




s = input()

k = int(input().strip())

result = findSubstring(s, k)

print(result)

