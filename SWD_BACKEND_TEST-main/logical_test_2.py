
"""
Convert Arabic Number to Roman Number.
เขียนโปรแกรมรับค่าจาก user เพื่อแปลง input ของ user ที่เป็นตัวเลขอราบิก เป็นตัวเลขโรมัน
โดยที่ค่าที่รับต้องมีค่ามากกว่า 0 จนถึง 1000

*** อนุญาตให้ใช้แค่ตัวแปรพื้นฐาน, built-in methods ของตัวแปรและ function พื้นฐานของ Python เท่านั้น
ห้ามใช้ Library อื่น ๆ ที่ต้อง import ในการทำงาน(ยกเว้น ใช้เพื่อการ test การทำงานของฟังก์ชัน).

"""

num_map = [(1000,'M'), (900, 'CM'), (500, 'D'), (400, 'CD'), (100, 'C'), 
           (90, 'XC'), (50, 'L'), (40, 'XL'), (10, 'X'), 
           (9, 'IX'), (5, 'V'), (4, 'IV'),(1, 'I')]

def NumRoman(num):
    roman = ''
    while num > 0:
        for i, r in num_map:
            while num >=i:
                roman = roman+r
                num = num - i
    return roman

number = int(input('input your Arabic Number for convert to Roman Number: '))
if number >=0 and number <= 1000:
    print('Roman Number is ',NumRoman(number))
else:
    print(number,'Not between 0-1000')
