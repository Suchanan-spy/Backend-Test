
"""
Convert Number to Thai Text.
เขียนโปรแกรมรับค่าจาก user เพื่อแปลง input ของ user ที่เป็นตัวเลข เป็นตัวหนังสือภาษาไทย
โดยที่ค่าที่รับต้องมีค่ามากกว่าหรือเท่ากับ 0 และน้อยกว่า 10 ล้าน

*** อนุญาตให้ใช้แค่ตัวแปรพื้นฐาน, built-in methods ของตัวแปรและ function พื้นฐานของ Python เท่านั้น
ห้ามใช้ Library อื่น ๆ ที่ต้อง import ในการทำงาน(ยกเว้น ใช้เพื่อการ test การทำงานของฟังก์ชัน).

"""
from decimal import Decimal

class NumThai:

    def __init__(self):

        self.number = None
        self.num_text = {
                        0  : "ศูนย์",
                        1  : "หนึ่ง",
                        2  : "สอง",
                        3  : "สาม",
                        4  : "สี่",
                        5  : "ห้า",
                        6  : "หก",
                        7  : "เจ็ด",
                        8  : "แปด",
                        9  : "เก้า",
                        "0" : "",
                        "1" : "สิบ",
                        "2" : "ร้อย",
                        "3" : "พัน",
                        "4" : "หมื่น",
                        "5" : "แสน",
                        "6" : "ล้าน"
                    }

    def process_int(self):
        result = []
        le = len(str(self.number))
        val = self.num_text['6']
        i=0
        
        for x in range(0,le):
            n = int(self.number%10)
            self.number /=10

            if le >1:
                if x >=1 and x%6==0:
                    if n==1 and le<8:
                        result.append(self.num_text[n]+val)
                    elif n==1 and le>7:
                        result.append("เอ็ด"+val)
                    else:
                        if n !=0:
                            result.append(self.num_text[n]+val)
                        else:
                            result.append(val)

                elif x==0 and n==1:
                    result.append("เอ็ด")
                else:
                    if i==1 and n==1:
                        result.append(self.num_text[str(i)])
                    elif i==1 and n==2:
                        result.append("ยี่"+self.num_text[str(i)])
                    elif n==0:
                        pass
                    else:
                        result.append(self.num_text[n]+self.num_text[str(i)])         
            else:
                result.append(self.num_text[n])
    
            if i>5:
                val+=val
                i=0
            i+=1
        
        return list(reversed(result))
    
from num_thai.thainumbers import NumThai

num = NumThai()
number = int(input('input your Number for convert to Thai Text: '))
if number >=0 and number <= 10000000:
    text = num.NumberToTextThai(number)
    print("Thai Text is ",text)
else:
    print(number,'Not between 0-10000000 ')

