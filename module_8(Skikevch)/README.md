Учебный проект на курсе Data Science:
Прогнозирование стоимости автомобиля по характеристикам
Цель:  
Разработать модель для предсказания стоимости автомобиля по различным данным - табличным, текстовым и графическим.

Задачи:  
- построить наивную модель
- обработать признаки
- обучить CatBoostRegressor
- обучить простую нейронную сеть
- обучить multi-input сеть на табличных и текстовых данных
- обучить multi-input сеть на табличных,текстовых данных и фотографиях
- ансамблировать результаты предсказаний

Данные:  
**Табличные признаки**  
- bodyType - категориальный
- brand - категориальный
- color - категориальный
- description - текстовый
- engineDisplacement - числовой, представленный как текст
- enginePower - числовой, представленный как текст
- fuelType - категориальный
- mileage - числовой
- modelDate - числовой
- model_info - категориальный
- name - категориальный, желательно сократить размерность
- numberOfDoors - категориальный
- price - числовой, целевой
- productionDate - числовой
- sell_id - изображение (файл доступен по адресу, основанному на sell_id)
- vehicleConfiguration - содержит информацию, содержащуюся в других признаках
- vehicleTransmission - категориальный
- Владельцы - категориальный
- Владение - числовой, представленный как текст
- ПТС - категориальный
- Привод - категориальный
- Руль - категориальный

**Текст**  
- текстовые данные представлены в формате комментариев к лотам.

**Изображения**  
- по одной фотографии на каждый лот.

**Подробнее об этапах**  
Наивная модель: в качестве наивной модели экстраполяция таргета по двум значимым признакам.  

Обработка признаков: 
- приведение признаков к единому формату
- нормализация
- обработка категориальных признаков двумя способами для двух видов моделей.  

Обучение моделей: в данных разделах представлены лучшие из всех экспериментов со скриншотами результатов и графиков обучения. Использовались модели CatBoost, нейронная сеть с архитектурой собственной разработки на табличных данных, и две multi-input сети (сеть на табличных данных + NLP с архитектурой собственной разработки; сеть на табличных данных + NLP с архитектурой собственной разработки + DenseNet201)

Ансамблирование и выводы: в данных разделах проведено финальное ансамблирование результатов с проверкой точности по метрике MAPE и представлены выводы и дальнейшие умозаключения по доработке проекта.

