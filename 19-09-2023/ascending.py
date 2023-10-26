d={1:2,3:4,4:3,2:1,0:0,3:5}
print("Original dictionary",d)
sorted_d=sorted(d.items())
print("Dictionary in ascending order:",sorted_d)
sorted_d_reverse=sorted(d.items(),reverse=True)
print("Dictionary in descending order:",sorted_d_reverse)
