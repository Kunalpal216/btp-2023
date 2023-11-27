import pprint
import time
import google.generativeai as palm
from google.generativeai.types import safety_types
from prompt import get_prompt

palm.configure(api_key='AIzaSyCtuUpyWk6S5e-eDb1gJvCL7V6wd7Lc_P0')

def details_extractor(article):
    models = [m for m in palm.list_models() if 'generateText' in m.supported_generation_methods]
    model = models[0].name
    print(model)
    prompt = get_prompt(article)
    completion = palm.generate_text(
        model=model,
        prompt=prompt,
        temperature=0,
        max_output_tokens=1500,
        safety_settings=[
            {
                "category": safety_types.HarmCategory.HARM_CATEGORY_DEROGATORY,
                "threshold": safety_types.HarmBlockThreshold.BLOCK_NONE
            },
            {
                "category": safety_types.HarmCategory.HARM_CATEGORY_VIOLENCE,
                "threshold": safety_types.HarmBlockThreshold.BLOCK_NONE,
            },
            {
                "category": safety_types.HarmCategory.HARM_CATEGORY_TOXICITY,
                "threshold": safety_types.HarmBlockThreshold.BLOCK_NONE,
            },
            {
                "category": safety_types.HarmCategory.HARM_CATEGORY_SEXUAL,
                "threshold": safety_types.HarmBlockThreshold.BLOCK_NONE,
            },
            {
                "category": safety_types.HarmCategory.HARM_CATEGORY_DANGEROUS,
                "threshold": safety_types.HarmBlockThreshold.BLOCK_NONE,
            },
            {
                "category": safety_types.HarmCategory.HARM_CATEGORY_MEDICAL,
                "threshold": safety_types.HarmBlockThreshold.BLOCK_NONE,
            }
        ]
    )
    print(completion.result)
    time.sleep(0.1)
    return completion.result;

details_extractor(" 11/02/2023, Man Rams Car Into Police Picket, Kills Constable In Delhi: Cops The accident took place around 4 am at Al-Kauser picket when the accused, Samit Yadav, dozed off while he was returning from a hospital after attending to his COVID-19 positive wife, police said. India NewsPress Trust of IndiaUpdated: May 01, 2021 2:45 pm IST Man Rams Car Into Police Picket, Kills Constable In Delhi: Cops The constable was rushed to AIIMS where he died during the treatment, police said. (Representational) New Delhi: A 42-year-old man allegedly rammed his car into a police picket, killing a constable in southwest Delhi's Vasant Vihar area early on Saturday morning, officials said. The accident took place around 4 am at Al-Kauser picket when the accused, Samit Yadav, dozed off while he was returning from a hospital after attending to his COVID-19 positive wife, police said. The constable was identified as Munshi Lal, 57, they said. The offending vehicle, Honda CRV, rammed into the picket tent that was erected for staff to ensure lockdown and dragged Lal for 30 to 40 meters Deputy Commissioner of Police (southwest) Ingit Pratap Singh said. The constable was rushed to AIIMS trauma center where he died during the course of treatment, he said. Yadav, a resident of Munirka, who works in IT sector, was apprehended from the spot, police said. He told police that he felt asleep while returning from Max Hospital, Gurgaon, to attend to his wife, the police said. Yadav was taken to Vasant Vihar police station and given a PPE kit and isolated in police station premises. His medical test will be conducted soon, police said, adding a case has been registered under relevant sections of law and investigation is underway. Listen to the latest songs, only on JioSaavn.com Mr Lal, an ex-serviceman, was posted in Vasant Vihar police station since August 28, 2020, police said.");


# AIzaSyCDJ28lMyK7UbSUNUN_KeMTZa-rzd0GiWU