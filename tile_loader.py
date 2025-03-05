from map import Tilekind
def Tile_loder():
        tile_kind = [
            Tilekind('grass', r'C:\Users\ravi4\OneDrive\Pictures\Saved Pictures\grass.jfif', False),
            Tilekind('grass_stare', r'C:\Users\ravi4\OneDrive\Pictures\Saved Pictures\grass_stare.jpg', False),
            Tilekind('grass_stone', r'C:\Users\ravi4\OneDrive\Pictures\Saved Pictures\grass_stone.jpg', False),
            Tilekind('stare', r'C:\Users\ravi4\OneDrive\Pictures\Saved Pictures\stare.jfif', True),
            Tilekind('stone', r'C:\Users\ravi4\OneDrive\Pictures\Saved Pictures\stone.jpg', False)
        ]
        return tile_kind
