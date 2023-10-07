import sys
import pickle
import joblib
import re # Regex Library

def load_model():
	with open("./models/vectorizer_tfidf-os.pickle", "rb") as input_file:
		vectorizer = pickle.load(input_file)

	loaded_model = joblib.load('./models/SA_NLP_Model-os.joblib')
	
	return vectorizer, loaded_model

def main():
	args = sys.argv[1:]
	
	with open('./demo/review.txt') as f:
		lines = f.readlines()
	print('The input text is: ', lines[0])
		
	vec, model = load_model()
	
	test_vec = vec.transform(lines)
	
	print('The predicted sentiment is:', model.predict(test_vec)[0])
	return
        

if __name__ == "__main__":
 	main()
