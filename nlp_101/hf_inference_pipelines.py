from transformers import pipeline

transcriber = pipeline(taks='text-classification', model='facebook/bart-large-mnli', device=0)

if __name__ == '__main__':
    print(transcriber('This is a test message'))
    print(transcriber('This is a test message')['label'])


