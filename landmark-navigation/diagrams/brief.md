# Навигация по ориентирам

Общая идея: хотелось бы озвучить маршрут из точки A в точку B через ориентиры. Сделать маршрут более прогнозируемым и интересным. Ограничимся пешей прогулкой

> Сделать интерфейс как в приложении 2GIS, там два поля: точка A, точка B, их можно менять местами, переназначать и т.д. Ниже после работы системы описать маршрут через ориентиры, например:

➡️ Пройдите мимо Пятёрочки

↩️ Возле Аптеки "Здоровье" поверните налево

🏁 Через 100 м вы на месте

### 1. Построить обычный маршрут A -> B

Пример вывода [API](https://docs.2gis.com/ru/api/navigation/directions/reference/directions_601#/paths/~1carrouting~16.0.1~1global/post). Вывод уже разбит на шаги, сегменты с комментариями:

```json
{
	"maneuvers": [
		{
			"comment": "Source",
			"icon": "start",
			"id": "18243427438627852119",
			"outcoming_path": {
				"distance": 13,
				"duration": 4,
				"geometry": [],
				"names": []
			},
			"outcoming_path_comment": "10 м прямо",
			"type": "begin"
		},
		{
			"comment": "Поворот направо на ул. Петухова",
			"icon": "crossroad_right",
			"id": "11013427180351570021",
			"outcoming_path": {
				"distance": 379,
				"duration": 105,
				"geometry": [],
				"names": []
			},
			"outcoming_path_comment": "400 м прямо",
			"turn_angle": 90,
			"turn_direction": "right",
			"type": "crossroad"
		},
		{
			"comment": "Поворот направо на ул. Петухова",
			"icon": "crossroad_right",
			"id": "10486992078115446896",
			"outcoming_path": {
				"distance": 1994,
				"duration": 277,
				"geometry": [],
				"names": []
			},
			"outcoming_path_comment": "2 км прямо",
			"turn_angle": 90,
			"turn_direction": "right",
			"type": "crossroad"
		},
		{
			"comment": "Круговое движение 1 съезд на ул. Сибиряков-Гвардейцев",
			"icon": "ringroad_right_90",
			"id": "851511220966961902",
			"outcoming_path": {
				"distance": 51,
				"duration": 8,
				"geometry": [],
				"names": []
			},
			"outcoming_path_comment": "50 м прямо",
			"ringroad_exit_number": 1,
			"turn_angle": 85,
			"type": "ringroad"
		},
		{
			"comment": "1 съезд на ул. Сибиряков-Гвардейцев",
			"icon": "ringroad_exit",
			"id": "14676290839728035649",
			"outcoming_path": {
				"distance": 3362,
				"duration": 1003,
				"geometry": [],
				"names": []
			},
			"outcoming_path_comment": "3.4 км прямо",
			"type": "ringroad_exit"
		},
		{
			"comment": "Поворот направо на ул. Немировича-Данченко",
			"icon": "crossroad_right",
			"id": "11682105410583176895",
			"outcoming_path": {
				"distance": 5061,
				"duration": 691,
				"geometry": [],
				"names": []
			},
			"outcoming_path_comment": "5.1 км прямо",
			"turn_angle": 100,
			"turn_direction": "right",
			"type": "crossroad"
		},
		{
			"comment": "Плавный поворот направо на ул. Большевистская",
			"icon": "crossroad_slightly_right",
			"id": "3887500705741526467",
			"outcoming_path": {
				"distance": 329,
				"duration": 80,
				"geometry": [],
				"names": []
			},
			"outcoming_path_comment": "350 м прямо",
			"turn_angle": 13,
			"turn_direction": "slightly_right",
			"type": "crossroad"
		},
		{
			"comment": "Крутой поворот направо на ул. Большевистская",
			"icon": "crossroad_sharply_right",
			"id": "17324583098489101207",
			"outcoming_path": {
				"distance": 912,
				"duration": 258,
				"geometry": [],
				"names": []
			},
			"outcoming_path_comment": "900 м прямо",
			"turn_angle": 158,
			"turn_direction": "sharply_right",
			"type": "crossroad"
		},
		{
			"comment": "Держитесь правее",
			"icon": "crossroad_keep_right",
			"id": "2357458904113779569",
			"outcoming_path": {
				"distance": 198,
				"duration": 25,
				"geometry": [],
				"names": []
			},
			"outcoming_path_comment": "200 м прямо",
			"turn_angle": 2,
			"turn_direction": "keep_right",
			"type": "crossroad"
		},
		{
			"comment": "Круговое движение 1 съезд на ул. Ипподромская",
			"icon": "ringroad_right_45",
			"id": "3505931146236764371",
			"outcoming_path": {
				"distance": 20,
				"duration": 3,
				"geometry": [],
				"names": []
			},
			"outcoming_path_comment": "20 м прямо",
			"ringroad_exit_number": 1,
			"turn_angle": 48,
			"type": "ringroad"
		},
		{
			"comment": "1 съезд на ул. Ипподромская",
			"icon": "ringroad_exit",
			"id": "8473919833578789823",
			"outcoming_path": {
				"distance": 2371,
				"duration": 260,
				"geometry": [],
				"names": []
			},
			"outcoming_path_comment": "2.4 км прямо",
			"type": "ringroad_exit"
		},
		{
			"comment": "Поворот направо на ул. Ядринцевский Конный спуск",
			"icon": "crossroad_right",
			"id": "9217065371019675846",
			"outcoming_path": {
				"distance": 251,
				"duration": 47,
				"geometry": [],
				"names": []
			},
			"outcoming_path_comment": "250 м прямо",
			"turn_angle": 47,
			"turn_direction": "right",
			"type": "crossroad"
		},
		{
			"comment": "Поворот направо на ул. Ядринцевский Конный спуск",
			"icon": "crossroad_right",
			"id": "7594775025999479592",
			"outcoming_path": {
				"distance": 116,
				"duration": 24,
				"geometry": [],
				"names": []
			},
			"outcoming_path_comment": "100 м прямо",
			"turn_angle": 101,
			"turn_direction": "right",
			"type": "crossroad"
		},
		{
			"comment": "Крутой поворот налево на ул. Военная Горка 5-я линия",
			"icon": "crossroad_sharply_left",
			"id": "18286432877377999606",
			"outcoming_path": {
				"distance": 102,
				"duration": 28,
				"geometry": [],
				"names": []
			},
			"outcoming_path_comment": "100 м прямо",
			"turn_angle": -117,
			"turn_direction": "sharply_left",
			"type": "crossroad"
		},
		{
			"comment": "Поворот направо на ул. Военная Горка 5-я линия",
			"icon": "crossroad_right",
			"id": "7570173330757430500",
			"outcoming_path": {
				"distance": 27,
				"duration": 8,
				"geometry": [],
				"names": []
			},
			"outcoming_path_comment": "30 м прямо",
			"turn_angle": 48,
			"turn_direction": "right",
			"type": "crossroad"
		},
		{
			"comment": "Target",
			"icon": "finish",
			"id": "13991250694901917865",
			"outcoming_path_comment": "Вы на месте!",
			"type": "end"
		}
	]
}
```

> Идея: для начала сделать обработку только некоторых иконок маневров

### 2. Поиск ориентиров для каждого сегмента

С помощью [этого API](https://docs.2gis.com/ru/api/search/places/reference/3.0/items) можно получить в указанном радиусе от точки (задана широтой и долготой) все места по указанным категориям.

### 3. Генерация текстовой инструкции

Подать на вход LLM маршрут по сегментам с подобранными ориентирами и сгенерировать более человечное описание маршрута

> Можно ли определить, как поступить пользователю при нахождении ориентира? Повернуть перед/после ориентира, двигаться в сторону ориентира (например высотки или другого объекта, который видно издалека) 

> Как провалидировать сгенерированное описание маршрута? 

> Идея: сделать подсказки вроде "По правую сторону будет пятерочка, нужно будет повернуть направо во двор..."