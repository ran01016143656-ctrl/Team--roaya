import streamlit as st
import json
import os

st.set_page_config(
    page_title="تيم رؤية",
    page_icon="❤️",
    layout="centered"
)

FILE = "team_roaya_tasks.json"

def load_tasks():
    if os.path.exists(FILE):
        try:
            with open(FILE, "r", encoding="utf-8") as f:
                return json.load(f)
        except (OSError, ValueError):
            pass
    return [
        {"name": "تاسك البرمجيات", "done": False},
        {"name": "الأجهزة التعليمية", "done": False},
        {"name": "تجهيز العروض التقديمية", "done": False}
    ]

def save_tasks():
    with open(FILE, "w", encoding="utf-8") as f:
        json.dump(
            st.session_state.tasks,
            f,
            ensure_ascii=False,
            indent=2
        )

if "tasks" not in st.session_state:
    st.session_state.tasks = load_tasks()

st.title("❤️ تيم رؤية ❤️")
st.subheader("مع بعض ننجز تكليفاتنا الجامعية 🎓")

name = st.text_input("👩 اكتبي اسمك")
if name:
    st.success(f"أهلاً يا {name} في فريق رؤية ❤️")

st.divider()
st.header("📚 مهام الفريق")

new_task = st.text_input("اكتبي مهمة جديدة")

if st.button("➕ إضافة المهمة"):
    if new_task.strip():
        st.session_state.tasks.append({
            "name": new_task.strip(),
            "done": False
        })
        save_tasks()
        st.rerun()
    else:
        st.warning("اكتبي اسم المهمة الأول")

if not st.session_state.tasks:
    st.info("لا توجد مهام حالياً")

for i, task in enumerate(st.session_state.tasks):
    col1, col2 = st.columns([4, 1])

    with col1:
        done = st.checkbox(
            task["name"],
            value=task["done"],
            key=f"task_{i}"
        )
        if done != task["done"]:
            task["done"] = done
            save_tasks()
            st.rerun()

    with col2:
        if st.button("🗑️", key=f"delete_{i}"):
            st.session_state.tasks.pop(i)
            save_tasks()
            st.rerun()

st.divider()

total = len(st.session_state.tasks)
completed = sum(
    task["done"] for task in st.session_state.tasks
)

st.write(f"📌 إجمالي المهام: {total}")
st.write(f"✅ المهام المكتملة: {completed}")

if total:
    st.progress(completed / total)

st.caption("صُنع بحب لفريق رؤية ❤️")
  
