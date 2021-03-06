# -*- coding: utf-8 -*-

# enlève le message welcome from pygame
import os

os.environ["PYGAME_HIDE_SUPPORT_PROMPT"] = "hide"

# règle le problème de l'icône dans la barre des tâches
import ctypes

myappid = 'mycompany.myproduct.subproduct.version'
ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)

import pygame
from ressource import *
from DialogueBox import animation_text, istime


# définition d'une fonction qui lance le menu principal au lancement du jeu
def main():
    option = Option()

    width = option.w  # caractéristiques de la fenêtre
    height = option.h
    black = pygame.Color(0, 0, 0)  # crée un objet couleur  en ayant référence RGB du noir
    fade = pygame.Surface((width, height))
    fade.fill((0, 0, 0))
    bisfade = pygame.Surface((width, height))
    bisfade.fill((0, 0, 0))
    fade.set_alpha(0)
    bisfade.set_alpha(255)
    white = pygame.Color(255, 255, 255)  # crée un objet couleur  en ayant référence RGB du blanc
    red = pygame.Color(255, 0, 0)  # de même
    blue = pygame.Color(0, 0, 255)
    green = pygame.Color(0, 255, 0)
    yellow = pygame.Color(255, 255, 0)

    loading = pygame.image.load  # pour que ce soit plus rapide pour charger des images
    icon = loading("images/logo.png")
    # le titre en fenêtre de jeu
    pygame.display.set_caption("Red Blaze")
    pygame.display.set_icon(icon)
    screen = pygame.display.set_mode((width, height),
                                     pygame.RESIZABLE)  # pour ouvrir une fenêtre aux dimensions height width

    frontpops = []
    backpops = []
    rightpops = []
    leftpops = []
    Wfrontpops = []
    Wrightpops = []
    Wleftpops = []
    Rfrontpops = []
    Rbackpops = []
    Rrightpops = []
    Rleftpops = []
    RWfrontpops = []
    RWrightpops = []
    RWleftpops = []
    bouncepops = []
    dubitatifpops = []
    dubitatif_bispops = []
    frontfalo = []
    rightfalo = []
    leftfalo = []
    bouncefalo = []
    for i in range(6):
        frontpops.append(
            loading("images/chara/pops/sprite_standing/front/normal/front{}.png".format(i + 1)).convert_alpha())

        backpops.append(loading("images/chara/pops/sprite_standing/back/back{}.png".format(i + 1)).convert_alpha())

        rightpops.append(
            loading("images/chara/pops/sprite_standing/right/normal/right{}.png".format(i + 1)).convert_alpha())

        leftpops.append(
            loading("images/chara/pops/sprite_standing/left/normal/left{}.png".format(i + 1)).convert_alpha())

        Wfrontpops.append(
            loading("images/chara/pops/sprite_standing/front/wink/front{}.png".format(i + 1)).convert_alpha())

        Wrightpops.append(
            loading("images/chara/pops/sprite_standing/right/wink/right{}.png".format(i + 1)).convert_alpha())

        Wleftpops.append(
            loading("images/chara/pops/sprite_standing/left/wink/left{}.png".format(i + 1)).convert_alpha())

        Rfrontpops.append(
            loading("images/chara/pops/sprite_walking/front/normal/front{}.png".format(i + 1)).convert_alpha())

        Rbackpops.append(loading("images/chara/pops/sprite_walking/back/back{}.png".format(i + 1)).convert_alpha())

        Rrightpops.append(
            loading("images/chara/pops/sprite_walking/right/normal/right{}.png".format(i + 1)).convert_alpha())

        Rleftpops.append(
            loading("images/chara/pops/sprite_walking/left/normal/left{}.png".format(i + 1)).convert_alpha())

        RWfrontpops.append(
            loading("images/chara/pops/sprite_walking/front/wink/front{}.png".format(i + 1)).convert_alpha())

        RWrightpops.append(
            loading("images/chara/pops/sprite_walking/right/wink/right{}.png".format(i + 1)).convert_alpha())

        RWleftpops.append(
            loading("images/chara/pops/sprite_walking/left/wink/left{}.png".format(i + 1)).convert_alpha())

        frontfalo.append(loading("images/chara/falo/sprite_standing/front/front{}.png".format(i + 1)))

        leftfalo.append(loading("images/chara/falo/sprite_standing/left/left{}.png".format(i + 1)))

        rightfalo.append(loading("images/chara/falo/sprite_standing/right/right{}.png".format(i + 1)))

    for i in range(4):
        bouncepops.append(loading("images/dialogue/face_discussion/Pops/"
                                  + "bounce/bounce{}.png ".format(i + 1)).convert_alpha())
        dubitatifpops.append(loading("images/dialogue/face_discussion"
                                     + "/Pops/dubitatif/dubitatif{}.png ".format(i + 1)).convert_alpha())

        dubitatif_bispops.append(loading("images/dialogue/face_discussion"
                                         + "/Pops/dubitatif2/dubitatif_bis{}.png ".format(i + 1)).convert_alpha())

        bouncefalo.append(loading("images/dialogue/face_discussion"
                                  + "/Falo/bounce/bounce{}.png".format(i + 1)).convert_alpha())

    bar = loading("images/level/background/bar.png").convert_alpha()
    dialogue_box = loading("images/dialogue/dialogue_box.png").convert()

    curseur = [loading("images/dialogue/curseur/Sprite-0001.png").convert_alpha(),
               loading("images/dialogue/curseur/Sprite-0002.png").convert_alpha()]

    initialPosX = 600
    initialPosY = 400

    widthPops, heightPops = backpops[0].get_rect().size
    velPops = 5

    Pops = Player(initialPosX, initialPosY, velPops, frontpops,
                  backpops,
                  rightpops,
                  leftpops,
                  Wfrontpops,
                  Wrightpops,
                  Wleftpops,
                  Rfrontpops,
                  Rbackpops,
                  Rrightpops,
                  Rleftpops,
                  RWfrontpops,
                  RWrightpops,
                  RWleftpops,
                  bouncepops,
                  dubitatifpops,
                  dubitatif_bispops)  # toutes les caractéristiques de Pops

    # toutes les caractéristiques pour le scrolling
    # on prend la moitié de l'écran pour le début du scrolling 
    startScrollingX = option.mw
    startScrollingY = option.mh

    Bar = Scene(bar, 500, -300)
    table1 = loading("images/level/objects/table1.png").convert_alpha()
    comptoir1 = loading("images/level/objects/comptoir1.png").convert_alpha()
    comptoir2 = loading("images/level/objects/comptoir2.png").convert_alpha()
    comptoir3 = loading("images/level/objects/comptoir3.png").convert_alpha()
    comptoir4 = loading("images/level/objects/comptoir4.png").convert_alpha()
    buffet = loading("images/level/objects/buffet.png").convert_alpha()
    tabouret = loading("images/level/objects/tabouret.png").convert_alpha()
    horloge = loading("images/level/objects/horloge.png").convert_alpha()
    tele = loading("images/level/objects/tele.png")
    mur1 = loading("images/level/objects/mur1.png")
    mur2 = loading("images/level/objects/mur2.png")
    Mur1 = Object(mur1, Bar, -168, 0)
    Mur2 = Object(mur1, Bar, Bar.width - 32, 0)
    Mur3 = Object(mur2, Bar, 30, 30)
    Mur4 = Object(mur2, Bar, 30, Bar.height-50)
    Horloge = Object(horloge, Bar, 122, 116)
    Tele = Object(tele, Bar, 1129, 100)
    Buffet = Object(buffet, Bar, 396, 54)
    Tabouret = Object(tabouret, Bar, 1044, 536)
    Comptoir1 = Object(comptoir1, Bar, 310, 410)
    Comptoir2 = Object(comptoir2, Bar, 310 + Comptoir1.rect.w, 410)
    Comptoir3 = Object(comptoir3, Bar, 310 + Comptoir1.rect.w + Comptoir2.rect.w, 410)
    Comptoir4 = Object(comptoir4, Bar, 310 + Comptoir1.rect.w + Comptoir2.rect.w + Comptoir3.rect.w, 343)
    Table1 = Object(table1, Bar, 256, 790)
    Table2 = Object(table1, Bar, 256 + table1.get_rect().size[0], 790)
    Table3 = Object(table1, Bar, 256 + table1.get_rect().size[0] * 2, 790)
    for elt in (Mur1, Mur2, Mur3, Mur4, Horloge, Tele, Buffet, Comptoir1, Comptoir2, Comptoir3, Comptoir4, Tabouret,
                Table1, Table2, Table3):
        Bar.addFurnitures(elt)
    Falo = PNJ(230, 366, Pops.speed, Bar, frontfalo, frontfalo, rightfalo, leftfalo,
               frontfalo, rightfalo, leftfalo, frontfalo, frontfalo, frontfalo, frontfalo, frontfalo, frontfalo
               , frontfalo, bouncefalo, bouncefalo, bouncefalo)
    # initialize the pygame module
    pygame.init()
    # On initialise le son (si jamais)
    pygame.mixer.init()

    startScrollingX = option.mw
    startScrollingY = option.mh

    # active le module de texte
    pygame.font.init()

    # La police d'écriture du jeu
    font = pygame.font.Font("VCR_OSD_MONO_1.001.ttf", 34)
    otherfont = pygame.font.Font("VCR_OSD_MONO_1.001.ttf", 150)

    # define a variable to control the main loop
    running = True

    # Objet qui permet de contrôler le nombre de frame et le temps
    clock = pygame.time.Clock()

    Menu = Handler()
    Fading = Handler()
    Game = Handler()
    Scrolling = Handler()
    Scrolling.stateEvent = True
    ScrollingX = Handler()
    ScrollingY = Handler()
    ScrollingX.stateEvent = True
    ScrollingY.stateEvent = True
    Intro = Handler()
    Intro.stateEvent = True

    save = {"paramètres": option, "joueur": Pops}
    nb_dialogue = 0
    position = 0
    compteur = 0
    time1 = 0

    # définiton d'une fonction pour le menu principal au lancement du jeu
    def game_intro(position, compteur, time1, events):
        text1 = font.render("Un jeu pas réalisé par Hideo Kojima", False, white)
        text2 = font.render("et par Yoko Taro, Masahiro Sakurai, et encore moins David Cage", False, white)
        Input = False

        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.unicode == 'z':
                    Input = True
                else:
                    Input = False
                if event.key == pygame.K_LEFT:
                    position -= 1
                elif event.key == pygame.K_RIGHT:
                    position += 1

        if not Input and compteur == 0:
            compteur = fadetoblack(5, screen, [],
                                   [(text1, 370,
                                     380)], Fading,
                                   Menu, compteur)
            if compteur == 1:
                time1 = pygame.time.get_ticks()
        elif Input and compteur == 0:
            fade.set_alpha(255)
            bisfade.set_alpha(0)
            compteur += 1
            screen.fill(black)

        elif istime(time1, 1) and compteur == 1:
            compteur = fadetoblack(5, screen, [(text1, 370, 380)], [(text2, 10, 380)], Fading,
                                   Menu, compteur)

            if compteur == 2:
                time1 = pygame.time.get_ticks()
        elif Input and compteur == 1:
            fade.set_alpha(255)
            bisfade.set_alpha(0)
            compteur += 1
            screen.fill(black)
        elif istime(time1, 1) and compteur == 2:
            compteur = fadetoblack(5, screen, [(text2, 10, 380)],
                                   [(font.render("Lancer jeu", False, white), 800, 400),
                                    (font.render("Commencer", False, white), 400, 400)], Game,
                                   Menu, compteur)
        elif Input and compteur == 2:
            fade.set_alpha(255)
            bisfade.set_alpha(0)
            compteur += 1
            screen.fill(black)
        if compteur == 3:
            Fading.stateEvent = True

        if compteur == 3 and Menu.stateEvent and Intro.stateEvent:
            menu(font, otherfont, position, Input)

        if Fading.stateEvent and not Menu.stateEvent:
            fadetoblack(5, screen, [(font.render("Lancer jeu", False, yellow), 800, 400),
                                    (font.render("Commencer", False, white), 400, 400)],
                        [Bar, *decor, Pops], Fading, Menu, compteur)
            if not Fading.stateEvent:
                Intro.stateEvent = False
        return position, compteur, time1

    def menu(font, otherfont, position, touch):
        position %= 1
        screen.fill(black)
        maintitle = otherfont.render("RedBlaze", True, white)
        # remplir le fond de la couleur
        hitbox_lancerjeu = pygame.Rect(800, 400, 200, 50)
        hitbox_commencer = pygame.Rect(400, 400, 200, 50)
        mousepos = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()[0]
        if hitbox_lancerjeu.collidepoint(mousepos[0], mousepos[1]):
            screen.blit(maintitle, (10, 10))
            screen.blit(font.render("Lancer jeu", False, yellow), (800, 400))
            screen.blit(font.render("Commencer", False, white), (400, 400))
            if click:
                Fading.stateEvent = True
                Menu.stateEvent = False
        elif hitbox_commencer.collidepoint(mousepos[0], mousepos[1]):
            screen.blit(maintitle, (10, 10))
            screen.blit(font.render("Lancer jeu", False, white), (800, 400))
            screen.blit(font.render("Commencer", False, yellow), (400, 400))
            if click:
                Fading.stateEvent = True
                Menu.stateEvent = False

        else:
            screen.blit(maintitle, (10, 10))
            screen.blit(font.render("Lancer jeu", False, white), (800, 400))
            screen.blit(font.render("Commencer", False, white), (400, 400))
        pygame.display.update()
        # def d'une fonction qui permet de faire un fondu en noir

    def fadetoblack(speed, screen, ancient, new, event, bisevent, compteur):
        nonlocal fade, bisfade
        if fade.get_alpha() >= 255 and bisfade.get_alpha() <= 0:
            fade.set_alpha(0)
            bisfade.set_alpha(255)
        if fade.get_alpha() < 255:
            for elt in ancient:
                if isinstance(elt, (Scene, Object)):
                    elt.draw(screen)
                elif isinstance(elt, Chara):
                    elt.standing(screen)
                else:
                    screen.blit(elt[0], (elt[1], elt[2]))
            screen.blit(fade, (0, 0))

            # si la valeur alpha du noir est en dessous de 255

            fade.set_alpha(fade.get_alpha() + speed)

            # on  active le processus inverse
        # si processus inverse activé
        elif bisfade.get_alpha() > 0 and fade.get_alpha() >= 255:

            # on baisse alpha
            for elt in new:
                if isinstance(elt, (Scene, Object)):
                    elt.draw(screen)
                elif isinstance(elt, Chara):
                    elt.standing(screen)
                else:
                    screen.blit(elt[0], (elt[1], elt[2]))
            screen.blit(bisfade, (0, 0))

            bisfade.set_alpha(bisfade.get_alpha() - speed)
            # si alpha est égale à 0
            if bisfade.get_alpha() <= 0:
                # on désactive le processus
                Fading.stateEvent = False
                event.stateEvent = False
                bisevent.stateEvent = True
                compteur += 1
                fade.set_alpha(0)
                bisfade.set_alpha(255)
        pygame.display.update()
        return compteur

    # définition de la fonction du jeu principal
    def controles(level, chara):
        global velX, velY
        pygame.event.set_allowed(pygame.KEYDOWN)
        # On associe keys pour gérer les touches plus efficacement
        key = pygame.key.get_pressed()

        # Commandes
        # Si les commandes sont activées
        if chara.commande_get():
            if key[pygame.K_UP] and key[pygame.K_RIGHT]:
                chara.VelX = chara.speed
                chara.VelY = -chara.speed
            elif key[pygame.K_RIGHT] and key[pygame.K_DOWN]:
                chara.VelX = chara.speed
                chara.VelY = chara.speed
            # Gauche
            if key[pygame.K_LEFT]:
                chara.x -= chara.speed
                chara.VelX = -chara.speed
                chara.set_left()  # permet de figer le perso dans la dernière pose qu'il faisait
                # Si jamais d'autres touches sont pressées
                # Bas
                if key[pygame.K_DOWN]:
                    chara.y += chara.speed
                    chara.VelY = chara.speed
                    chara.set_front()
                    chara.VelY = chara.speed
                # Haut
                elif key[pygame.K_UP]:
                    chara.y -= chara.speed
                    chara.set_back()
                    chara.VelY = -chara.speed
                chara.walk = True
            # Droite
            elif key[pygame.K_RIGHT]:
                chara.x += chara.speed
                chara.VelX = chara.speed
                chara.set_right()  # Aussi
                if key[pygame.K_DOWN]:
                    chara.y += chara.speed
                    chara.velY = chara.speed
                    chara.set_front()

                # Haut
                elif key[pygame.K_UP]:
                    chara.y -= chara.speed
                    chara.velY = -chara.speed
                    chara.set_back()
                chara.walk = True
            # Bas
            elif key[pygame.K_DOWN]:
                chara.y += chara.speed
                chara.VelY = chara.speed
                chara.set_front()
                chara.walk = True
            # Haut
            elif key[pygame.K_UP]:
                chara.y -= chara.speed
                chara.VelY = -chara.speed
                chara.set_back()
                chara.walk = True
            else:
                chara.walk = False

            if not key[pygame.K_RIGHT] and not key[pygame.K_LEFT]:
                chara.VelX = 0
            if not key[pygame.K_DOWN] and not key[pygame.K_UP]:
                chara.VelY = 0
            # Scrolling horizontal
            if chara.x < startScrollingX:
                chara.cameraX = chara.x
                level.PosX = level.initialPosX

            elif chara.x > level.lengthX - startScrollingX:
                chara.cameraX = chara.x - level.lengthX + option.w

            elif chara.x >= startScrollingX:
                chara.cameraX = startScrollingX
                if Scrolling.stateEvent:
                    if ScrollingX.stateEvent:
                        if key[pygame.K_LEFT]:
                            velX = -chara.speed
                        elif key[pygame.K_RIGHT]:
                            velX = chara.speed
                        else:
                            velX = 0
                        level.PosX -= velX
                        while level.PosY % chara.speed != 0:
                            level.PosY -= 1

            if chara.y > startScrollingY:
                chara.cameraY = chara.y
                level.PosY = level.initialPosY
            elif level.initialPosY < chara.y < level.initialPosY + startScrollingY:
                chara.cameraY = chara.y - level.initialPosY
            else:
                chara.cameraY = startScrollingY
                if Scrolling.stateEvent:
                    if ScrollingY.stateEvent:
                        if key[pygame.K_UP]:
                            velY = -chara.speed
                        elif key[pygame.K_DOWN]:
                            velY = chara.speed
                        else:
                            velY = 0
                        level.PosY -= velY
                        while level.PosY % chara.speed != 0:
                            level.PosY -= 1
        else:
            chara.walk = False
            Scrolling.stateEvent = False
        while chara.x % chara.speed != 0:
            chara.x -= 1
        while chara.y % chara.speed != 0:
            chara.y -= 1
        for elt in pnj:
            elt.update()

    # fonction qui permet d'afficher la carte
    def printlevel(level):
        level.draw(screen)
        decor = pygame.sprite.Group(*pnj, *level.furnitures)

        for chara in player:
            chara.collision(decor, Scrolling, ScrollingX, ScrollingY)

        for elt in decor:
            for chara in player:
                if elt.rect.center[1] <= chara.downrect.top:
                    if isinstance(elt, Object):
                        elt.draw(screen)
                    else:
                        elt.standing(screen)

        for chara in player:
            if chara.walk:
                chara.walking(screen)
            else:
                chara.standing(screen)

        for elt in decor:
            for chara in player:
                if elt.rect.center[1] >= chara.uprect.bottom:
                    if isinstance(elt, Object):
                        elt.draw(screen)
                    else:
                        elt.standing(screen)

    # boucle principale
    while running:

        # Je bloque tous les évenements avec la souris car ils m'ont bien fait chier
        clock.tick_busy_loop(60)  # contrôle le nombre de frame du jeu
        characters = pygame.sprite.Group(Pops, Falo)
        pnj = pygame.sprite.Group(Falo)
        player = pygame.sprite.Group(Pops)
        decor = pygame.sprite.Group(*pnj, *Bar.furnitures)
        # event handling, gets all event from the event queue
        events = pygame.event.get()
        for event in events:
            # only do something if the event is of type QUIT
            if event.type == pygame.QUIT:
                # change the value to False, to exit the main loop
                running = False
            # Si une touche est pressée ...
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_F4:
                    screen = option.dimension(screen)
                for sprite in characters:
                    if sprite.detection and event.type == pygame.KEYDOWN and event.unicode == "z":
                        sprite.set_dialogue(True)
                        Scrolling.stateEvent = False
                    if event.key == pygame.K_ESCAPE:
                        running = False

        if Intro.stateEvent:
            position, compteur, time1 = game_intro(position, compteur, time1, events)
        else:
            Game.stateEvent = True
            Fading.stateEvent = False

        if Game.stateEvent:

            if Pops.commande_get():
                controles(Bar, Pops)
            # puis on affiche le sprite
            screen.fill(black)
            printlevel(Bar)

            # si on actives les dialogues
            if Pops.dialogue_get():
                Scrolling.stateEvent = False
                if Pops.informationDetection in (Table1.rect, Table3.rect, Table2.rect):
                    if nb_dialogue == 0:
                        nb_dialogue = animation_text("Une simple banquette rouge avec une table.", screen, Pops,
                                                     dialogue_box, curseur, nb_dialogue, 4, None, events)
                    elif nb_dialogue == 1:
                        nb_dialogue = animation_text("... Hein ? Pourquoi des tasses sont servies s'il y a personne ?"
                                                     + " \n "
                                                     + "En plus elles sont vides ...", screen, Pops, dialogue_box,
                                                     curseur, nb_dialogue, 4, None, events)
                    elif nb_dialogue == 2:
                        nb_dialogue = animation_text("Que c'est stupide.", screen, Pops, dialogue_box, curseur,
                                                     nb_dialogue, 4, None, events)
                    elif nb_dialogue == 3:
                        nb_dialogue = animation_text("...", screen, Pops, dialogue_box, curseur, nb_dialogue, 4,
                                                     "dubitatif", events)
                elif Pops.informationDetection == Falo.rect:
                    if Pops.right:
                        Falo.set_left()
                    elif Pops.left:
                        Falo.set_right()
                    elif Pops.back:
                        Falo.set_front()

                    if nb_dialogue == 0:
                        nb_dialogue = animation_text("t un panda", screen, Falo, dialogue_box, curseur, nb_dialogue,
                                                     2, "bounce", events)
                    elif nb_dialogue == 1:
                        nb_dialogue = animation_text("eh beh c'est sympa", screen, Pops, dialogue_box, curseur,
                                                     nb_dialogue, 2, "bounce", events)
                elif Pops.informationDetection == Comptoir1.rect:
                    if nb_dialogue == 0:
                        nb_dialogue = animation_text("Le portrait d'une tête de télé pédante.", screen, Pops,
                                                     dialogue_box, curseur, nb_dialogue, 3, None, events)
                    elif nb_dialogue == 1:
                        nb_dialogue = animation_text("Tu l'as déjà vu quelque part ...", screen, Pops, dialogue_box,
                                                     curseur, nb_dialogue, 3, None, events)
                    elif nb_dialogue == 2:
                        nb_dialogue = animation_text("En tout cas, sa tête ne te revient pas.", screen, Pops,
                                                     dialogue_box, curseur, nb_dialogue, 3, None, events)
            else:
                nb_dialogue = 0
        # puis on met à jour l'écran
        pygame.display.update()
    pygame.quit()


# run the main function only if this module is executed as the main script
# (if you import this as a module then nothing is executed)
if __name__ == "__main__":
    # call the main function
    main()