import pandas as pd
# import word2vec


def compute_score(row, vec):
    sc = 0
    if (type(row) == float):
        return 0
    row = row.replace("\\", "")
    for w in vec:
        if w[0] in row.split(" "):
            sc += 1

    return sc/len(vec)


def manage_keywords(kwds):
    score = []
    good_match = []
    df =  pd.read_csv("DB/questions_cleared.csv", sep=",", low_memory = False, encoding='latin-1')
    
    for i, row in df.iterrows():
        tup = str(i), compute_score(row['Body'], kwds)
        score.append(tup)
        if score[i][1] != 0.0:
            good_match.append(score[i])

    good_match.sort(key=lambda x: x[1], reverse=True)
    # print(good_match[:5])
    return good_match[:5]