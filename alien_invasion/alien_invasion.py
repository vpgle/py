# -*- coding: gb18030 -*-

import sys

import pygame

def run_game():
    # ��ʼ����Ϸ������һ����Ļ����
    pygame.init()
    screen = pygame.display.set_mode((1920, 1200))
    pygame.display.set_caption("Alien Invasion")

    # ��ʼ��Ϸ����ѭ��
    while True:
    
        # ���Ӽ��̺�����¼�
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        
        # ��������Ƶ���Ļ�ɼ�
        pygame.display.flip()

run_game()
