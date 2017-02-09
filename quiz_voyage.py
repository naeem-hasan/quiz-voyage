import facebook
import score_counter as sc
import logging
import respond
from string import punctuation
from time import sleep

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

ACCESS_TOKEN = "EAACEdEose0cBAPOvJMj1VuLl4LRXTm3JkZBQCYlhcT8yL3qhiVlOFGoKPY7GwvrTNVoEjmVToNxuZBa6E0yNUyyZAv8krDUqB8ZCpl8Esjilq2tZAX78aWXN17SYkrgzQR3EPeYaDMZBCYGFXx0qrRBQuh9yralO6o3rF0MdcHFAZDZD"
graph = facebook.GraphAPI(ACCESS_TOKEN)


def post_string(string):
    return graph.put_object(parent_object="", connection_name="feed", message=string)


def post_comment(post_id, comment):
    return graph.put_object(parent_object=post_id, connection_name="comments", message=comment)


def check_comments(post_id, correct_answer):
    comments = graph.get_object(post_id + "/comments", fields="from,message")
    if "data" in comments:
        for each in comments["data"]:
            comment = " ".join(each["message"].split())
            logger.debug("Checking comment: %s" % comment)
            if correct_answer.lower().translate(None, (punctuation + " ")) in comment.lower().encode('ascii', 'ignore').translate(None, (punctuation + " ")):
                logger.info("Answer exists in the comment.")
                if comment[-2] == " " and comment[-1] in "shrg":
                    return [True, comment[-1], each["from"]["name"]]

    return [False]


def run_voyage(question_set):
    question_index = 1
    while question_set.is_next_available():
        logger.info("Question available.")
        current_question = question_set.get_next_question()
        logger.debug("Current question is: %s" % current_question.question)
        current_post = post_string("#%d\n%s [%d]" % (question_index, current_question.question, current_question.point))
        question_index += 1
        logger.info("Made a post.")
        answer_found = False
        while not answer_found:
            details = check_comments(current_post["id"], current_question.answer)
            logger.info("Comments loaded and they are checked.")
            if details[0]:
                logger.info("Correct answer found.")
                sc.process_scores(details[1], details[2], current_question.point)
                logger.info("Points added to the database.")
                post_comment(current_post["id"], respond.thats_correct(details[2]))
                logger.info("Commented.")
                answer_found = True
            else:
                logger.info("Answer not found. Trying again.")
            sleep(5)

    sleep(5)
    logger.info("Quizzing done.")
    post_string(respond.render_result(sc.house_scores, sc.individual_scores))
    logger.info("Rendered a result post and it is posted.")

if __name__ == '__main__':
    import scramble
    run_voyage(scramble.Scrambles())
