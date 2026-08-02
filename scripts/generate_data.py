from faker import Faker
import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import random
import os

# Создаем папки для данных
os.makedirs("data/raw", exist_ok=True)
os.makedirs("data/analytics", exist_ok=True)

print(" ГЕНЕРАЦИЯ ДАННЫХ ДЛЯ RETAIL FINANCIAL ANALYTICS")
print("="*60)

# Инициализируем генератор
fake = Faker("ru_RU")
np.random.seed(42)
random.seed(42)

# ============= 1. КАТЕГОРИИ =============
print("\n1️ Генерация категорий...")
categories = pd.DataFrame({
    'category_id': range(1, 11),
    'category_name': [
        'Смартфоны', 'Ноутбуки', 'Планшеты', 'Телевизоры', 
        'Аудиотехника', 'Игровые консоли', 'Бытовая техника',
        'Кофеварки', 'Умные часы', 'Периферия'
    ]
})
print(f"    Создано {len(categories)} категорий")

# ============= 2. ТОВАРЫ =============
print("\n2️ Генерация товаров...")

products_data = {
    1: ['iPhone 15 Pro', 70000, 99990],
    2: ['iPhone 15', 60000, 84990],
    3: ['Samsung Galaxy S24', 65000, 89990],
    4: ['Samsung Galaxy S23', 50000, 74990],
    5: ['Xiaomi 14 Pro', 45000, 69990],
    6: ['Xiaomi 13T', 35000, 54990],
    7: ['Google Pixel 8', 55000, 79990],
    8: ['Honor 90', 30000, 49990],
    9: ['MacBook Pro 16', 140000, 199990],
    10: ['MacBook Air 15', 110000, 159990],
    11: ['Dell XPS 15', 120000, 169990],
    12: ['Lenovo ThinkPad X1', 115000, 164990],
    13: ['ASUS ROG Zephyrus', 125000, 179990],
    14: ['HP Spectre x360', 95000, 139990],
    15: ['iPad Pro 12.9', 65000, 89990],
    16: ['iPad Air', 50000, 69990],
    17: ['Samsung Tab S9', 55000, 79990],
    18: ['Lenovo Tab P12', 35000, 49990],
    19: ['Xiaomi Pad 6', 30000, 44990],
    20: ['Samsung QLED 65"', 90000, 129990],
    21: ['LG OLED 55"', 85000, 119990],
    22: ['Sony Bravia 48"', 70000, 99990],
    23: ['TCL 4K 50"', 40000, 59990],
    24: ['Hisense 43"', 30000, 44990],
    25: ['Sony WH-1000XM5', 18000, 29990],
    26: ['AirPods Pro 2', 15000, 24990],
    27: ['Bose QC45', 16000, 27990],
    28: ['JBL Tune 770NC', 10000, 19990],
    29: ['Samsung Galaxy Buds', 8000, 14990],
    30: ['PlayStation 5', 35000, 49990],
    31: ['Xbox Series X', 35000, 49990],
    32: ['Nintendo Switch', 20000, 29990],
    33: ['Steam Deck', 30000, 39990],
    34: ['Dyson V15 Vacuum', 45000, 59990],
    35: ['iRobot Roomba j7', 50000, 69990],
    36: ['Xiaomi Robot Vacuum', 25000, 39990],
    37: ['Kärcher VC7', 18000, 29990],
    38: ['De\'Longhi Espresso', 35000, 49990],
    39: ['Philips LatteGo', 40000, 59990],
    40: ['Nespresso Vertuo', 15000, 19990],
    41: ['Moccamaster', 25000, 39990],
    42: ['Apple Watch Ultra 2', 30000, 49990],
    43: ['Apple Watch Series 9', 20000, 34990],
    44: ['Samsung Watch 6', 18000, 29990],
    45: ['Garmin Fenix 7', 28000, 39990],
    46: ['Logitech MX Master', 8000, 12990],
    47: ['Razer DeathAdder', 6000, 9990],
    48: ['Corsair K70', 10000, 14990],
    49: ['Keychron Q1', 7000, 9990],
    50: ['Samsung 4K Monitor', 30000, 49990]
}

products = []
for product_id, (name, purchase, sale) in products_data.items():
    # Распределяем по категориям
    if product_id <= 8: 
        category_id = 1  # Смартфоны
    elif product_id <= 14: 
        category_id = 2  # Ноутбуки
    elif product_id <= 19: 
        category_id = 3  # Планшеты
    elif product_id <= 24: 
        category_id = 4  # Телевизоры
    elif product_id <= 29: 
        category_id = 5  # Аудиотехника
    elif product_id <= 33: 
        category_id = 6  # Игровые консоли
    elif product_id <= 37: 
        category_id = 7  # Бытовая техника
    elif product_id <= 41: 
        category_id = 8  # Кофеварки
    elif product_id <= 45: 
        category_id = 9  # Умные часы
    else: 
        category_id = 10  # Периферия
    
    products.append({
        'product_id': product_id,
        'product_name': name,
        'category_id': category_id,
        'purchase_price': purchase,
        'sale_price': sale
    })

products_df = pd.DataFrame(products)
print(f"    Создано {len(products_df)} товаров")

# ============= 3. МАГАЗИНЫ =============
print("\n3️ Генерация магазинов...")
stores = pd.DataFrame({
    'store_id': range(1, 16),
    'store_name': [
        'TechStore Московский', 'TechStore Невский', 'TechStore Казанский',
        'TechStore Екатеринбург', 'TechStore Новосибирск', 'TechStore Краснодар',
        'TechStore Нижний', 'TechStore Челябинск', 'TechStore Уфа',
        'TechStore Ростов', 'TechStore Волгоград', 'TechStore Красноярск',
        'TechStore Пермь', 'TechStore Воронеж', 'TechStore Саратов'
    ],
    'city': [
        'Москва', 'Санкт-Петербург', 'Казань', 'Екатеринбург',
        'Новосибирск', 'Краснодар', 'Нижний Новгород', 'Челябинск',
        'Уфа', 'Ростов-на-Дону', 'Волгоград', 'Красноярск',
        'Пермь', 'Воронеж', 'Саратов'
    ]
})
print(f"    Создано {len(stores)} магазинов")

# ============= 4. КЛИЕНТЫ =============
print("\n4️ Генерация клиентов...")

# Распределение клиентов по городам
city_distribution = {
    'Москва': 0.20, 'Санкт-Петербург': 0.15, 'Казань': 0.08,
    'Екатеринбург': 0.08, 'Новосибирск': 0.07, 'Краснодар': 0.06,
    'Нижний Новгород': 0.06, 'Челябинск': 0.05, 'Уфа': 0.05,
    'Ростов-на-Дону': 0.05, 'Волгоград': 0.04, 'Красноярск': 0.04,
    'Пермь': 0.03, 'Воронеж': 0.02, 'Саратов': 0.02
}

cities = list(city_distribution.keys())
city_weights = list(city_distribution.values())

customers = []
for customer_id in range(1, 3001):
    city = np.random.choice(cities, p=city_weights)
    registration_date = fake.date_between(start_date='-3y', end_date='2025-12-31')
    
    customers.append({
        'customer_id': customer_id,
        'first_name': fake.first_name(),
        'last_name': fake.last_name(),
        'city': city,
        'registration_date': registration_date
    })

customers_df = pd.DataFrame(customers)
print(f"    Создано {len(customers_df)} клиентов")

# ============= 5. ЗАКАЗЫ =============
print("\n5️⃣ Генерация заказов...")

# Сезонные коэффициенты
seasonal_factors = {
    1: 0.7, 2: 0.6, 3: 0.8, 4: 0.9, 5: 1.0,
    6: 1.1, 7: 1.0, 8: 1.0, 9: 1.1, 10: 1.2,
    11: 1.5, 12: 1.8
}

orders = []
for order_id in range(1, 10001):
    # Выбираем месяц с учетом сезонности
    month = np.random.choice(range(1, 13), p=[seasonal_factors[m]/sum(seasonal_factors.values()) 
                                              for m in range(1, 13)])
    day = np.random.randint(1, 29)
    order_date = datetime(2025, month, day)
    
    # Выбираем клиента и магазин
    customer_id = np.random.randint(1, 3001)
    customer_city = customers_df[customers_df['customer_id'] == customer_id]['city'].iloc[0]
    
    # 70% заказов - в городе клиента
    if np.random.random() < 0.7:
        available_stores = stores[stores['city'] == customer_city]['store_id'].tolist()
        store_id = np.random.choice(available_stores) if available_stores else np.random.randint(1, 16)
    else:
        store_id = np.random.randint(1, 16)
    
    orders.append({
        'order_id': order_id,
        'customer_id': customer_id,
        'store_id': store_id,
        'order_date': order_date
    })

orders_df = pd.DataFrame(orders)
print(f"    Создано {len(orders_df)} заказов")

# ============= 6. ТОВАРЫ В ЗАКАЗАХ =============
print("\n6️⃣ Генерация товаров в заказах...")

order_items_list = []
item_id = 1

for order_id in range(1, 10001):
    # Количество товаров в заказе зависит от месяца
    order_month = orders_df[orders_df['order_id'] == order_id]['order_date'].iloc[0].month
    if order_month in [12, 6, 11]:
        num_items = np.random.choice([1, 2, 3, 4, 5, 6], p=[0.05, 0.15, 0.2, 0.25, 0.2, 0.15])
    else:
        num_items = np.random.choice([1, 2, 3, 4, 5], p=[0.1, 0.2, 0.3, 0.25, 0.15])
    
    product_ids = np.random.choice(products_df['product_id'], size=num_items, replace=False)
    
    for product_id in product_ids:
        quantity = np.random.choice([1, 2, 3], p=[0.6, 0.3, 0.1])
        order_items_list.append({
            'item_id': item_id,
            'order_id': order_id,
            'product_id': product_id,
            'quantity': quantity
        })
        item_id += 1

order_items_df = pd.DataFrame(order_items_list)
print(f"    Создано {len(order_items_df)} позиций")

# ============= 7. РАСЧЕТ ФИНАНСОВ =============
print("\n7️⃣ Расчет финансовых показателей...")

# Обогащаем данные ценами
order_items_enriched = order_items_df.merge(
    products_df[['product_id', 'sale_price', 'purchase_price']], 
    on='product_id'
)

# Рассчитываем суммы
order_items_enriched['total_sale'] = order_items_enriched['quantity'] * order_items_enriched['sale_price']
order_items_enriched['total_purchase'] = order_items_enriched['quantity'] * order_items_enriched['purchase_price']
order_items_enriched['profit'] = order_items_enriched['total_sale'] - order_items_enriched['total_purchase']

# Агрегируем по заказам
order_summary = order_items_enriched.groupby('order_id').agg({
    'total_sale': 'sum',
    'total_purchase': 'sum',
    'profit': 'sum'
}).reset_index()

# Добавляем в заказы
orders_df = orders_df.merge(order_summary, on='order_id', how='left')
orders_df['total_sale'] = orders_df['total_sale'].fillna(0)
orders_df['total_purchase'] = orders_df['total_purchase'].fillna(0)
orders_df['profit'] = orders_df['profit'].fillna(0)

# Добавляем статусы
def get_order_status(order_date):
    days_ago = (datetime.now() - order_date).days
    if days_ago > 30:
        return np.random.choice(['Completed', 'Completed', 'Completed', 'Cancelled'], 
                               p=[0.8, 0.15, 0.04, 0.01])
    elif days_ago > 7:
        return np.random.choice(['Completed', 'Shipped', 'Processing'], p=[0.7, 0.2, 0.1])
    else:
        return np.random.choice(['Processing', 'Shipped', 'Pending'], p=[0.4, 0.3, 0.3])

orders_df['status'] = orders_df['order_date'].apply(get_order_status)

# ============= 8. СОХРАНЕНИЕ =============
print("\n8️ Сохранение данных...")

customers_df.to_csv("data/raw/customers.csv", index=False, encoding='utf-8-sig')
categories.to_csv("data/raw/categories.csv", index=False, encoding='utf-8-sig')
products_df.to_csv("data/raw/products.csv", index=False, encoding='utf-8-sig')
stores.to_csv("data/raw/stores.csv", index=False, encoding='utf-8-sig')
orders_df.to_csv("data/raw/orders.csv", index=False, encoding='utf-8-sig')
order_items_df.to_csv("data/raw/order_items.csv", index=False, encoding='utf-8-sig')

print("    Все файлы сохранены в data/raw/")

# ============= 9. АНАЛИТИКА =============
print("\n9️ Создание аналитических отчетов...")

# Ежемесячная статистика
monthly_stats = orders_df[orders_df['status'] == 'Completed'].groupby(
    pd.Grouper(key='order_date', freq='M')
).agg({
    'order_id': 'count',
    'total_sale': 'sum',
    'profit': 'sum',
    'customer_id': 'nunique'
}).reset_index()
monthly_stats.columns = ['month', 'orders', 'revenue', 'profit', 'customers']
monthly_stats['avg_check'] = monthly_stats['revenue'] / monthly_stats['orders']
monthly_stats['margin'] = (monthly_stats['profit'] / monthly_stats['revenue'] * 100).round(2)

# Статистика по магазинам
store_stats = orders_df[orders_df['status'] == 'Completed'].groupby('store_id').agg({
    'order_id': 'count',
    'total_sale': 'sum',
    'profit': 'sum'
}).reset_index()
store_stats.columns = ['store_id', 'orders', 'revenue', 'profit']
store_stats = store_stats.merge(stores, on='store_id')

# Сохраняем
monthly_stats.to_csv("data/analytics/monthly_kpi.csv", index=False, encoding='utf-8-sig')
store_stats.to_csv("data/analytics/store_performance.csv", index=False, encoding='utf-8-sig')

print("    Аналитические отчеты сохранены в data/analytics/")

# ============= 10. ИТОГИ =============
print("\n" + "="*60)
print(" ИТОГОВАЯ СТАТИСТИКА")
print("="*60)

completed = orders_df[orders_df['status'] == 'Completed']
total_revenue = completed['total_sale'].sum()
total_profit = completed['profit'].sum()
total_orders = len(completed)

print(f" Выручка: {total_revenue:,.0f} ₽")
print(f" Прибыль: {total_profit:,.0f} ₽")
print(f" Маржинальность: {(total_profit/total_revenue*100):.1f}%")
print(f" Заказов: {total_orders}")
print(f"  Средний чек: {total_revenue/total_orders:,.0f} ₽")
print(f"  Клиентов: {completed['customer_id'].nunique()}")
