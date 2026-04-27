#Router

from phase1 import vectorstore

def route(post_content, threshold=0.5):             #this function tells which bot post is best
    results = vectorstore.similarity_search_with_score(post_content)     #compare the database to users posts return score

    matched_bots = []                        # make empty list where matching bots stores

    for doc, score in results:               #check every result
        if score < threshold:
            matched_bots.append(doc.metadata["bot_id"])     # taking bot name from the metadata and add in list स

    return matched_bots