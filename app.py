import streamlit as st
import matplotlib.pyplot as plt

import numpy as np
import math
import datetime


st.set_page_config(
    page_title="Шкільний помічник",
    page_icon="🎓",
    layout="centered"
)

page_bg_img = """
<style>
[data-testid="stAppViewContainer"] > div:first-child {
    background-image: url("https://i.imgur.com/BJc5ZJ3.jpg");
    background-size: cover;
    background-position: center;
    background-repeat: no-repeat;
    background-attachment: fixed;
}
</style>
"""

st.markdown(page_bg_img, unsafe_allow_html=True)


st.sidebar.title("🎓 Навігація")
page = st.sidebar.radio(
    "Оберіть розділ:",
    ["🏠 Титульна сторінка", "🧮 Калькулятор", "🔁 Конвертер", "📉 Побудова графіка", "📅 Календар ДЗ"]
)

# --- 1. ТИТУЛЬНА СТОРІНКА ---
if page == "🏠 Титульна сторінка":
    st.title("🎓 Шкільний помічник")
    st.subheader("Твій помічник у світі знань")
    st.markdown("""
    👋 Ласкаво просимо до **Шкільного помічника** — застосунку, який допоможе швидко та зручно:

    - 🔁 Конвертувати одиниці маси, часу, префіксів
    - 🧮 Обчислювати звичайні приклади
    - 📅 У майбутньому — переглядати календар подій
    
    Оберіть розділ у бічній панелі, щоб почати.
    """)

    st.markdown("### 🆕 Що нового:")
    st.success("✅ Додано - 📅 Календар ДЗ")
    st.warning("⚠️ Незабаром — генерація тестів на основі завдань")

# --- 2. КАЛЬКУЛЯТОР ---
elif page == "🧮 Калькулятор":
    st.header("🧮 Простий калькулятор")

    num1 = st.number_input("Перше число", value=0.0)
    operation = st.selectbox("Операція", ["Додавання", "Віднімання", "Множення", "Ділення"])
    num2 = st.number_input("Друге число", value=0.0)

    result = None
    if operation == "Додавання":
        result = num1 + num2
    elif operation == "Віднімання":
        result = num1 - num2
    elif operation == "Множення":
        result = num1 * num2
    elif operation == "Ділення":
        if num2 != 0:
            result = num1 / num2
        else:
            st.error("❌ Ділення на нуль неможливе!")

    if result is not None:
        st.success(f"Результат: {result}")

# --- 3. КОНВЕРТЕР ---
elif page == "🔁 Конвертер":
    st.header("🔁 Конвертація величин")
    conversion_type = st.selectbox("Що хочеш конвертувати?", ["Маса", "Час", "Префікси"])

    if conversion_type == "Маса":
        mass_units = {"г": 1, "кг": 1000, "т": 1000000}
        value = st.number_input("Введіть значення:", min_value=0.0)
        from_unit = st.selectbox("Звідки:", mass_units.keys(), key="mass_from")
        to_unit = st.selectbox("Куди:", mass_units.keys(), key="mass_to")
        result = value * mass_units[from_unit] / mass_units[to_unit]
        st.success(f"{value} {from_unit} = {result} {to_unit}")

    elif conversion_type == "Час":
        time_units = {"с": 1, "хв": 60, "год": 3600}
        value = st.number_input("Введіть час:", min_value=0.0)
        from_unit = st.selectbox("Звідки:", time_units.keys(), key="time_from")
        to_unit = st.selectbox("Куди:", time_units.keys(), key="time_to")
        result = value * time_units[from_unit] / time_units[to_unit]
        st.success(f"{value} {from_unit} = {result} {to_unit}")

    elif conversion_type == "Префікси":
        prefixes = {
            "Тера (Т)": 1e12,
            "Гіга (Г)": 1e9,
            "Мега (М)": 1e6,
            "Кіло (к)": 1e3,
            "Одиниця": 1,
            "мілі (м)": 1e-3,
            "мікро (мк)": 1e-6,
            "нано (н)": 1e-9,
        }
        value = st.number_input("Введіть значення:", min_value=0.0)
        from_prefix = st.selectbox("Звідки:", prefixes.keys(), key="prefix_from")
        to_prefix = st.selectbox("Куди:", prefixes.keys(), key="prefix_to")
        result = value * prefixes[from_prefix] / prefixes[to_prefix]
        st.success(f"{value} {from_prefix} = {result} {to_prefix}")

# --- 4. ГРАФІК ФУНКЦІЇ ---
elif page == "📉 Побудова графіка":
    st.header("📉 Побудова математичної функції")

    st.markdown("""
    ✍️ Введи функцію, яку хочеш побудувати. Наприклад: `x**2`, `sin(x) + x`, `exp(-x**2)`
    """)

    func_input = st.text_input("Функція f(x):", "sin(x)")
    x_min = st.number_input("Мінімальне значення x", value=-10.0)
    x_max = st.number_input("Максимальне значення x", value=10.0)

    x = np.linspace(x_min, x_max, 500)

    try:
        y = [eval(func_input, {
            "x": val,
            "sin": math.sin,
            "cos": math.cos,
            "tan": math.tan,
            "exp": math.exp,
            "log": math.log,
            "sqrt": math.sqrt,
            "__builtins__": {}
        }) for val in x]

        fig, ax = plt.subplots()
        ax.plot(x, y, label=f"f(x) = {func_input}", color="blue")
        ax.set_xlabel("x")
        ax.set_ylabel("f(x)")
        ax.set_title("Графік функції")
        ax.grid(True)
        ax.legend()
        st.pyplot(fig)

    except Exception as e:
        st.error(f"❌ Помилка у формулі: {e}")


# 📅 КАЛЕНДАР З ДЗ
if "calendar_hw" not in st.session_state:
    st.session_state.calendar_hw = []
elif page == "📅 Календар ДЗ":
    st.title("📅 Календар домашніх завдань")

    # Додавання нового ДЗ
    st.subheader("➕ Додати ДЗ до календаря")
    with st.form("add_hw_calendar_form"):
        subject = st.text_input("Предмет")
        hw_date = st.date_input("Дата виконання", min_value=datetime.date.today())
        description = st.text_area("Опис домашнього завдання")
        submitted = st.form_submit_button("Додати")

        if submitted and subject:
            st.session_state.calendar_hw.append({
                "Предмет": subject,
                "Дата": hw_date,
                "Опис": description,
                "✅ Виконано": False
            })
            st.success("✅ ДЗ додано!")

    # Перегляд ДЗ у календарі
    st.subheader("📖 Завдання за датами")
    if st.session_state.calendar_hw:
        selected_date = st.date_input("Оберіть дату для перегляду")
        filtered = [task for task in st.session_state.calendar_hw if task["Дата"] == selected_date]

        if filtered:
            for i, task in enumerate(filtered):
                cols = st.columns([3, 4, 2, 1])
                cols[0].markdown(f"**{task['Предмет']}**")
                cols[1].markdown(task["Опис"])
                done = cols[2].checkbox("Готово", value=task["✅ Виконано"], key=f"cal_done_{i}")
                if cols[3].button("❌", key=f"del_{i}"):
                    st.session_state.calendar_hw.remove(task)
                    st.rerun()
                task["✅ Виконано"] = done
        else:
            st.info("Немає ДЗ на цю дату.")
    else:
        st.info("Поки нічого не додано.")