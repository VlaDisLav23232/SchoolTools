import streamlit as st

st.set_page_config(
    page_title="Шкільний помічник",
    page_icon="🎓",
    layout="centered"
)

st.sidebar.title("🎓 Навігація")
page = st.sidebar.radio(
    "Оберіть розділ:",
    ["🏠 Титульна сторінка", "🧮 Калькулятор", "🔁 Конвертер"]
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
