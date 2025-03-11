# 🚀 Начало работы с Apache Superset и ClickHouse

## 📚 Введение

### Apache Superset

**Apache Superset** - современное веб-приложение для бизнес-аналитики и визуализации данных.  
🔗 [Официальная документация](https://superset.apache.org/)  
⭐ [GitHub репозиторий](https://github.com/apache/superset)

### ClickHouse

**ClickHouse** - высокопроизводительная колоночная СУБД для аналитики в реальном времени.  
🔗 [Официальная документация](https://clickhouse.com/docs/)  
⭐ [GitHub репозиторий](https://github.com/ClickHouse/ClickHouse)

---

## 👥 Кто и зачем использует Apache Superset?

### 🔍 Основные пользователи:

- **Аналитики данных**  
  📈 Создание интерактивных дашбордов и отчетов  
  🔎 Исследовательский анализ данных (EDA)  
  🎨 Визуализация сложных SQL-запросов

- **Бизнес-пользователи**  
  📊 Мониторинг бизнес-метрик в реальном времени  
  📑 Генерация отчетов для руководства  
  🔄 Анализ динамики ключевых показателей

- **Разработчики/Data Engineers**  
  ⚙️ Интеграция с внешними системами через API  
  🔐 Настройка прав доступа и ролей  
  🛠️ Оптимизация запросов через SQL Lab

- **Руководители отделов**  
  🎯 Отслеживание выполнения целей (OKR/KPI)  
  🌐 Сводные аналитические панели  
  ⏱️ Быстрый доступ к актуальной статистике

### 💡 Ключевые сценарии использования:

```bash
1. Анализ продаж и маркетинговых кампаний
2. Визуализация данных IoT-устройств
3. Мониторинг активности пользователей
4. Финансовая аналитика и прогнозирование
5. Оперативная отчетность для стейкхолдеров
```

## 🛠️ Установка и запуск

1. **Клонируйте репозиторий**

   ```bash
   git clone https://github.com/Mardvey-UMA/ApacheSupersetStart.git
   cd ApacheSupersetStart
   ```

2. **Запустите docker-compose** 🐳

   ```bash
   docker-compose up --build -d
   ```

3. **Важно!** После запуска:  
   ⚠️ Из-за отсутствия healthcheck может потребоваться перезапуск контейнеров:
   ```bash
   docker-compose restart data-loader apache-superset
   ```

---

## 🔧 Конфигурационная информация

```ini

# ClickHouse
URI: clickhouse+native://test:test@clickhouse:9000/test

Доступные таблицы:

- [cryptocurrency_prices]
- [employees]
- [geography_data]
- [ml_results]
- [sales]

# Apache Superset

URL: http://0.0.0.0:8088/login/
Логин: admin
Пароль: admin
```

---

## Подключение базы данных

![alt text](screenshots/connect.png)
![alt text](screenshots/connect_db.png)

---

## Создание Датасета

![alt text](screenshots/create_ds.png)
![alt text](screenshots/listoftables.png)

## Первые визуализации

### Все настройки для визуализаций можно найти на скриншотах

### 1. Тепловая карта

![alt text](screenshots/heatmap1.png)

---

### 2. Временной ряд с ценами криптовалют

![alt text](screenshots/crypto1.png)

---

### 3. Карта мира с доходами по странам

![alt text](screenshots/country_salary.png)

---

### 4. Bubble Chart Зарплаты

![alt text](screenshots/bubble.png)

---

### 5. Собственный Tensorboard

![alt text](screenshots/customtensorboard.png)

---

### 6. Круговая диаграмма с отношением

![alt text](screenshots/round.png)

---

## Dashboards

### Создание Dashboard

![alt text](screenshots/credshb.png)
drug-n-drop для переноса графиков
![alt text](screenshots/dranddrop.png)
результат
![alt text](screenshots/dashboard.png)
