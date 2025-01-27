cmake_minimum_required(VERSION 3.30)
project(PFR C)

set(CMAKE_C_STANDARD 11)

# Ajouter les fichiers de traitement d'images
file(GLOB IMAGE_SOURCES "fonction_traitement_image/*.c")
file(GLOB IMAGE_HEADERS "fonction_traitement_image/*.h")

# Définir les fichiers principaux pour chaque exécutable
set(MAIN_SOURCE "prancipal/main.c")          # Fichier principal pour le premier exécutable
set(MAIN_TI_SOURCE "fonction_traitement_image/main_ti.c")  # Fichier principal pour le second exécutable

# Créer l'exécutable pour main (prancipal)
add_executable(main ${MAIN_SOURCE})

# Créer l'exécutable pour main_ti (traitement d'images)
add_executable(main_ti ${MAIN_TI_SOURCE} ${IMAGE_SOURCES})

# Assurez-vous que les exécutables sont des applications console
set_target_properties(main PROPERTIES LINK_FLAGS "-mconsole")
set_target_properties(main_ti PROPERTIES LINK_FLAGS "-mconsole")
