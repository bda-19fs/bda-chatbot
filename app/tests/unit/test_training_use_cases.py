from bda_core.use_cases.training.utils import (
    create_language_model
)

concepts = [
    'Dropbox acquired document collaboration company Hackpad in April 2014. A year later, Dropbox launched a Dropbox Notes note-taking product in beta testing phase. Dropbox Paper was officially announced on October 15, 2015, followed by an open beta and release of mobile Android and iOS apps in August 2016. Dropbox Paper was officially released on January 30, 2017.',
    'Writing for "TechRadar", John Brandon wrote that Dropbox Paper "might be a light tool for now without the extensive templates of Microsoft Office or the integration with other apps in the Zoho suite, but it does work well with the Dropbox storage service that is so popular with office workers these days."',
    'Dropbox Paper, or simply Paper, is a collaborative document-editing service developed by Dropbox. Originating from the companys acquisition of document collaboration company Hackpad in April 2014, Dropbox Paper was officially announced in October 2015, and launched in January 2017. It offers a web application, as well as mobile apps for Android and iOS.'
]

questions = [
    'After I cut or chop something up on a cutting board I have the problem of funneling the pieces into a bowl or other container and it typically makes a mess. Normally what I try to do is scrape the pieces with a knife into the bowl or whatever but inevitably some of the pieces miss and go flying off onto the counter or floor. Is there a reliable method of funneling food off a cutting board into a bowl cup or other smaller container?',
    'I am using a dehydrator to make jerky from boneless skinless chicken breasts. Cutting these by hand is too time-consuming and produces uneven pieces which finish dehydrating at various times. What is the quickest way to remove the fat from and evenly slice chicken breasts for jerky?',
    'Certain types of meat like chicken breast seem to have such a short window of being done. Cooking too little can be unhealthy and cooking too much can dry it out. So it seems most cooks are very careful with not overcooking these types of meats. Yet I see all kinds of recipes about how to reuse leftover roast chicken or chicken pot pie recipes where you\'re supposed to cook the chicken first (or use leftover cooked chicken) and then put it in the oven for another 15 - 45 minutes (depending on the recipe). I just can\'t understand how we\'re expected not to severely dry out and overcook the meat in these types of recipes. Is there some kind of a trick I\'m missing? If there is enough liquid are we able to drastically slow the cooking process? But even braised chicken breast can be overcooked without too much extra time. Can we optimize for this second cooking by using large pieces or trying to not completely cook the meat in the first cooking?'
]

def test_create_language_model():
    language_model = create_language_model(concepts, questions)
    assert language_model.shape == (3, 93)
