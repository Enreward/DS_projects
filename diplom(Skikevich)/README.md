Дипломный проект на курсе Data Science:
Интеллектуальная система оптимизации ценообразования услуг частного медицинского центра.

Этапы работы:
- Введение
- Цель
- Задачи
- Выбор метрики оценивания
- Осмотр данных
- Наивная модель
- EDA
- Корреляционный анализ
- Обучение
- Выводы
- Итоги

Цель:  
Разработать модель машинного обучения, прогнозирующую величину продаж услуг для 
использования в интеллектуальной системе ценовой оптимизации частного медицинского центра.

Задачи:  
- Выбрать метрику оценивания;
- Собрать данные из внутренних и внешних источников;
- Осмотреть данные;
- Разработать наивную модель;
- Провести EDA;
- Разработать и протестировать различные модели.
- Выбрать финальную модель и проанализировать некоторые услуги по предсказаниям выбранной модели.

Данные:  
service_id 			- id услуги
cost 				- цена
name 				- название услуги
item_code 			- стандартизированный код услуги
medical_specialty 	- медицинская специальность
amount_doctors 		- количество врачей, принимающих в этот день
service_date 		- дата оказания услуги в формате строки вида дд.мм.гггг
sales 				- спрос
service_type 		- номенклатурная группа услуги
weekend 			- триггер календарного выходного дня
weekday 			- день недели в сокращённом формате
holiday 			- триггер праздничного дня по данным производственных календарей
season 				- время года
unique_service 		- триггер услуги, оказываемой только в нашем МЦ
pandemic 			- триггер эпидемиологической ситуации по данным ВОЗ
month 				- название месяца в сокращённом формате


**Об основных этапах**  
Метрики RMSE и MPE

Наивная модель: в качестве наивной модели было взято скользящее среднее с окном в 2 дня.  

EDA: 
в разделе представлен подробный осмотр данных с помощью pandas_profiling, графики зависимости таргета от некоторых признаков для одной услуги.

Финальная обработка признаков:
в разделе произведен feature ingeneering и приведение признаков к виду, необходимому для загрузки в модели машинного обучения.

Обучение моделей: 
в разделе представлено обучение двух моделей на основе градиентного бустинга - CatBoost и LightGBM

