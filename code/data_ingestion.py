from datasets import load_dataset, ReadInstruction
import random
random.seed(42)

# From record 10 (included) to record 20 (excluded) of `train` split.
train_10_20_ds = load_dataset('trivia_qa','rc', split=ReadInstruction('train', from_=10, to=20, unit='abs'))

# return search results
train_10_20_ds[0]['search_results']

'''
>>> train_10_20_ds[0].keys()
dict_keys(['answer', 'entity_pages', 'question', 'question_id', 'question_source', 'search_results'])
'''

def search_result_from_question(data, n: int) -> dict:
    out = {}
    for question in data:
        q = question['question']
        qty_orig_source=len(question['search_results']['rank'])
        if (n>qty_orig_source):
            q_filling=n-qty_orig_source
            j=0
            sources={}
            ranks = {}
            for i in range(qty_orig_source):
                sources[i]=question['search_results']['search_context'][i]
                ranks[i]=question['search_results']['rank'][i]
            while(q_filling>0):
                l = random.randrange(len(data))
                m = random.randrange(len(data[l]['search_results']['rank']))
                sources[j+qty_orig_source]=data[l]['search_results']['search_context'][m]
                ranks[j+qty_orig_source]=-1
                q_filling-=1
                j+=1
        else:
            for i in range(n):
                sources[i]=question['search_results']['search_context'][i]
                ranks[i]=question['search_results']['rank'][i]
        out[q]={"sources": sources,
                "ranks": ranks}
    return out


oo = search_result_from_question(train_10_20_ds, 10)
oo
'''
>>> train_10_20_ds[0]['question']
'Which innovation for the car was developed by Prince Henry of Prussia in 1911?'
>>> train_10_20_ds[0]['search_results']
{'description': ['The National Motor Museum Trust. Home; ... He patented his design in 1911. Various motoring magazine pictures show Prince Henry of Prussia in 
a car with simple up and ...'], 
'filename': ['18/18_430.txt'], 
'rank': [2], 
'search_context': ["Motoring Firsts - The National Motor Museum Trust\nThe National Motor Museum Trust\nHome > Story of Motoring > Motoring Firsts\nMotoring Firsts\nAmong 
the questions we are most frequently asked are the various motoring firsts. Listed below are some of the most common questions that have been answered by our Motoring 
Research Service.\nQuestions\nWhat were the first motor cars?\nThe motor car was developed over many years by a number of talented individuals but Karl Benz of Mannheim in Germany
 is normally credited as the Inventor of the Motor Car. In the autumn of 1885, his three-wheeled vehicle became the first successful petrol-engined car. He was awarded a patent for it on 29 January 1886, and became the first motor manufacturer in 1888 with his Modell 3 Benz. 
 In 1886, Gottlieb Daimler and his protégé Wilhelm Maybach built the first successful four-wheeled petrol-driven car at Bad Cannstatt. The Daimler Motoren Gesellschaft was established four years later in 1890. 
 On 1 July 1926 Benz and Daimler merged to become Daimler-Benz AG and its products Mercedes-Benz. Fredrick William Bremer, a plumber and gas fitter, built the first British four-wheeled petrol-engined motor car. 
 Starting work in 1892, when he was 20, the still incomplete car made its first run on a public highway in December 1894.\nWhat was the first motor car to run on the 
 British Highway?\nThere are a number of claims and counter claims for the first motor car to appear on the road in Britain. Frederick William Bremer of Walthamstow
  is believed to have had a four-wheeled car running in late 1894. Both he and James D. Roots may have independently built motorised tricycles as early as 1892. 
  Roots certainly had one powered by an oil engine running on the road in early 1896.\nAnother theory is that the first motor car to run on the British highway was a 2hp Benz Velo imported by
   Henry Hewetson in November 1894, although some believe this may have actually been in 1895. The Hon. Evelyn Ellis certainly imported a Panhard et Levassor into 
   Britain in June 1895.\nBy the end of 1895, following further importations, it was estimated that there were 14 or 15 cars on Britain’s roads, a figure which had
    increased dramatically by 1900 to approximately seven or eight hundred! The million mark for private cars was reached in Britain in 1930, with 10 million in 1967.
    \nJohn Henry Knight of Farnham, Surrey was an engineer and enthusiastic inventor with a keen interest in photography and locomotion. With the help of engineer
     George Parfitt, in 1895 he created the first purpose-built, petrol-driven, three-wheeled car to be run on the roads of Britain. In order to improve stability a
      fourth wheel was added the following year. This pioneering British car is on display at the National Motor Museum.\nCycle makers Charles and Walter Santler of
       Malvern Link, Worcestershire built a steam car in 1889 which was subsequently fitted with a single cylinder gas engine and then rebuilt again with a single
        cylinder ‘petrol’ engine in 1894. Santlers went on to build several other cars between 1897 and 1913 when they launched a range of light cars for general 
sale.\nFrederick Lanchester started work on a four-wheeled petrol car in 1895 which was successfully tested on the road in early 1896. The Lanchester Engine Co. 
commenced building production cars in 1899.\nWhen was the word petrol first used?\nThe term petrol was not used until 1896, when it was patented by Messrs Carless, 
Capel & Leonard of Hackney Wick.\nWhen were windscreen wipers first used?\nThere are various claims for the first windscreen wipers. Some sources say that they were 
first used in France in 1907. British photographer Gladstone Adams is said to have had the idea for wipers whilst driving his Daracq home to Newcastle after watching 
the 1908 FA Cup Final at Crystal Palace (his team Newcastle United had lost 3 – 1 to Wolverhampton Wanderers). He patented his design in 1911.  Various motoring 
magazine pictures show Prince Henry of Prussia in a car with simple up and down squeegee type wiper fitted to the windscreen in 1909. In 1919 (some sources say 1921
) William Folberth of Cleveland, USA, marketed the first automatic windscreen wipers. They were operated by vacuum from the engine's inlet manifold.\nWhere was the 
first motor museum?\nBritain’s first dedicated motor museum was set up by Edmund Dangerfield, Editor of The Motor magazine. Temporarily sited in Oxford Street, 
London, it opened on 31 May 1912 with over forty vehicles built before 1903 and a range of accessories. The exhibition closed on 31 July 1912 and reopened on 12 
March 1914 at the Crystal Palace, Sydenham. The collection remained there until the British Government commandeered the building during World War I, when exhibits w
ere returned to owners, taken in by Government Museums, or dumped on waste ground near Charing Cross Station. This has been described as 'one of the untold tragedies o
f the war'. In 1931 the remaining unplaced vehicles from the 1912 Motor Museum were destroyed. In 1972 five of the saved cars from the original 1912 Museum were 
displayed at the newly opened National Motor Museum at Beaulieu.\nWho was the first person to be charged for a speeding offence?\nWalter Arnold of East Peckham, 
Kent had the dubious honour of being the first person in Great Britain to be successfully charged with speeding on 28 January 1896. Travelling at approximately 
8mph/12.87kph, he had exceeded the 2mph/3.22kph speed limit for towns. Fined one shilling and costs, Arnold had been caught by a policeman who had given chase on a 
bicycle.\nWhen was the first driving licence issued?\nFrance introduced the first driving licences under the Paris Police Ordinance of 14 August 1893. The Motor 
Car Act of 14 August 1903, which took effect on 1 January 1904, introduced the driving licence (along with registration numbers for vehicles and a new speed limit 
of 20mph/32.19kph) into Great Britain.\nWhen were the first driving lessons given?\nThe Motor Carriage Supply Company of London, their instructor being one Mr 
Hankinson, offered the first driving lessons in Britain in June 1900.   The first organisation to title itself a driving school in Britain was the Liver Motor Car 
Depot and School of Automobilism of Birkenhead.  William Lee established the school in May 1901 and its Chief Instructor was Archibald Ford.\nWhen were the first 
driving tests introduced?\nFrance, under the Paris Police Ordinance of 14 August 1893, introduced the first driving test. Introduced on a voluntary basis, on 13 
March 1935, the driving test did not become official in Great Britain until 1 April 1935 and compulsory until 1 June 1935. The first driving test pass certificate 
in Great Britain was awarded on the 16 March 1935 to Mr R.E.L. Beere of Kensington.\nWhen was the first Highway Code published?\nFirst published in booklet form in 
Great Britain in April 1931, it cost one penny.\nWhen did the first motoring fatality occur?\nMrs Bridget Driscoll of Old Town, Croydon became the first motoring 
fatality on 17 August 1896, when she was run over by a Roger-Benz car at Crystal Palace, London. Employed by the Anglo-French Motor Co, Arthur Edsell was driving 
at 4mph/6.44kph when he hit Mrs Driscoll, fracturing her skull in the process. The first driver to die from injuries sustained in a motoring accident was Mr Henry 
Lindfield of Brighton when his electrical carriage overturned on Saturday 12 February 1898. He died of shock the following day, caused by the amputation of one of 
his legs. According to the 19 February 1898 copy of Autocar, he had only driven the car two or three times and the accident was probably ‘due to the fact of the 
speed being so high’ – 16 or 17mph (25–27kph) – ‘a pretty high speed for a novice to maintain.’ The first crash to cause the death of a car passenger occurred on 
25 February 1899 at Grove Hill, Harrow. Major James Stanley Richer, 63, died four days after the accident without regaining consciousness. The driver, Mr E.R. Sewell 
had been demonstrating the vehicle, a Daimler Wagonette, to Major Richer, Department Head at the Army & Navy Stores, with the view to a possible purchase for the 
company. Mr Sewell was killed on the spot, becoming the first driver of a petrol-driven car to die in an accident.\nWhen were the first traffic lights installed?\
    nThe first traffic signals in Britain (and indeed the world) were installed outside the Houses of Parliament on 10 December 1868. They used contemporary 
    railway signalling technology – semaphore arms for day-time use and green or red gas lamps at night. Unfortunately they exploded on the night of 2 January 
    1869 injuring the police constable operating them! The first electric stop-go traffic lights were installed in Cleveland, Ohio in August 1914, with the firs
    t three-colour traffic lights in Detroit in 1919. 1922 saw the first electrically synchronised traffic signals installed in Houston, Texas. In Great Britain
    , manually operated three-colour traffic lights were first used in Piccadilly, London in 1926, with automatic traffic lights making their first appearance o
    n an experimental basis in Princes Square, Wolverhampton, during November 1927. The experiment was presumably a success and the lights became permanent in 1
    930. Pedestrian-operated street crossing lights were first erected on the Brighton Road, Croydon, Surrey in 1932.\nWhere were the first parking meters insta
    lled?\nOklahoma City, USA was the site for the world’s first parking meter, where it was installed in July 1935. An invention of Gerald A. Hale and Professo
    r H.G. Thuesen of Oklahoma State University, the first person to be arrested for a parking meter offence was the Reverend C.H. North of the Third Pentecosta
    l Church of Oklahoma City in August 1935. Britain’s first parking meters made their appearance outside the American Embassy in London’s Grosvenor Square on 
    10 July 1958.\nWhen did the first roadside petrol pumps appear?\nThe first roadside petrol pumps became operational in St Louis, USA in 1905. Roadside petro
    l pumps were first installed in Britain in 1913, though they did not enter into general use until 1921. In 1920 the Automobile Association opened the first 
    roadside petrol station (solely for the purpose of supplying fuel as opposed to being a garage) at Aldermaston, Berkshire. A number of similar stations wer
    e established around the country. They were operated by AA Patrolmen and exclusively for the use of AA members. They established the modern pattern of vehi
    cles pulling off the public road and drawing up alongside petrol pumps rather than being filled at the kerbside as at garages. Britain’s first self-service 
    petrol pump became operational in November 1961 at Southwark Bridge, London."], 'title': ['Motoring Firsts - The National Motor Museum Trust'], 
    
'url': ['http://www.nationalmotormuseum.org.uk/motoring_firsts']}
'''