"""
Mini Feature Store (KV + version)
Goal: Store/retrieve feature snapshots by (entity_key, version).
"""
from collections import defaultdict
import heapq
class FeatureStore:
    def __init__(self):
        self.store = defaultdict(list)
        self.version_store = defaultdict(list)
        """
        TODO: init an internal dict, e.g. {(key, version): features_dict}
        """
        # TODO
        pass

    def put(self, key, features: dict, version: int) -> None:
        self.store[(key,version)].append(features)
        heapq.heappush(self.version_store[key],-version)
        return
        """
        Store features for (key, version).
        - key: str | int
        - features: dict of feature_name -> value
        - version: int (e.g., timestamp-based or semantic)
        """
        # TODO
        pass

    def get(self, key, version: int):
        if (key, version) in self.store:
            return self.store[(key,version)]
        return None
        """
        Retrieve features for (key, version).
        Return None if not found.
        """
        # TODO
        pass

    def latest(self, key):
        if key in self.version_store:

            l_k = heapq.heappop(self.version_store[key])
            return (key,-l_k)
        return None
        
        """
        (Optional) Return (version, features) with the highest version for key.
        If none, return None.
        """
        # TODO
        pass


if __name__ == "__main__":
    fs = FeatureStore()
    # EXPECTED USAGE (after implementation):
    fs.put("cam_001", {"motion_rate": 0.12, "brightness": 0.8}, version=1)
    fs.put("cam_001", {"motion_rate": 0.15, "brightness": 0.75}, version=2)
    print(fs.get("cam_001", 1))
    print(fs.latest("cam_001"))
