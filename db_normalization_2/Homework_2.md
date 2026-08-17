# Домашнее задание №2. Проектирование базы данных для интернет-магазина

## Part 1: Выбор сценария

Для данной работы выбран сценарий: **Онлайн-магазин электроники**.  
Эта система будет управлять категориями товаров, товарами, покупателями и оформленными заказами.

---

## Part 2: Проектирование базы данных и документация

### Идентификация сущностей и атрибутов

1. Покупатели (Customers)  
2. Заказы (Orders)  
3. Товары (Products)  
4. Категории (Categories)  
5. Товары в заказе (Order_Items)  

---

### Проектирование таблиц

#### 1. Table Name: Customers
**Description:** Хранит информацию о покупателях.

**Attributes:**
- `customer_id` — INTEGER, PK, NOT NULL, UNIQUE
- `first_name` — VARCHAR(50), NOT NULL
- `last_name` — VARCHAR(50), NOT NULL
- `email` — VARCHAR(100), UNIQUE, NOT NULL
- `phone` — VARCHAR(20)
- `registration_date` — DATE, DEFAULT CURRENT_DATE

**Constraints:**
- `PK_Customers`: PRIMARY KEY (customer_id)
- `UQ_Email`: UNIQUE (email)

---

#### 2. Table Name: Orders
**Description:** Хранит информацию о заказах.

**Attributes:**
- `order_id` — INTEGER, PK, NOT NULL, UNIQUE
- `customer_id` — INTEGER, FK (REFERENCES Customers), NOT NULL
- `order_date` — DATE, DEFAULT CURRENT_DATE
- `order_status` — VARCHAR(20), NOT NULL

**Constraints:**
- `PK_Orders`: PRIMARY KEY (order_id)
- `FK_Orders_Customers`: FOREIGN KEY (customer_id) REFERENCES Customers(customer_id)
- `CHK_Status`: CHECK (order_status IN ('Новый', 'Оплачен', 'Отправлен', 'Доставлен'))

---

#### 3. Table Name: Products
**Description:** Хранит информацию о товарах.

**Attributes:**
- `product_id` — INTEGER, PK, NOT NULL, UNIQUE
- `product_name` — VARCHAR(100), NOT NULL
- `price` — DECIMAL(10,2), NOT NULL
- `category_id` — INTEGER, FK (REFERENCES Categories), NOT NULL

**Constraints:**
- `PK_Products`: PRIMARY KEY (product_id)
- `FK_Products_Categories`: FOREIGN KEY (category_id) REFERENCES Categories(category_id)
- `CHK_Price`: CHECK (price >= 0)

---

#### 4. Table Name: Categories
**Description:** Хранит информацию о категориях товаров.

**Attributes:**
- `category_id` — INTEGER, PK, NOT NULL, UNIQUE
- `category_name` — VARCHAR(50), NOT NULL, UNIQUE

**Constraints:**
- `PK_Categories`: PRIMARY KEY (category_id)
- `UQ_CategoryName`: UNIQUE (category_name)

---

#### 5. Table Name: Order_Items
**Description:** Хранит информацию о товарах в заказе (связующая таблица).

**Attributes:**
- `order_item_id` — INTEGER, PK, NOT NULL, UNIQUE
- `order_id` — INTEGER, FK (REFERENCES Orders), NOT NULL
- `product_id` — INTEGER, FK (REFERENCES Products), NOT NULL
- `quantity` — INTEGER, NOT NULL

**Constraints:**
- `PK_OrderItems`: PRIMARY KEY (order_item_id)
- `FK_OrderItems_Orders`: FOREIGN KEY (order_id) REFERENCES Orders(order_id)
- `FK_OrderItems_Products`: FOREIGN KEY (product_id) REFERENCES Products(product_id)
- `CHK_Quantity`: CHECK (quantity > 0)

---

### Связи между таблицами

- **Categories → Products** (один-ко-многим):  
  Одна категория может содержать много товаров.  
  `Products.category_id` является внешним ключом, ссылающимся на `Categories.category_id`.

- **Customers → Orders** (один-ко-многим):  
  Один покупатель может сделать много заказов.  
  `Orders.customer_id` является внешним ключом, ссылающимся на `Customers.customer_id`.

- **Orders → Order_Items** (один-ко-многим):  
  Один заказ может содержать много товаров.  
  `Order_Items.order_id` является внешним ключом, ссылающимся на `Orders.order_id`.

- **Products → Order_Items** (один-ко-многим):  
  Один товар может быть в разных заказах.  
  `Order_Items.product_id` является внешним ключом, ссылающимся на `Products.product_id`.

- **Orders ↔ Products** (многие-ко-многим):  
  Эта связь реализована через промежуточную таблицу `Order_Items`.

---

## Part 3: ER-диаграмма


## Дополнительно: цели и задачи проекта

Данная база данных предназначена для управления интернет-магазином электроники.  
Она позволяет:
- хранить информацию о товарах и категориях;
- управлять покупателями и их заказами;
- отслеживать состав каждого заказа;
- анализировать продажи и популярность товаров.

---

*Проект выполнил: Влад Каменков*  
*Дата: август 2026*