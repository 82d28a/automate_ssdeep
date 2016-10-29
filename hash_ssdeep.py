import ssdeep
import collections
import pickle


MIN_FLOOR_SIMILARITY_SCORE = 0


def fuzzy_hash_file(filepath):
    return ssdeep.hash_from_file(filepath)

def default_dict():
    return collections.defaultdict(int)

def open_dict(type):
    try:
        with open("known_{}.store".format(type), "rb") as rfile:
            _temp = rfile.read()
            rfile.seek(0)
            if len(_temp) > 0:
                # return default dict
                return pickle.load(rfile)
            else:
                # create dict
                return collections.defaultdict(default_dict)
    except IOError:
        # create dict
        return collections.defaultdict(default_dict)

def save_dict(type, store):
    with open("known_{}.store".format(type), "wb") as writefile:
        # return default dict
        return pickle.dump(store, writefile)

def dump_hash_file(type, store_dict):
    HEADER = "ssdeep,1.1--blocksize:hash:hash,filename\n"
    with open("known_{}.csv".format(type), "wb") as writefile:
        writefile.write(HEADER)
        for hash in store_dict:	
            for filename in store_dict[hash]:
                writefile.write('{},"{}"\n'.format(hash, filename))

def compare_hashs(hash_a, dict_hashes):
    for hash_b in dict_hashes:
        match_score = ssdeep.compare(hash_a, hash_b)
        if match_score > MIN_FLOOR_SIMILARITY_SCORE:
            print("{}% match(s) to {}".format(match_score, ", ".join([file for file in dict_hashes[hash_b]])))