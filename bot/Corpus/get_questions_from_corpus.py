import json
import sys
import os

def get_questions(corpus_path, corpus_name=None, label=1):
	corpus = json.load(open(corpus_path))
	if not corpus_name:
		# get name of file without extension
		corpus_name = corpus_path.split('/')[-1].split('.')[0]
	training_data = []
	for couple in corpus[corpus_name]:
		training_data.append((couple[0],label))
	return training_data

if __name__ == '__main__':
	if(len(sys.argv) > 3):
		if not os.path.isfile(sys.argv[1]):
			raise ValueError('%s is not a correct file path' % sys.argv[1])
		else:
			print get_questions(sys.argv[1], corpus_name = sys.argv[2], label = sys.argv[3])
	elif(len(sys.argv) > 2):
		if not os.path.isfile(sys.argv[1]):
			print ValueError('%s is not a correct file path' % sys.argv[1])
		else:
			print get_questions(sys.argv[1], corpus_name = sys.argv[2])
	elif(len(sys.argv)>1):
		if sys.argv[1]=='help':
			print 'python get_questions_from_corpus.py corpus_path [corpus_name] [label]'
		elif not os.path.isfile(sys.argv[1]):
			print ValueError('%s is not a correct file path' % sys.argv[1])
		else:
			print get_questions(sys.argv[1])
	else:
		print ValueError('Input is wrong : python get_questions_from_corpus.py corpus_path [corpus_name] [label]')