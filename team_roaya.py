
import json
import os

FILE = "team_roaya_tasks.json"

print("❤️ أهلاً بيكي في تيم رؤية ❤️")

name = input("اكتبي اسمك: ")
print("أهلاً يا", name, "في فريق رؤية ❤️")

# تحميل المهام المحفوظة
if os.path.exists(FILE):
    try:
        with open(FILE, "r", encoding="utf-8") as f:
            tasks = json.load(f)
    except (json.JSONDecodeError, OSError):
        tasks = []
else:
    tasks = [
        "تاسك البرمجيات",
        "الأجهزة التعليمية"
    ]

def save_tasks():
    with open(FILE, "w", encoding="utf-8") as f:
        json.dump(tasks, f, ensure_ascii=False, indent=4)

while True:
    print("\n❤️ قائمة تيم رؤية ❤️")
    print("1 - عرض مهام الفريق")
    print("2 - إضافة مهمة جديدة")
    print("3 - حذف مهمة")
    print("4 - الخروج")

    choice = input("اختاري رقم: ")

    if choice == "1":
        print("\n📚 مهام الفريق:")
        if not tasks:
            print("لا توجد مهام حالياً")
        else:
            for i, task in enumerate(tasks, 1):
                print(i, "-", task)

    elif choice == "2":
        task = input("اكتبي المهمة الجديدة: ").strip()
        if task:
            tasks.append(task)
            save_tasks()
            print("✅ تم إضافة المهمة بنجاح")
        else:
            print("اكتبي اسم المهمة أولاً")

    elif choice == "3":
        for i, task in enumerate(tasks, 1):
            print(i, "-", task)

        try:
            number = int(input("رقم المهمة للحذف: "))
            if 1 <= number <= len(tasks):
                removed = tasks.pop(number - 1)
                save_tasks()
                print("تم حذف:", removed)
            else:
                print("رقم غير صحيح")
        except ValueError:
            print("اكتبي رقم صحيح")

    elif choice == "4":
        save_tasks()
        print("مع السلامة يا", name, "❤️")
        break

    else:
        print("اختيار غير صحيح، حاولي تاني")
