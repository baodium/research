import matplotlib.pyplot as plt

data = [
    {
        "published_date": "4/19/2018 4:51",
        "comment_toxicity": 0.99239194
    },
    {
        "published_date": "4/19/2018 15:16",
        "comment_toxicity": 0.9874958
    },
    {
        "published_date": "4/18/2018 21:57",
        "comment_toxicity": 0.97575843
    },
    {
        "published_date": "4/19/2018 11:51",
        "comment_toxicity": 0.96770984
    },
    {
        "published_date": "4/19/2018 5:25",
        "comment_toxicity": 0.9675589
    },
    {
        "published_date": "4/19/2018 3:53",
        "comment_toxicity": 0.9539183
    },
    {
        "published_date": "4/19/2018 0:18",
        "comment_toxicity": 0.951087
    },
    {
        "published_date": "4/19/2018 7:03",
        "comment_toxicity": 0.94142056
    },
    {
        "published_date": "4/19/2018 11:30",
        "comment_toxicity": 0.8468856
    },
    {
        "published_date": "4/18/2018 23:00",
        "comment_toxicity": 0.84371877
    },
    {
        "published_date": "4/19/2018 14:57",
        "comment_toxicity": 0.82595015
    },
    {
        "published_date": "4/19/2018 16:48",
        "comment_toxicity": 0.8220205
    },
    {
        "published_date": "4/18/2018 21:09",
        "comment_toxicity": 0.7851712
    },
    {
        "published_date": "4/18/2018 21:30",
        "comment_toxicity": 0.78130203
    },
    {
        "published_date": "4/19/2018 1:56",
        "comment_toxicity": 0.76823187
    },
    {
        "published_date": "4/19/2018 10:28",
        "comment_toxicity": 0.7144925
    },
    {
        "published_date": "4/19/2018 3:40",
        "comment_toxicity": 0.7009271
    },
    {
        "published_date": "4/18/2018 23:56",
        "comment_toxicity": 0.7009271
    },
    {
        "published_date": "4/19/2018 0:27",
        "comment_toxicity": 0.64452356
    },
    {
        "published_date": "4/18/2018 21:44",
        "comment_toxicity": 0.64452356
    },
    {
        "published_date": "4/19/2018 15:05",
        "comment_toxicity": 0.64452356
    },
    {
        "published_date": "4/19/2018 15:20",
        "comment_toxicity": 0.6236596
    },
    {
        "published_date": "4/19/2018 12:41",
        "comment_toxicity": 0.5933285
    },
    {
        "published_date": "4/19/2018 0:08",
        "comment_toxicity": 0.57823396
    },
    {
        "published_date": "4/19/2018 22:27",
        "comment_toxicity": 0.5588107
    },
    {
        "published_date": "4/19/2018 6:22",
        "comment_toxicity": 0.5269066
    },
    {
        "published_date": "4/19/2018 3:02",
        "comment_toxicity": 0.505243
    },
    {
        "published_date": "4/19/2018 15:11",
        "comment_toxicity": 0.46095464
    },
    {
        "published_date": "4/19/2018 16:54",
        "comment_toxicity": 0.41553274
    },
    {
        "published_date": "4/19/2018 14:17",
        "comment_toxicity": 0.40557852
    },
    {
        "published_date": "4/19/2018 4:16",
        "comment_toxicity": 0.4054363
    },
    {
        "published_date": "4/19/2018 21:10",
        "comment_toxicity": 0.4009967
    },
    {
        "published_date": "4/20/2018 2:59",
        "comment_toxicity": 0.39283583
    },
    {
        "published_date": "4/19/2018 15:56",
        "comment_toxicity": 0.3889421
    },
    {
        "published_date": "4/19/2018 4:51",
        "comment_toxicity": 0.3889421
    },
    {
        "published_date": "4/19/2018 16:40",
        "comment_toxicity": 0.38429213
    },
    {
        "published_date": "4/19/2018 13:50",
        "comment_toxicity": 0.3838311
    },
    {
        "published_date": "4/19/2018 4:53",
        "comment_toxicity": 0.3823185
    },
    {
        "published_date": "4/19/2018 0:14",
        "comment_toxicity": 0.34974855
    },
    {
        "published_date": "4/19/2018 15:08",
        "comment_toxicity": 0.311235
    },
    {
        "published_date": "4/19/2018 10:56",
        "comment_toxicity": 0.30849954
    },
    {
        "published_date": "4/19/2018 1:07",
        "comment_toxicity": 0.3084489
    },
    {
        "published_date": "4/18/2018 23:18",
        "comment_toxicity": 0.27581513
    },
    {
        "published_date": "4/18/2018 23:49",
        "comment_toxicity": 0.23754409
    },
    {
        "published_date": "4/19/2018 22:15",
        "comment_toxicity": 0.22677228
    },
    {
        "published_date": "4/19/2018 4:19",
        "comment_toxicity": 0.21058422
    },
    {
        "published_date": "4/19/2018 21:01",
        "comment_toxicity": 0.20870788
    },
    {
        "published_date": "4/19/2018 4:19",
        "comment_toxicity": 0.2039859
    },
    {
        "published_date": "4/19/2018 4:55",
        "comment_toxicity": 0.19996315
    },
    {
        "published_date": "4/19/2018 5:11",
        "comment_toxicity": 0.18456101
    },
    {
        "published_date": "4/19/2018 15:02",
        "comment_toxicity": 0.18423413
    },
    {
        "published_date": "4/18/2018 21:52",
        "comment_toxicity": 0.13020806
    },
    {
        "published_date": "4/18/2018 22:26",
        "comment_toxicity": 0.1278128
    },
    {
        "published_date": "4/19/2018 15:06",
        "comment_toxicity": 0.11394651
    },
    {
        "published_date": "4/19/2018 5:24",
        "comment_toxicity": 0.110666186
    },
    {
        "published_date": "4/18/2018 21:49",
        "comment_toxicity": 0.11027557
    },
    {
        "published_date": "4/18/2018 21:24",
        "comment_toxicity": 0.11027555
    },
    {
        "published_date": "4/19/2018 8:40",
        "comment_toxicity": 0.10916616
    },
    {
        "published_date": "4/19/2018 4:31",
        "comment_toxicity": 0.10458933
    },
    {
        "published_date": "4/19/2018 19:55",
        "comment_toxicity": 0.089784525
    },
    {
        "published_date": "4/18/2018 21:43",
        "comment_toxicity": 0.080773786
    },
    {
        "published_date": "4/19/2018 5:32",
        "comment_toxicity": 0.056836408
    },
    {
        "published_date": "4/19/2018 15:09",
        "comment_toxicity": 0.055265892
    },
    {
        "published_date": "4/19/2018 5:34",
        "comment_toxicity": 0.05357874
    },
    {
        "published_date": "4/18/2018 21:47",
        "comment_toxicity": 0.051198483
    },
    {
        "published_date": "4/19/2018 7:04",
        "comment_toxicity": 0.051092103
    },
    {
        "published_date": "4/19/2018 3:51",
        "comment_toxicity": 0.051039618
    },
    {
        "published_date": "4/18/2018 21:35",
        "comment_toxicity": 0.0419906
    },
    {
        "published_date": "4/19/2018 3:52",
        "comment_toxicity": 0.039931744
    },
    {
        "published_date": "4/19/2018 7:03",
        "comment_toxicity": 0.037542965
    },
    {
        "published_date": "4/19/2018 8:41",
        "comment_toxicity": 0.036404077
    },
    {
        "published_date": "4/19/2018 0:59",
        "comment_toxicity": 0.008075628
    },
    {
        "published_date": "4/21/2018 0:17",
        "comment_toxicity": 0.95348823
    },
    {
        "published_date": "4/20/2018 13:34",
        "comment_toxicity": 0.9335144
    },
    {
        "published_date": "4/22/2018 18:09",
        "comment_toxicity": 0.87163895
    },
    {
        "published_date": "4/20/2018 9:41",
        "comment_toxicity": 0.64772373
    },
    {
        "published_date": "4/20/2018 5:19",
        "comment_toxicity": 0.54766345
    },
    {
        "published_date": "4/19/2018 12:02",
        "comment_toxicity": 0.36739603
    },
    {
        "published_date": "4/19/2018 12:22",
        "comment_toxicity": 0.35939196
    },
    {
        "published_date": "4/23/2018 21:45",
        "comment_toxicity": 0.13667394
    },
    {
        "published_date": "4/24/2018 3:14",
        "comment_toxicity": 0.10769081
    }
]

# import json

# with open('data.json') as f:
#     data_unsorted = json.load(f)

# data = sorted(data_unsorted, key=lambda k: k['published_date'])

def calc_avg_dist(bin_list):
    dists = []
    for a in bin_list:
        for b in bin_list:
            if (a != b):
                dist = abs(b - a)
                dists.append(dist)
    avg_dist = round( ( sum(dists) / len(dists) ) , 2)
    return avg_dist

print('creating bins...')
bin1, bin2, bin3, bin4, bin5, bin6, bin7, bin8, bin9, bin10 = (
    [] for i in range(10))

print('assigning members to bins...')
for count, x in enumerate(data):
    if round(x['comment_toxicity'], 1) <= 0.1:
        bin1.append(count)
    elif round(x['comment_toxicity'], 1) <= 0.2:
        bin2.append(count)
    elif round(x['comment_toxicity'], 1) <= 0.3:
        bin3.append(count)
    elif round(x['comment_toxicity'], 1) <= 0.4:
        bin4.append(count)
    elif round(x['comment_toxicity'], 1) <= 0.5:
        bin5.append(count)
    elif round(x['comment_toxicity'], 1) <= 0.6:
        bin6.append(count)
    elif round(x['comment_toxicity'], 1) <= 0.7:
        bin7.append(count)
    elif round(x['comment_toxicity'], 1) <= 0.8:
        bin8.append(count)
    elif round(x['comment_toxicity'], 1) <= 0.9:
        bin9.append(count)
    else:
        bin10.append(count)

# print out the bins here like : 
print(bin4)

print('calculating average distances for each bin...')
distances = {
    'bin1'  : calc_avg_dist(bin1),
    'bin2'  : calc_avg_dist(bin2),
    'bin3'  : calc_avg_dist(bin3),
    'bin4'  : calc_avg_dist(bin4),
    'bin5'  : calc_avg_dist(bin5),
    'bin6'  : calc_avg_dist(bin6),
    'bin7'  : calc_avg_dist(bin7),
    'bin8'  : calc_avg_dist(bin8),
    'bin9'  : calc_avg_dist(bin9),
    'bin10' : calc_avg_dist(bin10)
}

print(distances)