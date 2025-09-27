from flask import Flask, render_template, request, jsonify
import time
import random
from utils.essay_grader import grade_essay

app = Flask(__name__)

sources = [
    {
        "title": "John Dickinson, Letters from a Farmer in Pennsylvania, 1767-1768",
        "url": "https://www.gilderlehrman.org/sites/default/files/inline-pdfs/Dickinson%27s%20Second%20Letter_0.pdf",
        "type": "text",
        "content": "There is another late act of parliament, which appears to me to be unconstitutional, and as destructive to the liberty of these colonies, as that mentioned in my last letter; that is, the act for granting the duties on paper, glass, &c. The parliament unquestionably possesses a legal authority to regulate the trade of Great Britain, and all her colonies. Such an authority is essential to the relation between a mother country and her colonies; and necessary for the common good of all. He who considers these provinces as states distinct from the British Empire, has very slender notions of justice, or of their interests. We are but parts of a whole; and therefore there must exist a power somewhere to preside, and preserve the connection in due order. This power is lodged in the parliament; and we are as much dependent on Great Britain, as a perfectly free people can be on another."
    },
    {
        "title": "The Interesting Narrative of the Life of Olaudah Equiano, 1789",
        "url": "https://www.gutenberg.org/files/15399/15399-h/15399-h.htm",
        "type": "text",
        "content": "The first object which saluted my eyes when I arrived on the coast was the sea, and a slave ship, which was then riding at anchor, and waiting for its cargo. This filled me with astonishment, which was soon converted into terror when I was carried on board. I was immediately handled and tossed up to see if I were sound by some of the crew; and I was now persuaded that I had gotten into a world of bad spirits, and that they were going to kill me. Their complexions too differing so much from ours, their long hair, and the language they spoke, (which was very different from any I had ever heard) united to confirm me in this belief. Indeed such were the horrors of my views and fears at the moment, that, if ten thousand worlds had been my own, I would have freely parted with them all to have exchanged my condition with that of the meanest slave in my own country. Consequently, I was unwilling to quit the sight of the land; which I looked upon with the utmost eagerness, and wished to be again among the mountains and valleys of my native country."
    },
    {
        "title": "Diary of Mary Cooper, 1768-1773",
        "url": "https://www.longislandhistoricsocieties.org/uploads/2/4/9/9/24995994/the_diary_of_mary_cooper.pdf",
        "type": "text",
        "content": "I am this day forty six years old. A poor, distressed, worthless worm, but hope in the mercy of God that he will spair me a little longer… I am for ever hurried and this day am very much so. My daughter is gone to a spinning frolick and I am left alone. I am this day fifty years old, and a poor, distressed, worthless worm, whose whole life has been a continued scene of hurry and confusion, but I hope in the mercy of God that he will pardon my sins and accept of me for Christ’s sake. I have been to meeting and am returned home, but my mind is not so composed as I could wish. The world, the flesh, and the devil are too busy with me. I am very much tired and my mind is much disturbed. I have been to a meeting of the Daughters of Liberty and am returned home. I am very much pleased with the spirit of patriotism that prevails among us. We are all determined to do what we can to assist our country in this time of distress."
    },
    {
        "title": "Abigail Adams to John Adams, 1776",
        "url": "https://www.masshist.org/digitaladams/archive/doc?id=L17760331aa",
        "type": "text",
        "content": "I long to hear that you have declared an independency—and by the way in the new Code of Laws which I suppose it will be necessary for you to make I desire you would Remember the Ladies, and be more generous and favourable to them than your ancestors. Do not put such unlimited power into the hands of the Husbands. Remember all Men would be tyrants if they could. If perticuliar care and attention is not paid to the Laidies we are determined to foment a Rebelion, and will not hold ourselves bound by any Laws in which we have no voice, or Representation."
    },
    {
        "title": "John Dickinson, Letters from a Farmer in Pennsylvania, 1767-1768",
        "url": "https://www.gilderlehrman.org/sites/default/files/inline-pdfs/Dickinson%27s%20Second%20Letter_0.pdf",
        "type": "text",
        "content": "We are therefore—I speak it with grief—I speak it with indignation—we are slaves. The late act is as much a violation of our rights, as that which was passed for the same purpose in the reign of Charles the First, and which cost that monarch his head. I hope, I have shewn, that a power to lay taxes for the purpose of raising a revenue, is not necessary for the regulation of trade; and that if it was, it has been fully and fairly exercised by the colonies themselves. I hope, I have also shewn, that the stamp-act, and the late act, are founded on the same principles; and that if the parliament has a right to lay one, it has a right to lay the other. If they have a right to lay a tax of one penny on us, they have a right to lay a million. If they have a right to tax us at all, they have a right to tax us to any amount they please. For where is the line to be drawn between a shilling and a pound? Between a pound and a million? There is no line to be drawn. The parliament has either a right to tax us, or it has not. If it has a right, it may tax us to any amount. If it has not, it cannot tax us at all."
    },
    {
        "title": "The Bloody Massacre perpetrated in King-Street Boston on March 5th 1770",
        "url": "https://www.gilderlehrman.org/sites/default/files/inline-pdfs/Revere%27s%20Engraving%20of%20the%20Boston%20Massacre%2C%201770.pdf",
        "type": "image"
    },
    {
        "title": "A colonial American shipwright at work, late 18th century",
        "url": "https://c8.alamy.com/comp/B4N6XW/colonial-shipwright-at-work-in-an-american-shipyard-in-the-1700s-B4N6XW.jpg",
        "type": "image"
    }
]

search_status = {"current_source": 0, "total_sources": len(sources)}

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/generate_dbq', methods=['GET', 'POST'])
def generate_dbq():
    if request.method == 'POST':
        global search_status
        search_status = {"current_source": 0, "total_sources": len(sources)}

        for i in range(len(sources)):
            search_status["current_source"] = i + 1
            time.sleep(random.randint(5, 15))

        return jsonify(sources)
    return render_template('generate_dbq.html')

@app.route('/search_status')
def get_search_status():
    return jsonify(search_status)

@app.route('/submit_essay', methods=['GET', 'POST'])
def submit_essay():
    if request.method == 'POST':
        essay = request.form['essay']
        feedback = grade_essay(essay)
        rubric_max_scores = {'Thesis': 1, 'Contextualization': 1, 'Evidence': 3, 'Analysis_and_Reasoning': 2}
        return render_template('feedback.html', feedback=feedback, rubric_max_scores=rubric_max_scores)
    return render_template('submit_essay.html')

if __name__ == '__main__':
    app.run(debug=True)