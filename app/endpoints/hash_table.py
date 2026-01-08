from fastapi import APIRouter
from pydantic import BaseModel

# Define request schema
class HashTableRequest(BaseModel):
    operations: list  # List of operations, e.g. [{"op":"insert","key":"a","value":1}, {"op":"get","key":"a"}]

# Simple Hash Table implementation
class HashTable:
    def __init__(self):
        self.table = {}

    def insert(self, key, value):
        self.table[key] = value
        return f"Inserted {key}:{value}"

    def get(self, key):
        return self.table.get(key, None)

    def delete(self, key):
        if key in self.table:
            del self.table[key]
            return f"Deleted {key}"
        return f"{key} not found"

# Create router
router = APIRouter()

@router.post("/ds/hash_table")
def hash_table_demo(req: HashTableRequest):
    """
    Perform a sequence of hash table operations.
    """
    ht = HashTable()
    results = []

    for op in req.operations:
        if op["op"] == "insert":
            results.append(ht.insert(op["key"], op["value"]))
        elif op["op"] == "get":
            results.append(ht.get(op["key"]))
        elif op["op"] == "delete":
            results.append(ht.delete(op["key"]))
        else:
            results.append(f"Unknown operation: {op['op']}")

    return {"results": results, "final_table": ht.table}