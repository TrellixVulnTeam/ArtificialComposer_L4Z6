import collections


def pitch_histogram(songs, pitches):
    """ histogram-dictionary of played pitches in songs. 0th order n-gram """

    histogram = {pitch: 0 for pitch in pitches}

    for song in songs:
        for pitch in song.pitch:
            histogram[pitch] = histogram[pitch]+1

    return histogram


def following_pitches_histogram(songs, pitches):
    """ histogram-dictionary of 2 following pitches in songs. 1st order n-gram """

    histogram = {(p1, p2): 0 for p1 in pitches for p2 in pitches}

    for song in songs:
        for i in range(len(song.pitch)-1):
            histogram[(song.pitch[i], song.pitch[i+1])] = histogram[(song.pitch[i], song.pitch[i+1])]+1

    return histogram


def n_gram(songs, n):
    """ n-gram dictionary of following pitches """

    histogram = {}
    n = n+1

    for song in songs:
        for i in range(len(song.pitch)-n):
            tmp = []
            for j in range(n):
                # tmp.append(dictionaries["pitch_text"].index(song.pitch[i+j]))
                tmp.append(song.pitch[i + j])

            key = tuple(tmp)
            if key in histogram.keys():
                histogram[key] = histogram[key]+1
            else:
                histogram[key] = 1

    return collections.OrderedDict(sorted(histogram.items(), key=lambda x: x[1], reverse=True))


def interval_n_gram(songs, n):
    """ n-gram dictionary of following intervals """

    histogram = {}

    for song in songs:
        for i in range(len(song.pitch)-n-1):
            tmp = []
            for j in range(n):
                tmp.append(song.pitch[i + j + 1]-song.pitch[i + j])

            key = tuple(tmp)
            if key in histogram.keys():
                histogram[key] = histogram[key]+1
            else:
                histogram[key] = 1

    return collections.OrderedDict(sorted(histogram.items(), key=lambda x: x[1], reverse=True))


def interval_histogram(songs, pitches):
    """ histogram-dictionary of intervals in songs """

    histogram = {interval: 0 for interval in range(min(pitches)-max(pitches), max(pitches)-min(pitches)+1)}
    histogram = collections.OrderedDict(sorted(histogram.items()))

    for song in songs:
        for i in range(len(song.pitch)-1):
            histogram[song.pitch[i+1]-song.pitch[i]] = histogram[song.pitch[i+1]-song.pitch[i]]+1

    return histogram
