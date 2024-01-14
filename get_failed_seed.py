import json
import sys

import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

from randomizer import main_randomizer

SEEDS_DEV = "seeds"
SEEDS_PROD = "seeds-prod"
SEEDS_FAIL_DEV = "seeds-fail"
SEEDS_FAIL_PROD = "seeds-fail-prod"

firestore_seed_collection = SEEDS_FAIL_DEV # Change this to fetch from different DB collection

# Regenerates a failed seed by id, or latest if no id provided. Failed seed is also saved as failed_seed.json
# Requires you to have the service_account.json DB key in the same folder
# Usage: To get JSON for SeedID 12345: >python get_failed_seed.py 12345. When the id is ommited, the latest seed will be fetched instead
def main(seed_id):
    cred = credentials.Certificate('service_account.json')
    
    firebase_admin.initialize_app(cred)
    db = firestore.client()

    if(seed_id is not None):
        document =  db.collection(firestore_seed_collection).document(seed_id).get()
        if not document.exists:
            raise Exception(f"No Document with SeedID: {seed_id} was found in collection: {firestore_failure_collection}")
    else:
        document =  db.collection(firestore_seed_collection).order_by("CreationDate", direction=firestore.Query.DESCENDING).limit(1).get()[0]
    
    seed_json = document.to_dict()
            
    with open(f"failed_seed.json", 'w', encoding='utf-8') as f:
        json.dump(seed_json, f, ensure_ascii=False, indent=4, default=str, sort_keys=True)

    main_randomizer(["-c", "failed_seed.json"])

if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else None)