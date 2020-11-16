import spacy


nlp = spacy.load("en_trf_bertbaseuncased_lg")
paragraph = nlp("The National Motor Museum Trust The National Motor Museum Trust Home > Story of Motoring > Motoring Firsts Motoring Firsts Among  the questions we are most frequently asked are the various motoring firsts. Listed below are some of the most common questions that have been answered by our Motoring Research Service.Questions What were the first motor cars The motor car was developed over many years by a number of talented individuals but Karl Benz of Mannheim in Germany is normally credited as the Inventor of the Motor Car. In the autumn of 1885, his three-wheeled vehicle became the first successful petrol-engined car. He was awarded a patent for it on 29 January 1886, and became the first motor manufacturer in 1888 with his Modell 3 Benz. In 1886, Gottlieb Daimler and his protégé Wilhelm Maybach built the first successful four-wheeled petrol-driven car at Bad Cannstatt. The Daimler Motoren Gesellschaft was established four years later in 1890. On 1 July 1926 Benz and Daimler merged to become Daimler-Benz AG and its products Mercedes-Benz.")
question = nlp("Which innovation for the car was developed by Prince Henry of Prussia in 1911?")


# sentence similarity
print('similarity: ', question.similarity(paragraph)) #0.69861203

# sentence embeddings
print('vector: ', question.vector)  # or apple1.tensor.sum(axis=0)