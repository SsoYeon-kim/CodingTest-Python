a, b, c = map(int, input().split())

if b >= c:
    print(-1)
else:
    print(int(a/(c-b)+1))

# a+b*n = c*n 일 때 비용과 수입이 같아짐
# b>=c일 경우 손익분기점이 나타나지 않음
# a/(c-b)대 생산을 했을 때 수입과 비용이 같아지기 때문에 +1때 손익분기점