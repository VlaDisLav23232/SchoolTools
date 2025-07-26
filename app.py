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



st.sidebar.title("🎓 Навігація")
page = st.sidebar.radio(
    "Оберіть розділ:",
    ["🏠 Титульна сторінка", "🧮 Калькулятор", "🔁 Конвертер", "📉 Побудова графіка", "📅 Календар ДЗ", "➗ НСД, НСК та СА", "📚 Таблиця сталих", "🤫 Секрет"]
)

# --- 1. ТИТУЛЬНА СТОРІНКА ---
if page == "🏠 Титульна сторінка":
    st.title("🎓 Шкільний помічник")
    st.markdown("---")
    
    st.markdown("""
    ## 👋 Ласкаво просимо!
    
    **Шкільний помічник** — це універсальний інструмент для учнів, який допоможе вам у навчанні. 
    Наш застосунок об'єднує найнеобхідніші інструменти в одному місці.
    
    ### 🚀 Основні можливості:
    """)
    
    # Список функцій з іконками
    features = [
        ("🧮", "**Калькулятор**", "Швидкі математичні обчислення"),
        ("🔁", "**Конвертер величин**", "Переведення одиниць маси, часу та префіксів"),
        ("📉", "**Побудова графіків**", "Візуалізація математичних функцій"),
        ("📅", "**Календар завдань**", "Організація домашніх завдань"),
        ("➗", "**Математичні операції**", "НСД, НСК та середнє арифметичне"),
        ("📚", "**Довідник сталих**", "Фізичні та математичні константи")
    ]
    
    for icon, title, description in features:
        st.markdown(f"{icon} {title} — {description}")


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

# --- 5. НСД, НСК та СА ---
elif page == "➗ НСД, НСК та СА":
    st.header("➗ НСД, НСК та Середнє арифметичне")
    conversion_type = st.selectbox("Що хочеш знайти?", ["НСД", "НСК", "Середнє арифметичне"])
    if conversion_type=="НСД":
        if "nsd_values" not in st.session_state:
            st.session_state.nsd_values = [1.0, 1.0]

        st.subheader("Введіть числа для НСД:")

        for i, val in enumerate(st.session_state.nsd_values):
            st.session_state.nsd_values[i] = st.number_input(
                f"Число {i+1}:",
                value=val,
                min_value=1.0,
                step=1.0,
                key=f"nsd_input_{i}"
            )

        col1, col2 = st.columns(2)
        with col1:
            if st.button("➕ Додати число"):
                st.session_state.nsd_values.append(1.0)
                st.rerun()

        with col2:
            if len(st.session_state.nsd_values) > 2:
                if st.button("➖ Видалити останнє"):
                    st.session_state.nsd_values.pop()
                    st.rerun()

        if st.button("Обчислити НСД"):
            def gcd_multiple(numbers):
                """
                Обчислює НСД для списку чисел
                """
                resulter = int(numbers[0])
                for l in range(1, len(numbers)):
                    resulter = math.gcd(resulter, int(numbers[l]))
                return resulter

            try:
                result = gcd_multiple(st.session_state.nsd_values)
                st.success(f"НСД чисел {[int(x) for x in st.session_state.nsd_values]} = {result}")
            except Exception as e:
                st.error(f"Помилка обчислення. Перевірте введені значення. {e}")

    elif conversion_type=="НСК":
        if "lcm_values" not in st.session_state:
            st.session_state.lcm_values = [1.0, 1.0]

        st.subheader("Введіть числа для НСК:")

        for i, val in enumerate(st.session_state.lcm_values):
            st.session_state.lcm_values[i] = st.number_input(
                f"Число {i+1}:",
                value=val,
                min_value=1.0,
                step=1.0,
                key=f"lcm_input_{i}"
            )

        col1, col2 = st.columns(2)
        with col1:
            if st.button("➕ Додати число"):
                st.session_state.lcm_values.append(1.0)
                st.rerun()

        with col2:
            if len(st.session_state.lcm_values) > 2:
                if st.button("➖ Видалити останнє"):
                    st.session_state.lcm_values.pop()
                    st.rerun()

        if st.button("Обчислити НСК"):
            def lcm_multiple(numbers):
                """
                Обчислює НСК для списку чисел
                """
                resulter = int(numbers[0])
                for l in range(1, len(numbers)):
                    resulter = math.lcm(resulter, int(numbers[l]))
                return resulter

            try:
                result = lcm_multiple(st.session_state.lcm_values)
                st.success(f"НСК чисел {[int(x) for x in st.session_state.lcm_values]} = {result}")
            except Exception as e:
                st.error(f"Помилка обчислення. Перевірте введені значення. {e}")
    elif conversion_type=="Середнє арифметичне":
        if "average_values" not in st.session_state:
            st.session_state.average_values = [1.0, 1.0]

        st.subheader("Введіть числа для середнього арифметичного:")

        # Відображаємо всі поля введення
        for i, val in enumerate(st.session_state.average_values):
            st.session_state.average_values[i] = st.number_input(
                f"Число {i+1}:",
                value=val,
                min_value=1.0,
                step=1.0,
                key=f"average_input_{i}"
            )

        col1, col2 = st.columns(2)
        with col1:
            if st.button("➕ Додати число"):
                st.session_state.average_values.append(1.0)
                st.rerun()

        with col2:
            if len(st.session_state.average_values) > 2:
                if st.button("➖ Видалити останнє"):
                    st.session_state.average_values.pop()
                    st.rerun()

        if st.button("Обчислити середнє арифметичне"):
            def average_multiple(numbers):
                """
                Обчислює середнє арифметичне для списку чисел
                """
                return sum(numbers) / len(numbers)

            try:
                result = average_multiple(st.session_state.average_values)
                st.success(f"Середнє арифметичне чисел {[int(x) for x in st.session_state.average_values]} = {result}")
            except Exception as e:
                st.error(f"Помилка обчислення. Перевірте введені значення. {e}")

elif page == "📚 Таблиця сталих":
    st.title("📚 Фізичні та математичні сталі")

    constants_data = [
        {"Назва": "Швидкість світла у вакуумі", "Позначення": "c", "Значення": "299 792 458", "Одиниці": "м/с"},
        {"Назва": "Гравітаційна стала", "Позначення": "G", "Значення": "6.67430 × 10⁻¹¹", "Одиниці": "м³/кг·с²"},
        {"Назва": "Заряд електрона", "Позначення": "e", "Значення": "1.602176634 × 10⁻¹⁹", "Одиниці": "Кл"},
        {"Назва": "Постійна Планка", "Позначення": "h", "Значення": "6.62607015 × 10⁻³⁴", "Одиниці": "Дж·с"},
        {"Назва": "Маса електрона", "Позначення": "me", "Значення": "9.10938356 × 10⁻³¹", "Одиниці": "кг"},
        {"Назва": "Маса протона", "Позначення": "mp", "Значення": "1.6726219 × 10⁻²⁷", "Одиниці": "кг"},
        {"Назва": "Постійна Авогадро", "Позначення": "NA", "Значення": "6.02214076 × 10²³", "Одиниці": "1/моль"},
        {"Назва": "Газова стала", "Позначення": "R", "Значення": "8.314", "Одиниці": "Дж/моль·К"},
        {"Назва": "Пі (відношення кола до діаметра)", "Позначення": "π", "Значення": "3.1415926535", "Одиниці": "—"},
        {"Назва": "Ейлерова стала", "Позначення": "e", "Значення": "2.7182818284", "Одиниці": "—"},
    ]

    st.dataframe(constants_data, use_container_width=True)

# --- 6. СЕКРЕТНА СТОРІНКА ---
elif page == "🤫 Секрет":
    st.title("🤫 Секретна Сторінка")

    st.markdown("""Ти знайшов секретну сторінку! Ось щось особливе для тебе:
    """)

    # Video placeholder
    st.video("https://www.youtube.com/watch?v=dQw4w9WgXcQ")

    st.markdown("""Тримай цю сторінку в секреті від інших...""")

    st.balloons()
# --- 6. СЕКРЕТНА СТОРІНКА ---
elif page == "🤫 Секрет":
    st.title("🤫 Секретна Сторінка")

    st.markdown("""Ти знайшов секретну сторінку! Ось щось особливе для тебе:
    """)

    # Video placeholder
    st.video("https://www.youtube.com/watch?v=dQw4w9WgXcQ")

    st.markdown("""Тримай цю сторінку в секреті від інших...""")

    st.balloons()
