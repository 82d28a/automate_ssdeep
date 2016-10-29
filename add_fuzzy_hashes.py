import hash_ssdeep
import sys
import collections


def default_dict():
    return collections.defaultdict(int)


if __name__=="__main__":
    if len(sys.argv) >= 3:
        list_target_files = [filename for filename in sys.argv[2:]]
        try:
            hash_store = hash_ssdeep.open_dict(sys.argv[1])
            for filepath in list_target_files:
                file_hash = hash_ssdeep.fuzzy_hash_file(filepath)
                hash_store[file_hash][filepath]=0
            hash_ssdeep.save_dict(sys.argv[1], hash_store)
            hash_ssdeep.dump_hash_file(sys.argv[1], hash_store)
        except IOError:
            print("File(s) or path are invalid.")
    else:
        print("{} <hash store name> <file(s) to add hash store>".format(sys.argv[0]))