# graph/backtracking.py


class Graph():  
    def __init__(self):  
        pass
    
    def hamilton(self, G, size, pt, path=[]):
        print('hamilton called with pt={}, path={}'.format(pt, path))
        if pt not in set(path):
            path.append(pt)
            if len(path)==size:
                return path
            for pt_next in G.get(pt, []):
                res_path = [i for i in path]
                candidate = self.hamilton(G, size, pt_next, res_path)
                if candidate is not None:  # skip loop or dead end
                    return candidate
            print('path {} is a dead end'.format(path))
        else:
            print('pt {} already in path {}'.format(pt, path))
        # loop or dead end, None is implicitly returned
