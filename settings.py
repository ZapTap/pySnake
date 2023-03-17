import pygame

settings = {
	"Env": {
		"Name": "Snake",
		"Resolution": [1200, 800],
		"Scale": [40, 40],
		"FPS": 60,
		"BackgroundColor": (0, 0, 0),
		"States": {
			0: "QUIT",
			1: "PLAY"
		}
	},
	"Obj": {
		"Player": {
			"RefreshRate": 400,
			"StartPos": [15, 10],
			"BodyColor": (255, 255, 255),
			"Border": [5, 5],
			"Keys": {
				pygame.K_w: (0, -1),
				pygame.K_a: (-1, 0),
				pygame.K_s: (0, 1),
				pygame.K_d: (1, 0)
			}
		},
		"FPS": {
			"TextColor": (0, 255, 0),
			"Font": ['freesansbold.ttf', 20],
			"BackgroundColor": (0, 0, 0),
			"BackgroundOpacity": 0.6
		}
	}
}