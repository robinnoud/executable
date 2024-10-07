import pygame

pygame.init()

# Créer la fenêtre
fenetre = pygame.display.set_mode((500, 400))

# Modifier le titre de la fenêtre
pygame.display.set_caption("demo")

# charger une image
###image = pygame.image.load("genos_sprite.png")

# ajuster la taille d'une image
###image = pygame.transform.scale(image,(50,50))

# découper une image
###rect = pygame.Rect(x,y,length,heigth)
###img = image.subsurface(rect)

# supprimer une couleur d'une image
##img.set_colorkey((51,49,50))

# créer une écriture
ecriture = pygame.font.Font(None, 25) # type d'écriture, taille de police

# créer un texte
txt = ecriture.render("coucou",1,(0,255,0))

# création d'une horloge 
clock = pygame.time.Clock()

# définition des fps
fps = 60

# Boucle principale
running = True
while running:
    # Remplir la fenêtre de noir (RGB)
    fenetre.fill((0, 0, 0))

    # Dessiner un rectangle rouge (carré) sur la fenêtre
    carre_rouge = pygame.draw.rect(fenetre, (255, 0, 0), [10, 10, 50, 50])

    # Créer un Rect invisible 
    rect = pygame.Rect(100, 100, 25, 25)
    
    # affichier une image, un texte ...
    fenetre.blit(txt,(200,200))

    # Récupérer tous les événements tels que clic et clavier
    for event in pygame.event.get():
        # Tester si l'utilisateur essaie de fermer la fenêtre
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # Vérifier si la souris est sur le carré rouge lorsqu'on clique
            if carre_rouge.collidepoint(pygame.mouse.get_pos()): 
                print("Click sur le carré rouge")
        elif event.type == pygame.KEYDOWN:
           # Vérifier si la touche espace est préssé
           if event.key == pygame.K_ESCAPE:
               print("touche echap pressée")
           if event.key == pygame.K_SPACE:
               print("touche espace pressée")
    
    # application de x fps
    clock.tick(fps)
    
    # Actualiser la fenêtre
    pygame.display.flip()

# Fermer la fenêtre
pygame.quit()
