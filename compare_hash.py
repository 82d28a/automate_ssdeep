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
                hash_ssdeep.compare_hashs(filepath, file_hash, hash_store)
        except IOError:
            print("{} File(s) or path are invalid.".format(list_target_files))
    else:
        print("{} <hash store name> <file(s) to hash and compare with hash store>".format(sys.argv[0]))
