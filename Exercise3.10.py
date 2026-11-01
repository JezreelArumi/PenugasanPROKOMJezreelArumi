# 3.10 Every Function
# A list of beaches, using every list function from this chapter.
beaches = ['Lovina', 'Gunung Payung', 'Kelingking', 'Maldives']
print(f"Starting list: {beaches}")

beaches[0] = 'k2'                       # modify an element
print(f"Changed the first item:    {beaches}")

beaches.append('matterhorn')            # append
print(f"After append():            {beaches}")

beaches.insert(1, 'elbrus')             # insert
print(f"After insert():            {beaches}")

del beaches[2]                          # del
print(f"After del beaches[2]:    {beaches}")

popped_beach = beaches.pop()         # pop
print(f"After pop():               {beaches} (popped {popped_beach})")

beaches.remove('fuji')                  # remove by value
print(f"After remove('fuji'):      {beaches}")

print(f"sorted() view:             {sorted(beaches)}")
print(f"Original is unchanged:     {beaches}")

beaches.sort()                          # sort
print(f"After sort():              {beaches}")

beaches.reverse()                       # reverse
print(f"After reverse():           {beaches}")

print(f"Length with len():         {len(beaches)}")
print(f"Last item with index -1:   {beaches[-1]}")