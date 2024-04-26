#! /bin/bash

echo "Lancement PouleRenardVipere..."

#python3 ./Sources/main.py

echo "PouleRenardVipere fermé."
echo "Tracé des graphes d'évolution en cours..."

# graphes agents
python3 Sources/plotCSV-python3/plot.py --outputFilename "Graphes/evol_poules.pdf" -title "Evolution du nombre de poules" -xLabel "itérations" -xlimMin 0 -yLabel "nbPoules" -ylimMin 0 Graphes/evol_pop.csv 0 1 >/dev/null &
python3 Sources/plotCSV-python3/plot.py --outputFilename "Graphes/evol_renards.pdf" -title "Evolution du nombre de renards" -xLabel "itérations" -xlimMin 0 -yLabel "nbRenards" -ylimMin 0 Graphes/evol_pop.csv 0 2 >/dev/null &
python3 Sources/plotCSV-python3/plot.py --outputFilename "Graphes/evol_viperes.pdf" -title "Evolution du nombre de vipères" -xLabel "itérations" -xlimMin 0 -yLabel "nbViperes" -ylimMin 0 Graphes/evol_pop.csv 0 3 >/dev/null &

#graphes arbres
python3 Sources/plotCSV-python3/plot.py --outputFilename "Graphes/evol_arbres.pdf" -title "Evolution du nombre d'arbres" -xLabel "itérations" -xlimMin 0 -yLabel "nbArbres" -ylimMin 0 Graphes/evol_arbre.csv 0 1 >/dev/null &
python3 Sources/plotCSV-python3/plot.py --outputFilename "Graphes/evol_arbres_feu.pdf" -title "Evolution du nombre d'arbres en feu" -xLabel "itérations" -xlimMin 0 -yLabel "nbArbresFeu" -ylimMin 0 Graphes/evol_arbre.csv 0 2 >/dev/null

wait

echo "Les graphes ont été tracés."
echo "Au revoir"
