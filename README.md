# Implementacja i porównanie wydajności BFS i DFS w przeszukiwaniu grafów o różnej strukturze

## Wstęp

Celem projektu jest zaimplementowanie algorytmów BFS i DFS w języku Python oraz porównanie ich wydajności w przeszukiwaniu grafów o różnej strukturze. W projekcie wykorzystano bibliotekę NetworkX do generowania grafów o różnej strukturze.

## Opis implementacji

Projekt składa się z trzech plików:
- `main.py` - plik zawierający implementację algorytmów BFS i DFS oraz funkcje pomocnicze do generowania grafów
- `bfs_vs_dfs.py` - plik zawierający funkcje do porównania wydajności algorytmów BFS i DFS
- `test.py` - plik zawierający testy jednostkowe
- `requirements.txt` - plik zawierający zależności projektu
- `README.md` - plik zawierający opis projektu

## DFS (Depth First Search)

Algorytm DFS polega na przeszukiwaniu grafu w głąb. W każdym kroku wybierany jest wierzchołek, który nie został jeszcze odwiedzony i rekurancyjnie odwiedzane są wszystkie wierzchołki sąsiednie. Algorytm DFS jest implementowany za pomocą stosu.

## BFS (Breadth First Search)

Algorytm BFS polega na przeszukiwaniu grafu wszerz. W każdym kroku odwiedzane są wszystkie wierzchołki sąsiednie, a następnie przechodzimy do odwiedzenia wierzchołków sąsiednich dla wierzchołków odwiedzonych w poprzednim kroku. Algorytm BFS jest implementowany za pomocą kolejki.

## Instalacja

Najpierw należy się upewnić, że mamy zainstalowanego Dockera. Następnie należy sklonować repozytorium i uruchomić poniższe komendy:

```bash
docker build -t fastapi-app .
docker run -d -p 8000:8000 fastapi-app
```

Aplikcaja będzie dostępna pod adresem `http://127.0.0.1:8000/`.

Dokumentacja API dostępna jest pod adresem `http://127.0.0.1:8000/docs`.
