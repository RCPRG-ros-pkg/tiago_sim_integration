# tiago_sim_integration
Pliki integracyjne symulatora Tiago

# Integracja z symulatorem
## Świat
Świat gazebo tego repozytorium znajduje się w
```
/gazebo_ws/worlds
```

Odpowiedni świat należy umieścić w katalogu symulatora Tiago:
```
/tiago_public_ws/src/tiago_simulation/tiago_gazebo/worlds
```

## Launch
Pliki launch należy umieścić w katalogu symulatora Tiago pod tą samą ścieżką:
```
/tiago_sim_integration/tiago_simulation/tiago_2dnav_gazebo/launch
```

## Modele obiektów
Wszystkie modele znajdują się w katalogach
```
/blender_ws
```
Modele robocze i wyeksportowane elementy w formacie .dae utworzone na potrzeby świata laboratorium.


```
/gazebo_ws
```
Modele zaciągnięte z Blendera z dodatkiem opisu .sdf. Gotowe do wykorzystania elementy w budowie świata gazebo.


```
/sweet_home_ws
```
Model laboratorium z wyeksportowanymi modelami pojedynczych elementów w formacie .obj (nietolerowany przez gazebo format).
