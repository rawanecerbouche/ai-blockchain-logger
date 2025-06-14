from blockchain import Blockchain
from model import AIModel
from random import choice
import time
import json


model = AIModel()
chain = Blockchain()


sample_inputs = [
    [5.1, 3.5, 1.4, 0.2],
    [6.7, 3.0, 5.2, 2.3],
    [5.9, 3.0, 4.2, 1.5],
    [4.9, 2.5, 4.5, 1.7]
]


for _ in range(3):
    data = choice(sample_inputs)
    result = model.predict(data)
    result["timestamp"] = time.strftime('%Y-%m-%d %H:%M:%S')
    
    
    chain.add_block(result)


print("\n--- Blockchain Ledger ---\n")
for block in chain.chain:
    print(json.dumps({
        "index": block.index,
        "timestamp": block.timestamp,
        "data": block.data,
        "previous_hash": block.previous_hash,
        "hash": block.hash
    }, indent=4))

