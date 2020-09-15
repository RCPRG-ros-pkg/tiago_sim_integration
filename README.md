# tiago_sim_integration
Repozytorium integracyjne symulatora Tiago

# Integracja z symulatorem
## Świat i modele
Świat gazebo tego repozytorium znajduje się w
```
/worlds
```
Modele mebli są w
```
/models
```
Świat jest wczytywany w pliku launch:
```
roslaunch tiago_sim_integration tiago_navigation_public_012.launch
```
Ten launch dodaje ścieżkę do folderu models, aby gazebo wyświetlało meble.

## Modele obiektów
Wszystkie modele znajdują się w katalogach:
```
/blender_ws
```
Modele robocze i wyeksportowane elementy w formacie .dae utworzone na potrzeby świata laboratorium.


---

```
/sweet_home_ws
```
Model laboratorium z wyeksportowanymi modelami pojedynczych elementów w formacie .obj (nietolerowany przez gazebo format).

---
