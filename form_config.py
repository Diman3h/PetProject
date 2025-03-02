SECTIONS = {
    1: "Администрирование пользователей и прав доступа",
    2: "Анализ договорной документации по 152-ФЗ",
    3: "Проведение инструкитажей по вопросам информационной безопасности",
    4: "Разработка внутренней организационно распорядительной документации по вопросам информационной безопасности",
    5: "Организация обработки ПДн в структурных подразделениях",
    6: "Инвентаризация ИТ-активов ООО 'ПАРК ФОРОС'",
    7: "Администрирование СЗИ",
    8: "Монитороинг Событий ИБ",
    9: "Анализ уязвимостей и актуальных угроз",
    10: "Контроль за резервированием и обеспечением экстренного восстановления",
    11: "Работа органа криптографической защиты информации",
    12: "Работа с инструктивной и нормативно-правовой документацией по вопрсам информационной безопасности"
}
# hidden используется для того, чтобы задать какие поля не будут создаваться
METRIC_CONFIGS = {
    1: {
        "section_id": 1,
        "title": "Предоставление доступов к ресурсам и системам по заявкам",
        "labels": {
            "user_label": "ФИО пользователя",
            "initiator_label": "ФИО Инициатора",
            "label1": "Перечень доступов",
            "label2": "Поле 4",
            "label3": "Поле 5"
        },
        "hidden": ["label2", "label3"],
        "target_count": 10
    },
    2: {
        "section_id": 1,
        "title": "Сброс паролей и разблокировка учетных записей",
        "labels": {
            "user_label": "ФИО пользователя",
            "initiator_label": "ФИО инициатора",
            "label1": "Тип('разблокировка' или 'сброс')",
            "label2": "ФИО исполнителя",
            "label3": "Поле 5"
        },
        "hidden": ["label3"],
        "target_count": 10
    },
    3: {
        "section_id": 1,
        "title": "Анализ и актуализация должностных инструкций",
        "labels": {
            "user_label": "Поле 1",
            "initiator_label": "Поле 2",
            "label1": "Поле 3",
            "label2": "Поле 4",
            "label3": "Поле 5"
        },
        "target_count": 5
    },
    4: {
        "section_id": 1,
        "title": "Поиск неактивных УЗ, анализ и актуализация выданных прав доступа",
        "labels": {
            "user_label": "ФИО Пользователя",
            "initiator_label": "Тип('Отключение' или 'Удаление'",
            "label1": "Поле 3",
            "label2": "Поле 4",
            "label3": "Поле 5"
        },
        "hidden": ["label1","label2", "label3"],
        "target_count": 4
    },
    5: {
        "section_id": 2,
        "title": "Определить цель обработки ПДн, категории ПДн, получение соглсий, передача третьим лицам / трансграничная, требование конфиденциальности и защты",
        "labels": {
            "user_label": "Название Договора",
            "initiator_label": "Поле 2",
            "label1": "Поле 3",
            "label2": "Поле 4",
            "label3": "Поле 5"
        },
        "hidden": ["initiator_label", "label1","label2", "label3"],
        "target_count": 2
    },
    6: {
        "section_id": 2,
        "title": "______________",
        "labels": {
            "user_label": "ФИО Исполнителя",
            "initiator_label": "Название документа",
            "label1": "Поле 3",
            "label2": "Поле 4",
            "label3": "Поле 5"
        },
        "hidden": ["label1","label2", "label3"],
        "target_count": 6
    },
    7: {
        "section_id": 2,
        "title": "_________________",
        "labels": {
            "user_label": "Поле 1",
            "initiator_label": "Поле 2",
            "label1": "Поле 3",
            "label2": "Поле 4",
            "label3": "Поле 5"
        },
        "target_count": 10
    },
    8: {
        "section_id": 3,
        "title": "Вводный инструктаж при трудоустройстве",
        "labels": {
            "user_label": "ФИО пользователя",
            "initiator_label": "Поле 2",
            "label1": "Поле 3",
            "label2": "Поле 4",
            "label3": "Поле 5"
        },
        "hidden": ["initiator_label","label1","label2", "label3"],
        "target_count": 10
    },
    9: {
        "section_id": 3,
        "title": "Первичный инструктаж обработка и защита персональных данных",
        "labels": {
            "user_label": "ФИО пользователя",
            "initiator_label": "Поле 2",
            "label1": "Поле 3",
            "label2": "Поле 4",
            "label3": "Поле 5"
        },
        "hidden": ["initiator_label","label1","label2", "label3"],
        "target_count": 10
    },
    10: {
        "section_id": 3,
        "title": "Первичный инструктаж работа в ИСПДН",
        "labels": {
            "user_label": "ФИО пользователя",
            "initiator_label": "Поле 2",
            "label1": "Поле 3",
            "label2": "Поле 4",
            "label3": "Поле 5"
        },
        "hidden": ["initiator_label","label1","label2", "label3"],
        "target_count": 10
    },
    11: {
        "section_id": 3,
        "title": "Инструктаж сотрудников Медицинского центра",
        "labels": {
            "user_label": "ФИО пользователя",
            "initiator_label": "Поле 2",
            "label1": "Поле 3",
            "label2": "Поле 4",
            "label3": "Поле 5"
        },
        "hidden": ["initiator_label","label1","label2", "label3"],
        "target_count": 10
    },
    12: {
        "section_id": 4,
        "title": "Утверждено приказов",
        "labels": {
            "user_label": "ФИО исполнителя",
            "initiator_label": "Наименование документа",
            "label1": "Поле 3",
            "label2": "Поле 4",
            "label3": "Поле 5"
        },
        "hidden": ["label1","label2", "label3"],
        "target_count": 2
    },
    13: {
        "section_id": 4,
        "title": "Разработка проектов приказов",
        "labels": {
            "user_label": "ФИО исполнителя",
            "initiator_label": "Наименование документа",
            "label1": "Поле 3",
            "label2": "Поле 4",
            "label3": "Поле 5"
        },
        "hidden": ["label1","label2", "label3"],
        "target_count": 2
    },
    14: {
        "section_id": 5,
        "title": "Анализ движения персональных данных в подразделениях",
        "labels": {
            "user_label": "Поле 1",
            "initiator_label": "Поле 2",
            "label1": "Поле 3",
            "label2": "Поле 4",
            "label3": "Поле 5"
        },
        "target_count": 2
    },
    15: {
        "section_id": 5,
        "title": "Анализ и актулизация документации",
        "labels": {
            "user_label": "Поле 1",
            "initiator_label": "Поле 2",
            "label1": "Поле 3",
            "label2": "Поле 4",
            "label3": "Поле 5"
        },
        "target_count": 2
    },
    16: {
        "section_id": 6,
        "title": "Обнаружено и идентифицированно хостов в домене (без серверов)",
        "labels": {
            "user_label": "Имя хоста",
            "initiator_label": "Поле 2",
            "label1": "Поле 3",
            "label2": "Поле 4",
            "label3": "Поле 5"
        },
        "hidden": ["initiator_label","label1","label2", "label3"],
        "target_count": 10
    },
    17: {
        "section_id": 6,
        "title": "Active Directory - отключение неактивных хостов",
        "labels": {
            "user_label": "Имя хоста",
            "initiator_label": "Поле 2",
            "label1": "Поле 3",
            "label2": "Поле 4",
            "label3": "Поле 5"
        },
        "hidden": ["initiator_label","label1","label2", "label3"],
        "target_count": 5
    },
    18: {
        "section_id": 6,
        "title": "Идентифицировано хостов без АВЗ ",
        "labels": {
             "user_label": "Имя хоста",
            "initiator_label": "Поле 2",
            "label1": "Поле 3",
            "label2": "Поле 4",
            "label3": "Поле 5"
        },
        "hidden": ["initiator_label","label1","label2", "label3"],
        "target_count": 5
    },
    19: {
        "section_id": 6,
        "title": "Идентифицировано хостов без DLP",
        "labels": {
             "user_label": "Имя хоста",
            "initiator_label": "Поле 2",
            "label1": "Поле 3",
            "label2": "Поле 4",
            "label3": "Поле 5"
        },
        "hidden": ["initiator_label","label1","label2", "label3"],
        "target_count": 5
    },
    20: {
        "section_id": 7,
        "title": "DrWeb - Контроль приложений (исключения)",
        "labels": {
            "user_label": "Приложение",
            "initiator_label": "Название правиал",
            "label1": "Хеш / имя файла",
            "label2": "Поле 9.1.4",
            "label3": "Поле 9.1.5"
        },
        "hidden": ["label2", "label3"],
        "target_count": 12
    },
    21: {
        "section_id": 7,
        "title": "Обращение в техподдержку(DrWeb)",
        "labels": {
            "user_label": "Причина",
            "initiator_label": "Ответ ",
            "label1": "",
            "label2": "Поле 9.1.4",
            "label3": "Поле 9.1.5"
        },
        "hidden": ["label1","label2", "label3"],
        "target_count": 1
    },
    22: {
        "section_id": 7,
        "title": "Обращение в техподдержку(Staffcop)",
        "labels": {
            "user_label": "Причина",
            "initiator_label": "Ответ ",
            "label1": "",
            "label2": "Поле 9.1.4",
            "label3": "Поле 9.1.5"
        },
        "hidden": ["label1","label2", "label3"],
        "target_count": 1
    },
    23: {
        "section_id": 8,
        "title": "Мониторинг событий",
        "labels": {
            "user_label": "ФИО Пользователя",
            "initiator_label": "СЗИ",
            "label1": "Причина",
            "label2": "Описание",
            "label3": "Результат"
        },
        "target_count": 5
    },
    24: {
        "section_id": 9,
        "title": "Инвентаризация DrWeb",
        "labels": {
            "user_label": "Количество хостов в домене(a)",
            "initiator_label": "Количество хостов в СЗИ(b)",
            "label1": "a/b",
            "label2": "Поле 10.2.4",
            "label3": "Поле 10.2.5"
        },
        "hidden": ["label2", "label3"],
        "target_count": 1
    },
    25: {
        "section_id": 9,
        "title": "Инвентаризация Staffcop",
        "labels": {
            "user_label": "Количество хостов в домене(a)",
            "initiator_label": "Количество хостов в СЗИ(b)",
            "label1": "a/b",
            "label2": "Поле 10.2.4",
            "label3": "Поле 10.2.5"
        },
        "hidden": ["label2", "label3"],
        "target_count": 1
    },
    26: {
        "section_id": 10,
        "title": "Метрика 10.1",
        "labels": {
            "user_label": "Поле 11.1.1",
            "initiator_label": "Поле 11.1.2",
            "label1": "Поле 11.1.3",
            "label2": "Поле 11.1.4",
            "label3": "Поле 11.1.5"
        },
        "target_count": 10
    },
    27: {
        "section_id": 11,
        "title": "Метрика 11.1",
        "labels": {
            "user_label": "Поле 12.1.1",
            "initiator_label": "Поле 12.1.2",
            "label1": "Поле 12.1.3",
            "label2": "Поле 12.1.4",
            "label3": "Поле 12.1.5"
        },
        "target_count": 10
    },
    28: {
        "section_id": 12,
        "title": "21.2. Работа с нормативно-правовой базой",
        "labels": {
            "user_label": "ФЗ и подзаконне акты",
            "initiator_label": "НПА РКН",
            "label1": "НПА ФСТЭК",
            "label2": "НПА ФСБ",
            "label3": "Поле 12.1.5"
        },
        "hidden": ["label3"],
        "target_count": 1
    },
    29: {
        "section_id": 12,
        "title": "12.2. Работа с документацией инструкциями к СЗИ/СКЗИ ",
        "labels": {
            "user_label": "СКЗИ",
            "initiator_label": "СЗИ",
            "label1": "Поле 12.1.3",
            "label2": "Поле 12.1.4",
            "label3": "Поле 12.1.5"
        },
        "hidden": ["label1", "label2", "label3"],
        "target_count": 1
    },
    30: {
        "section_id": 12,
        "title": "12.3. Изучение протоколов, службы, сервисов и прочих технологий ",
        "labels": {
            "user_label": "Windows",
            "initiator_label": "Linux",
            "label1": "Поле 12.1.3",
            "label2": "Поле 12.1.4",
            "label3": "Поле 12.1.5"
        },
        "hidden": ["label1", "label2", "label3"],
        "target_count": 1
    },
    31: {
        "section_id": 7,
        "title": "Адмнистрирование DLP (Staffcop)",
        "labels": {
            "user_label": "Установка агентов",
            "initiator_label": "Правила для фильтрации",
            "label1": "Настройка конфигураций",
            "label2": "Настройка сервера",
            "label3": "поле 7.1.5"
        },
        "hidden": ["label3"],
        "target_count": 1
    },
    32: {
        "section_id": 7,
        "title": "Антивирусная сеть",
        "labels": {
            "user_label": "Установка агентов",
            "initiator_label": "Анализ вредоносного ПО (VirusTotal / ANY.RUN)",
            "label1": "Настройка конфигураций",
            "label2": "Настройка сервера",
            "label3": "Поле 9.1.5"
        },
        "hidden": ["label3"],
        "target_count": 12
    },
    33:{
        "section_id": 7,
        "title": "Скрипты, скомпллированные .exe и GPO/AD",
        "labels": {
            "user_label": "Групповые политики GPO / контейнеры AD",
            "initiator_label": "Скрипты powershell/bat",
            "label1": "Скомпилированные .exe на C/Python",
            "label2": "НПоле 9.1.5",
            "label3": "Поле 9.1.5"
        },
        "hidden": ["label2", "label3"],
        "target_count": 12
    }
}