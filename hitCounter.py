class GetHitCounter:
    # Initialize the hit counter
    LIMIT=300
    def __init__(self) -> None:
        self.hitDict = {}
    def hit(self,timestamp):
        if timestamp in self.hitDict:
            self.hitDict[timestamp] += 1
        else:
            self.hitDict[timestamp] = 1
    def getHits(self,timestamp):
        hitSum = 0
        remArr = []
        for key in self.hitDict:
            if key > timestamp - self.LIMIT:
                hitSum += self.hitDict[key]
            else:
                remArr.append(key)
        for key in remArr:
            del self.hitDict[key]
        
        return hitSum

counter = GetHitCounter();
counter.hit(1);

counter.hit(2);

counter.hit(3);

print(counter.getHits(4));

counter.hit(300);
counter.hit(300);
counter.hit(300);
counter.hit(300);


print(counter.getHits(300));



print(counter.getHits(308));
print(counter.getHits(308));


