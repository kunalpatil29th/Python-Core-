# database_sharding_sim.py

"""
Definition: Database Sharding is a type of database partitioning that separates very large databases into smaller, faster, more easily managed parts called data shards.
"""

class ShardManager:
    def __init__(self, shards):
        self.shards = shards

    def get_shard(self, user_id):
        # Sharding logic based on user ID
        shard_idx = user_id % len(self.shards)
        return self.shards[shard_idx]

# Usage
manager = ShardManager(["DB_Shard_A", "DB_Shard_B"])
for user_id in [101, 102, 103, 104]:
    print(f"User {user_id} data stored in: {manager.get_shard(user_id)}")
