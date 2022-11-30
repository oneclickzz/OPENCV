import random
import matplotlib.pyplot as plt


# **평균필터필터

# 평균값을 계산
# 평균 = 총합 / 갯수



# 배치식
# 값의 단위와 양이 매우 크다면 누적된 값의 공간이 커야지만
# 손실없이 보관 및 계산이 가능해서 기본적으로 큰 메모리 공간을 필요로함

# b mb gb tb pb 1000조
# 32bit == 4byte * x
# [1,2,3,4,5,6,7,8,9,10]

samples = []
def meanFilterForBatch():
    global samples

    # t = 0
    # for s in samples:
    #     t += s
    # # mean = t / (i+1)
    # mean = t / len(samples)

    # sum([1,2,3,4,5,6,7,8,9,10])
    mean = sum(samples) / len(samples)

    return mean

# 2^32, 11111111111111111111111111111111 => 0
total = 0
def meanFilterForBatch2(sample, numOfSamples):
    global total

    total += sample
    mean = total / numOfSamples
    return mean


# 50.0~51.0의 랜덤으로 생성되는 최대 1000개의 
# 샘플이 모이는 동안 실시간으로 평균필터된 값을 구하고 (샘플이 추가될때마다)
# 최종 평균을 구하세요


# 3Dof 6Dof 9Dof
sampleCount = 100

meanPlots = []
samplePlots = []

# 평균필터
# for i in range(sampleCount):

#     # 50.0, 50.999999999999
#     sample = random.uniform(50, 51)
#     print(f'[{i+1}] sample: ', sample)
    
#     samples.append(sample)
#     mean = meanFilterForBatch()

#     # total += sample
#     # mean = meanFilterForBatch2()
#     # print(f'[{i+1}] mean: ', mean)

#     samplePlots.append([sample])
#     meanPlots.append([mean])


# 이동평균필터
# 평균을 낼 샘플의 갯수를 지정된 수의 최신 원소들로만 유지하고 해당 원소들로 평균을 구함
x = 10
n = 0
for i in range(sampleCount):

    # 매 10의 배수 횟차마다 n을 증가
    if i % 10 == 0:
        n += 1

    sample = random.uniform(50 + n, 51 + n)
    print(f'[{i+1}] sample: ', sample)

    samples.append(sample)

    # 이동평균

    if len(samples) > x:
        samples.pop(0)
        # samples = samples[1:]

    mean = meanFilterForBatch()

    # total += sample
    # mean = meanFilterForBatch2()

    # print(f'[{i+1}] mean: ', mean)

    samplePlots.append([sample])
    meanPlots.append([mean])



print('result mean: ', mean)

plt.plot(samplePlots, color = 'b', label = 'sample')
plt.plot(meanPlots, color = 'r', label = 'mean', alpha=0.5)
plt.legend(loc = 'best')
plt.show()