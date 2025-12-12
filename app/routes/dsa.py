# app/routes/dsa.py
from fastapi import APIRouter
from app.services.dsa_service import stack, queue, linked_list, hash_table

router = APIRouter(prefix="/dsa", tags=["DS&A"])

# Stack endpoints
@router.post("/stack/push")
def push_stack(item: str):
    stack.push(item)
    return {"stack": stack.to_list()}

@router.post("/stack/pop")
def pop_stack():
    return {"popped": stack.pop(), "stack": stack.to_list()}

# Queue endpoints
@router.post("/queue/enqueue")
def enqueue_queue(item: str):
    queue.enqueue(item)
    return {"queue": queue.to_list()}

@router.post("/queue/dequeue")
def dequeue_queue():
    return {"dequeued": queue.dequeue(), "queue": queue.to_list()}

# Linked List endpoints
@router.post("/linkedlist/insert")
def insert_linkedlist(value: str):
    linked_list.insert(value)
    return {"linked_list": linked_list.to_list()}

# Hash Table endpoints
@router.post("/hashtable/put")
def put_hashtable(key: str, value: str):
    hash_table.put(key, value)
    return {"hash_table": hash_table.to_dict()}

@router.get("/hashtable/get")
def get_hashtable(key: str):
    return {"value": hash_table.get(key)}

@router.delete("/hashtable/delete")
def delete_hashtable(key: str):
    return {"deleted": hash_table.delete(key), "hash_table": hash_table.to_dict()}