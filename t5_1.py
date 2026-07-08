from transformers import pipeline

summarize=pipeline("summarization",model="t5-small")

long_text="Artificial intelligence has become one of the most influential technologies of the modern era"\
"Organizations around the world are investing heavily in AI research and development."\
"Machine learning, a subset of artificial intelligence, enables computers to learn patterns from data without being explicitly programmed"\
"Deep learning models have achieved remarkable success in fields such as computer vision, natural language processing, and speech recognition."

summary=summarize(long_text,max_length=50,min_length=25)
print(summary[0]['summary_text'])