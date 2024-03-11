import heapq

def dijkstra(graph, start, end):
    # Inicializamos las distancias con infinito para todos los nodos excepto el nodo de inicio
    distances = {node: float('infinity') for node in graph}
    distances[start] = 0
    
    # Creamos una cola de prioridad usando un heap
    priority_queue = [(0, start)]
    
    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)
        
        # Si la distancia actual es mayor que la conocida, continuamos
        if current_distance > distances[current_node]:
            continue
        
        # Actualizamos las distancias para los vecinos del nodo actual
        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight
            
            # Si encontramos una distancia más corta, actualizamos
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))
    
    # La distancia mínima desde el inicio hasta el final
    shortest_distance = distances[end]
    
    # Reconstruimos el camino desde el inicio hasta el final
    path = [end]
    current_node = end
    while current_node != start:
        for neighbor, weight in graph[current_node].items():
            if distances[current_node] == distances[neighbor] + weight:
                path.append(neighbor)
                current_node = neighbor
                break
    
    # Invertimos el camino para que sea desde el inicio hasta el final
    path.reverse()
    
    return shortest_distance, path

# Ejemplo de uso
if __name__ == "__main__":
    # Definimos un grafo de ejemplo (mapa de carreteras)
    road_map = {
        'Inicio': {'A': 2, 'B': 4},
        'A': {'Fin': 3},
        'B': {'A': 1, 'Fin': 5},
        'Fin': {}
    }
    
    start_location = 'Inicio'
    end_location = 'Fin'
    
    # Aplicamos el algoritmo de Dijkstra
    distance, shortest_path = dijkstra(road_map, start_location, end_location)
    
    # Imprimimos los resultados
    print(f"La distancia más corta desde {start_location} hasta {end_location} es: {distance}")
    print(f"El camino más corto es: {shortest_path}")