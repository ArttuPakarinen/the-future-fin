import pytest
from src import translate

SHORT_TEXT = """“Oh come on, you had me until…” My mother waved her hand.
“Maybe, maybe, maybe… That’s just – acid conjecture, like the ‘we are in a simulation’ lunatics. Here are the facts: Joan is a plain woman in her fifties who’s going to find out that the wonderful world she is setting out to join is just a refugee ship of broken people with broken lives, and she doesn’t have the sexual power she had in her twenties, and she’s going to end up burying her regrets in cat litter. And all the money she thinks she’s going to get from Bill, well that’s just going to the lawyers and two houses and eighteen vacations. It’s pathetic, and I hate her with all my heart for sowing this stupidity in the minds of her friends. She screwed up, she got greedy, she overreached – and now she’s fallen out of the cruise ship, and we cannot circle back to find her.”
My mother gnawed at her thumb. “She’s so sad, she needs someone…”
----- PAGE BREAK ----- 317"""

MEDIUM_TEXT = """----- PAGE BREAK ----- 317
“She had someone – she had Bill and a decent marriage. But someone put the worm in her ear, and now she’s trying to put the worm in your ear – don’t let her, don’t do it, it’s a hole with no bottom, you know it!”
“So I’m supposed to just – abandon her, in her hour of need?”
My father shrugged angrily. “She abandoned Bill. She’s got nothing to complain about.”
They moved on, and their voices no longer slid round the semicircle of the stone statue’s outstretched hands to my cupped ears.
I’d heard enough. Women had to be wrangled, their sympathies were their weakness.
Or, as my father once told me, “Women will always find someone or something to mother – if they don’t have kids, it’s cats or immigrants.”
I sometimes wished that the whole world was women, when I was running for office.
Anyway, I grew sick of my own inner ramblings – I felt a sudden savage yearning for action, and instantly remembered my own eldest son, who I had grudgingly taken to a petting zoo when he was young, because – according to my wife – he was turning into a little brat in pre‐K.
He was so goddamned mournful, that boy, almost from the beginning – he moped and sighed, and was congenitally ungrateful, which drove me quite mad – I fantasized that my wife had had an affair with some man‐bun soy‐drip barista at the local coffee shop.
Jake just talked and talked – he once complained that he was dying of boredom.
“You can’t die of boredom!” I snapped.
“How do you know?”
“Because I’ve spent months listening to you go on and on about that Robocraft game!”
I had to savagely cut him off when he went on these – “rambletangents” I called them. Endless stories of his dreams and ideas and plans – I didn’t even bother to listen, just thought my own thoughts and went all Zen and into the future, like he was a trickling brook of vapid nonsense.
My daughter was a talker too, but you could get a word in edgewise. I remember her describing her ideal restaurant once – in the woods, high in a treetop, birds on the leaves, rope swings and koi ponds – it was entertaining enough to interest me… I added in some robot waiters, and it was actually kind of fun…
But my eldest son, the whiner who wouldn’t get a haircut until I held him down, I spend most of his childhood just – shutting him up. He was like an impossible leaky house – every hole you patched just bled drippy water somewhere else.
----- PAGE BREAK ----- 318"""

TEXT = """“Oh come on, you had me until…” My mother waved her hand.
“Maybe, maybe, maybe… That’s just – acid conjecture, like the ‘we are in a simulation’ lunatics. Here are the facts: Joan is a plain woman in her fifties who’s going to find out that the wonderful world she is setting out to join is just a refugee ship of broken people with broken lives, and she doesn’t have the sexual power she had in her twenties, and she’s going to end up burying her regrets in cat litter. And all the money she thinks she’s going to get from Bill, well that’s just going to the lawyers and two houses and eighteen vacations. It’s pathetic, and I hate her with all my heart for sowing this stupidity in the minds of her friends. She screwed up, she got greedy, she overreached – and now she’s fallen out of the cruise ship, and we cannot circle back to find her.”
My mother gnawed at her thumb. “She’s so sad, she needs someone…”
----- PAGE BREAK ----- 317
“She had someone – she had Bill and a decent marriage. But someone put the worm in her ear, and now she’s trying to put the worm in your ear – don’t let her, don’t do it, it’s a hole with no bottom, you know it!”
“So I’m supposed to just – abandon her, in her hour of need?”
My father shrugged angrily. “She abandoned Bill. She’s got nothing to complain about.”
They moved on, and their voices no longer slid round the semicircle of the stone statue’s outstretched hands to my cupped ears.
I’d heard enough. Women had to be wrangled, their sympathies were their weakness.
Or, as my father once told me, “Women will always find someone or something to mother – if they don’t have kids, it’s cats or immigrants.”
I sometimes wished that the whole world was women, when I was running for office.
Anyway, I grew sick of my own inner ramblings – I felt a sudden savage yearning for action, and instantly remembered my own eldest son, who I had grudgingly taken to a petting zoo when he was young, because – according to my wife – he was turning into a little brat in pre‐K.
He was so goddamned mournful, that boy, almost from the beginning – he moped and sighed, and was congenitally ungrateful, which drove me quite mad – I fantasized that my wife had had an affair with some man‐bun soy‐drip barista at the local coffee shop.
Jake just talked and talked – he once complained that he was dying of boredom.
“You can’t die of boredom!” I snapped.
“How do you know?”
“Because I’ve spent months listening to you go on and on about that Robocraft game!”
I had to savagely cut him off when he went on these – “rambletangents” I called them. Endless stories of his dreams and ideas and plans – I didn’t even bother to listen, just thought my own thoughts and went all Zen and into the future, like he was a trickling brook of vapid nonsense.
My daughter was a talker too, but you could get a word in edgewise. I remember her describing her ideal restaurant once – in the woods, high in a treetop, birds on the leaves, rope swings and koi ponds – it was entertaining enough to interest me… I added in some robot waiters, and it was actually kind of fun…
But my eldest son, the whiner who wouldn’t get a haircut until I held him down, I spend most of his childhood just – shutting him up. He was like an impossible leaky house – every hole you patched just bled drippy water somewhere else.
----- PAGE BREAK ----- 318
He did, though, eventually.
Shut the hell up…
I had pretended to read a few books on parenting – slipping my cell phone between the pages so I could actually get something done – and knew that I wasn’t supposed to make him like me – which would’ve been all right, if he had wanted to be anything at all. But he was born silent – I thought he was retarded at first, or whatever word you were supposed to use in the current minute, but I could tell his perceptiveness from across the room. He was silent, he moped, he was a drip – but he was – he judged, too.
Judged me, in that involuntary way that some children have, like they are little conscience‐computers that chatter without control, like dreams. Thank God my second son was a mindless charismatic athletic ape who poured himself like quicksilver into whatever popular container came jostling along the cultural conveyor belt.
I was at – damn these memories, last one! – this petting zoo, when my eldest son – who was inexplicably obsessed with ducks – ah, his face lit up when he saw two of the foot‐sized white birds in an enclosure, next to some African cow with a tumour for a neck – and he ran forwards to the gate waving his arms like a conductor windmilling at the edge of a cliff – then wrestling with some vaguely complicated latch – and he turned to me with a contemptible agonized begging expression – and I can still feel the wild cold rage, even now, hundreds of years after Jake’s demise, because he loved the ducks, he cared about the ducks, but he only regretfully needed me to open the latch, swing the gate, and give him access to that which he treasured – I was only a means to his end – his end was never me, his love was never for me – and if he could’ve opened that latch himself, he would have poured his heart into those stupid birds and forgotten me entirely!
And what sort of boy wants to pick up and caress fluffy little birds?
I made a mistake, that day, which I worried about for over a week.
I did not hit him – I did, at other times – many times – I felt I wanted to drive the softness out of him, like hammering a nail can push wood out from the bottom of a plank – but my cold calculations led me to public error that day…
I watched as my son cooed over and petted the ducks. I did not enter the enclosure. I really liked my shoes, they were a rare gift from me to me.
Jake was picking up tiny leaves and plants, trying to feed them to the ducks, which showed little interest.
“We’ve got food, you know,” said a bored blonde teenage girl scrolling through her phone – surely against protocol.
“Cones are two dollars, three for five.” She pointed at a sign which said exactly the same thing – which irritated me even more.
----- PAGE BREAK ----- 319"""


def test_open_file():
    assert (
        "“So I’m supposed to just – abandon her, in her hour of need?”"
        in translate.open_file("../data/example.txt")
    )


def test_validate_file():
    assert translate._validate_file("txt", "Hello") == True
    with pytest.raises(ValueError):
        translate._validate_file("humbug", "Hello")


def test_translate_with_google():
    assert translate.translate_with_google("Hello", "fi") == "Hei"


def test_translate_with_deepl():
    assert translate.translate_with_deepl("Hello", "fi", 4000) == "Hei"


def test_split_content():
    chunks = translate._split_content("Hello world! \n", chars_per_chunk=5000)
    total_size = len(TEXT.encode("utf-8"))
    assert 10000 > total_size > 5000
    chunks = translate._split_content(TEXT, chars_per_chunk=5000)
    assert len(chunks) == 2
    assert "----- PAGE BREAK ----- 319" in chunks[-1]

    whole_text = "".join(chunks)
    total_size = len(SHORT_TEXT.encode("utf-8"))
    assert 1000 > total_size > 900

    chunks = translate._split_content(SHORT_TEXT, chars_per_chunk=100)
    assert len(chunks) == 3 == len(SHORT_TEXT) / 100
    whole_text = "".join(chunks)
    assert SHORT_TEXT == whole_text


def test_translate_file(monkeypatch):
    def mock_translate_with_deepl(
        translator, content: str, target_lang: str = "EN"
    ) -> str:
        return content.replace("SIVUNVAIHTO", "PAGE BREAK")

    monkeypatch.setattr(translate, "_translate_with_deepl", mock_translate_with_deepl)
    translate.translate_file("../data/example.txt", "FI", chars_per_chunk=4000)
    with open("data/example_fi.txt", "r") as f:
        read_content = f.read()

    assert "She had someone – " in read_content
    assert MEDIUM_TEXT == read_content
