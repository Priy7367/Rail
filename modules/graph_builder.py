import pandas as pd
import networkx as nx

def build_graph_from_howrah_csv(howrah_csv_path, data_csv_path):
    """
    Builds a railway network graph from Howrah Eastern schedule and train frequency data
    
    Args:
        howrah_csv_path: Path to Howrah Eastern schedule CSV
        data_csv_path: Path to train frequency data CSV
    
    Returns:
        NetworkX graph representing the railway network
    """
    # Load datasets
    schedule_df = pd.read_csv(howrah_csv_path)
    frequency_df = pd.read_csv(data_csv_path)
    
    # Create directed graph
    G = nx.DiGraph()
    
    # Add nodes from schedule data
    stations = set()
    for col in schedule_df.columns[1:]:
        for station in schedule_df[col]:
            if isinstance(station, str) and station.strip():
                stations.add(station.split('(')[0].strip())
    
    for station in stations:
        G.add_node(station, type="station")
    
    # Add edges from frequency data
    for _, row in frequency_df.iterrows():
        station1 = row['Station1'].strip()
        station2 = row['Station2'].strip()
        distance = row['Int_Dist_Kms']
        
        # Get hourly frequencies (columns 4 to 27)
        frequencies = row[4:28].tolist()
        avg_frequency = sum(frequencies) / len(frequencies) if frequencies else 0
        
        # Add edge with attributes
        G.add_edge(
            station1, 
            station2,
            distance=distance,
            frequencies=frequencies,
            avg_frequency=avg_frequency,
            train_type="Express" if avg_frequency > 5 else "Passenger"
        )
    
    # Add connections from schedule data
    for _, row in schedule_df.iterrows():
        current_station = None
        
        for col_idx, col_name in enumerate(schedule_df.columns[1:]):
            station_info = row[col_name]
            if not isinstance(station_info, str) or not station_info.strip():
                continue
                
            # Extract station name and time
            station_name = station_info.split('(')[0].split(')')[0].strip()
            
            # Skip generic stations
            if "Jn" not in station_name and "Station" not in station_name:
                continue
                
            # Connect stations in sequence
            if current_station and current_station in G and station_name in G:
                if not G.has_edge(current_station, station_name):
                    # Approximate distance for intermediate stations
                    G.add_edge(
                        current_station, 
                        station_name,
                        distance=50,  # Default approximation
                        frequencies=[0]*24,
                        avg_frequency=0,
                        train_type="Passenger"
                    )
            current_station = station_name
    
    return G