def scramble(seq):
	for i in range(len(seq)):
		seq=seq[1:]+seq[:1]
		yield seq
scramble2=lambda seq:(seq[1:]+seq[:1] for i in range(len(seq)))
	
