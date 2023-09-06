x = int(input('whats the number'))
Roman: str = ""
liRoman = [[1000, "M"], [900, "CM"], [500, "D"], [400, "CD"], [100, "C"], [90, "XC"], [50, "l"], [40, 'XL'], [10, "X"], [9, "IX"],
           [5, "V"], [4, "IV"], [1, "I"]]

for i in range(len(liRoman)):
    while x >= liRoman[i][0]:
        Roman += liRoman[i][1]
        x -= liRoman[i][0]


for i in range(Roman)
    for




print("Roman number:", Roman)
