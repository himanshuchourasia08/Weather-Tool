from transformers import pipeline

classifier=pipeline("zero-shot-classification")

labels=['politics','sports','technology','food','movies','cinema','bollywood']

text="Rohit Sharma"

result=classifier(text,candidate_labels=labels)

print("Top Label:",result['labels'][0])
print("Scores :",list(zip(result['labels'],result['scores'])))