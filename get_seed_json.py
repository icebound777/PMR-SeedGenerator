import json
import sys

import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

# Dumps the data for a seed in DB to a json file, with the SeedID as name
# Requires you to have the service_account.json DB key in the same folder
# Usage: To get JSON for SeedID 12345: >python get_seed_json.py 12345
def main(seed_id):
    cred = credentials.Certificate('service_account.json')
    firestore_seeds_collection = "seeds-prod"
    
    firebase_admin.initialize_app(cred)
    db = firestore.client()

    document =  db.collection(firestore_seeds_collection).document(seed_id).get()
    if not document.exists:
        raise Exception(f"No Document with SeedID: {seed_id} was found in collection: {firestore_seeds_collection}")

    result = document.to_dict()
            
    with open(f"{seed_id}.json", 'w', encoding='utf-8') as f:
        json.dump(result, f, ensure_ascii=False, indent=4, default=str, sort_keys=True)


if __name__ == "__main__":
    if(len(sys.argv) < 2):
        raise Exception("A seed ID must be provided as an argument to the script")
    main(sys.argv[1])