input(); english = set(map(int,raw_input().split())); input(); french = set(map(int,raw_input().split()))
print len(english.symmetric_difference(french))